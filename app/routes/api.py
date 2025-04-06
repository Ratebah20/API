"""
Routes API pour interagir avec l'API Orange Travel B2B.
"""
from flask import Blueprint, request, session, jsonify, current_app
import requests
import json
import re
from datetime import datetime

api_bp = Blueprint('api', __name__)

# Constantes pour les messages d'erreur
ERROR_UNAUTHORIZED = {"error": "Non authentifié"}
ERROR_API_CALL = {"error": "Erreur lors de l'appel à l'API"}
ERROR_INVALID_PARAMS = {"error": "Paramètres invalides"}

def make_api_request(endpoint, access_token, params=None, method='GET', data=None):
    """
    Fait une requête à l'API Orange Travel B2B avec le token d'authentification.
    
    Args:
        endpoint (str): L'endpoint à appeler (doit être une clé du dictionnaire ENDPOINTS dans la config)
        access_token (str): Le token d'accès OAuth 2.0
        params (dict, optional): Paramètres de requête optionnels
        method (str, optional): Méthode HTTP à utiliser (GET, POST, PATCH, etc.)
        data (dict, optional): Données à envoyer dans le corps de la requête (pour POST, PATCH, etc.)
        
    Returns:
        dict: La réponse JSON de l'API ou None en cas d'erreur
    """
    endpoints_map = current_app.config['ENDPOINTS']
    api_base_url = current_app.config['API_BASE_URL']
    
    # Gestion des endpoints dynamiques (ex: transactions/123, offers/456)
    if endpoint not in endpoints_map:
        # Vérifier si c'est un endpoint dynamique comme 'transactions/{id}'
        for base_endpoint in endpoints_map:
            if endpoint.startswith(base_endpoint + '/') or endpoint.startswith(f"suppliers/"):
                full_url = f"{api_base_url}/{endpoint}"
                break
        else:
            return None
    else:
        full_url = f"{api_base_url}/{endpoints_map[endpoint]}"
    
    # La définition de full_url est désormais gérée dans la condition ci-dessus
    headers = {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}

    print(f"Calling API: {full_url}")
    print(f"Headers: {headers}")
    if params:
        print(f"Params: {params}")

    try:
        if method.upper() == 'GET':
            response = requests.get(full_url, headers=headers, params=params, verify=False)
        elif method.upper() == 'POST':
            headers["Content-Type"] = "application/json"
            response = requests.post(full_url, headers=headers, json=data, verify=False)
        elif method.upper() == 'PATCH':
            headers["Content-Type"] = "application/json"
            response = requests.patch(full_url, headers=headers, json=data, verify=False)
        else:
            print(f"Méthode non supportée: {method}")
            return None

        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur API: {str(e)}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Détails: {e.response.text}")
        return None


@api_bp.route('/test/<endpoint>')
def test_api(endpoint):
    """
    Endpoint pour tester les différentes routes de l'API Orange Travel B2B.
    
    Args:
        endpoint (str): L'endpoint à tester (ex: countries, offers, etc.)
    """
    if "access_token" not in session:
        return jsonify({"error": "Non authentifié"}), 401

    endpoints_map = current_app.config['ENDPOINTS']
    
    # Gestion des endpoints dynamiques comme 'offers/{id}' ou 'transactions/{id}'
    if endpoint not in endpoints_map and not any(endpoint.startswith(base + '/') for base in endpoints_map):
        return jsonify({"error": "Endpoint non valide"}), 400

    # Paramètres spécifiques pour certains endpoints
    params = {}
    if endpoint == "offers":
        params = {
            "page": request.args.get("page", "1"),
            "size": request.args.get("size", "10"),
        }
    elif endpoint == "transactions":
        params = {
            "startDate": request.args.get("startDate", "2023-01-01"),
            "endDate": request.args.get("endDate", "2025-12-31"),
        }

    result = make_api_request(endpoint, session["access_token"], params)

    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de l'appel à l'API"}), 500


@api_bp.route('/offers', methods=['GET'])
def get_offers():
    """API pour récupérer la liste des offres disponibles."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    params = {
        "limit": request.args.get("limit", "10"),
        "offset": request.args.get("offset", "0"),
    }
    
    result = make_api_request("offers", session["access_token"], params)
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de la récupération des offres"}), 500


@api_bp.route('/offers/<offer_id>', methods=['GET'])
def get_offer_detail(offer_id):
    """API pour récupérer les détails d'une offre spécifique."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    # Construction de l'endpoint pour une offre spécifique
    custom_endpoint = f"offers/{offer_id}"
    
    result = make_api_request(custom_endpoint, session["access_token"])
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de la récupération des détails de l'offre"}), 500


@api_bp.route('/offers/<offer_id>', methods=['PATCH'])
def customize_offer(offer_id):
    """API pour personnaliser les paramètres d'une offre."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Aucune donnée de personnalisation fournie"}), 400
    
    # Vérifier que les paramètres sont valides selon la documentation de l'API
    valid_params = ["name", "distributor_fees", "distributor_fees_type", "metadata"]
    has_valid_param = False
    
    for param in valid_params:
        if param in data:
            has_valid_param = True
            break
    
    if not has_valid_param:
        return jsonify({"error": "Aucun paramètre valide fourni. Les paramètres modifiables sont: name, distributor_fees, distributor_fees_type, metadata"}), 400
    
    # Construction de l'endpoint pour modifier une offre spécifique
    custom_endpoint = f"offers/{offer_id}"
    
    result = make_api_request(custom_endpoint, session["access_token"], method="PATCH", data=data)
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de la personnalisation de l'offre"}), 500


@api_bp.route('/transactions', methods=['GET'])
def get_transactions():
    """API pour récupérer la liste des transactions."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    params = {
        "startDate": request.args.get("startDate", "2023-01-01"),
        "endDate": request.args.get("endDate", "2025-12-31"),
        "status": request.args.get("status", None),
        "offer": request.args.get("offer", None),
        "supplier": request.args.get("supplier", None),
        "limit": request.args.get("limit", "10"),
        "offset": request.args.get("offset", "0"),
        "user": request.args.get("user", None),
    }
    
    # Supprimer les paramètres None
    params = {k: v for k, v in params.items() if v is not None}
    
    result = make_api_request("transactions", session["access_token"], params)
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de la récupération des transactions"}), 500


@api_bp.route('/transactions/count', methods=['GET'])
def get_transactions_count():
    """API pour récupérer le nombre de transactions correspondant aux critères."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    params = {
        "startDate": request.args.get("startDate", None),
        "endDate": request.args.get("endDate", None),
        "status": request.args.get("status", None),
        "offer": request.args.get("offer", None),
        "supplier": request.args.get("supplier", None),
        "user": request.args.get("user", None),
    }
    
    # Supprimer les paramètres None
    params = {k: v for k, v in params.items() if v is not None}
    
    result = make_api_request("transactions_count", session["access_token"], params)
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors du comptage des transactions"}), 500


@api_bp.route('/transactions/<transaction_id>', methods=['GET'])
def get_transaction_detail(transaction_id):
    """API pour récupérer les détails d'une transaction spécifique."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    # Construction de l'endpoint pour une transaction spécifique
    custom_endpoint = f"transactions/{transaction_id}"
    
    result = make_api_request(custom_endpoint, session["access_token"])
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de la récupération des détails de la transaction"}), 500


@api_bp.route('/transactions', methods=['POST'])
def create_transaction():
    """API pour créer une nouvelle transaction."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    data = request.get_json()
    
    if not data or "offer_id" not in data:
        return jsonify({"error": "Paramètres requis manquants. L'ID de l'offre est obligatoire."}), 400
    
    result = make_api_request("transactions", session["access_token"], method="POST", data=data)
    
    if result:
        return jsonify(result), 201
    return jsonify({"error": "Erreur lors de la création de la transaction"}), 500


@api_bp.route('/suppliers', methods=['GET'])
def get_suppliers():
    """API pour récupérer la liste des fournisseurs disponibles."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    result = make_api_request("suppliers", session["access_token"])
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de la récupération des fournisseurs"}), 500


@api_bp.route('/suppliers/<supplier_id>/simstatus', methods=['GET'])
def get_sim_status(supplier_id):
    """API pour récupérer le statut d'une carte SIM ou eSIM."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    # Récupération des paramètres de requête
    params = {}
    
    transaction_id = request.args.get("transaction")
    sim_id = request.args.get("simId")
    
    if transaction_id:
        params["transaction"] = transaction_id
    elif sim_id:
        params["simId"] = sim_id
    else:
        return jsonify({"error": "Paramètre 'transaction' ou 'simId' requis"}), 400
    
    # Construction de l'endpoint
    custom_endpoint = f"suppliers/{supplier_id}/simstatus"
    
    result = make_api_request(custom_endpoint, session["access_token"], params=params)
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de la récupération du statut de la SIM"}), 500


@api_bp.route('/suppliers/<supplier_id>/usagebalances', methods=['GET'])
def get_usage_balances(supplier_id):
    """API pour récupérer les consommations restantes d'une carte SIM ou eSIM."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    # Récupération des paramètres de requête
    params = {}
    
    transaction_id = request.args.get("transaction")
    sim_id = request.args.get("simId")
    
    if transaction_id:
        params["transaction"] = transaction_id
    elif sim_id:
        params["simId"] = sim_id
    else:
        return jsonify({"error": "Paramètre 'transaction' ou 'simId' requis"}), 400
    
    # Construction de l'endpoint
    custom_endpoint = f"suppliers/{supplier_id}/usagebalances"
    
    result = make_api_request(custom_endpoint, session["access_token"], params=params)
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de la récupération des consommations"}), 500


@api_bp.route('/suppliers/<supplier_id>/globalbalances', methods=['GET'])
def get_global_balances(supplier_id):
    """API pour récupérer les consommations globales pour un distributeur."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    # Récupération des paramètres de requête
    start_date = request.args.get("startDate")
    end_date = request.args.get("endDate")
    zone_level = request.args.get("zoneLevel")
    
    if not start_date or not end_date or not zone_level:
        return jsonify({"error": "Paramètres 'startDate', 'endDate' et 'zoneLevel' requis"}), 400
    
    if zone_level not in ["region", "country"]:
        return jsonify({"error": "Paramètre 'zoneLevel' doit être 'region' ou 'country'"}), 400
    
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "zoneLevel": zone_level
    }
    
    # Construction de l'endpoint
    custom_endpoint = f"suppliers/{supplier_id}/globalbalances"
    
    result = make_api_request(custom_endpoint, session["access_token"], params=params)
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de la récupération des consommations globales"}), 500


@api_bp.route('/keys', methods=['GET'])
def get_distributor_key():
    """API pour récupérer la clé publique RSA du distributeur."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    # Paramètre optionnel pour l'encodage de la clé
    encoding = request.args.get("encoding")
    params = {}
    
    if encoding and encoding == "base64":
        params["encoding"] = encoding
    
    result = make_api_request("keys", session["access_token"], params=params)
    
    if result:
        return jsonify(result)
    return jsonify({"error": "Erreur lors de la récupération de la clé publique"}), 500


@api_bp.route('/keys', methods=['POST'])
def set_distributor_key():
    """API pour configurer la clé publique RSA du distributeur."""
    if "access_token" not in session:
        return jsonify(ERROR_UNAUTHORIZED), 401
    
    data = request.get_json()
    
    if not data or "key_type" not in data or "public_key_value" not in data:
        return jsonify({"error": "Les paramètres 'key_type' et 'public_key_value' sont requis"}), 400
    
    # Vérification du type de clé
    if data["key_type"] != "rsa256":
        return jsonify({"error": "Le type de clé doit être 'rsa256'"}), 400
    
    result = make_api_request("keys", session["access_token"], method="POST", data=data)
    
    if result:
        return jsonify(result), 201
    return jsonify({"error": "Erreur lors de la configuration de la clé publique"}), 500
