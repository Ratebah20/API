"""
Routes pour le testeur d'API interactif.
"""
from flask import Blueprint, request, session, jsonify, current_app
import json
import requests
from urllib.parse import urljoin

api_tester_bp = Blueprint('api_tester', __name__, url_prefix='')

@api_tester_bp.route('/api/test', methods=['POST'])
def test_api():
    """
    Endpoint pour tester les différents endpoints de l'API Orange Travel B2B.
    Reçoit les paramètres de la requête et les transmet à l'API réelle.
    """
    if "access_token" not in session:
        return jsonify({"error": "Authentification requise"}), 401
    
    data = request.get_json()
    if not data or "endpoint" not in data:
        return jsonify({"error": "Endpoint requis"}), 400
    
    # Extraction des paramètres
    endpoint = data.get("endpoint")
    http_method = data.get("method", "GET")
    params = data.get("params", {})
    payload = data.get("body")
    path_params = data.get("pathParams", {})
    
    # Construction de l'URL
    base_url = current_app.config["API_BASE_URL"]
    
    # Récupération du mapping des endpoints
    endpoints_map = current_app.config["ENDPOINTS"]
    
    # Cas spéciaux pour les endpoints avec des paramètres dans le chemin
    # Gestion des endpoints d'offres
    if endpoint == 'offers/{offer_id}' and 'offer_id' in path_params:
        endpoint = 'offers/{offer_id}'
    
    # Gestion des endpoints de personnalisation d'offres
    elif endpoint == 'offers/customize/{offer_id}' and 'offer_id' in path_params:
        endpoint = 'offers/{offer_id}'  # Correction: utiliser le même endpoint que pour les offres
    
    # Gestion des endpoints de transactions
    elif endpoint == 'transactions/{transaction_id}' and 'transaction_id' in path_params:
        endpoint = 'transactions/{transaction_id}'
        
    # Cas spéciaux pour les endpoints avec des actions
    elif 'action' in path_params:
        action = path_params.pop('action')
        if f"suppliers/{action}" in endpoints_map:
            endpoint = f"suppliers/{action}"
    
    if endpoint not in endpoints_map and endpoint not in ["countries", "currencies", "live"] and not endpoint.startswith("offers/") and not endpoint.startswith("transactions/") and not endpoint.startswith("suppliers/"):
        return jsonify({"error": f"Endpoint {endpoint} non supporté"}), 400
    
    # Construction de l'URL finale
    if endpoint in ["countries", "currencies", "live"]:
        # Pour les endpoints de base, il faut quand même utiliser le mapping s'il existe
        if endpoint in endpoints_map:
            api_endpoint = endpoints_map[endpoint]
        else:
            api_endpoint = endpoint
        print(f"Endpoint de base: {endpoint} -> {api_endpoint}")
    else:
        api_endpoint = endpoints_map[endpoint]
        print(f"Endpoint depuis mapping: {endpoint} -> {api_endpoint}")
    
    # Remplacement des paramètres d'URL
    for key, value in path_params.items():
        placeholder = f"{{{key}}}"
        if placeholder in api_endpoint:
            api_endpoint = api_endpoint.replace(placeholder, str(value))
    
    # Logs détaillés pour débuggage
    print(f"Transformé {endpoint} en {api_endpoint}")
    print(f"Base URL: {base_url}")
    
    # Construction de l'URL comme dans auth.py qui fonctionne
    url = f"{base_url}/{api_endpoint}"
    print(f"URL finale: {url}")
    
    # Construction des headers
    headers = {
        "Authorization": f"Bearer {session['access_token']}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        if http_method == "GET":
            response = requests.get(url, headers=headers, params=params, verify=False)
        elif http_method == "POST":
            response = requests.post(url, headers=headers, json=payload, verify=False)
        elif http_method == "PATCH":
            # Traitement spécial pour la personnalisation des offres
            if endpoint.startswith('offers/') and http_method == "PATCH":
                # Afficher le payload reçu pour débogage
                print(f"Payload reçu pour personnalisation d'offre: {payload}")
                
                # Vérifier et formater correctement le payload pour la personnalisation d'offre
                formatted_payload = {}
                
                # Mapper les champs de l'interface utilisateur aux champs de l'API
                if payload:
                    # Ajouter le nom personnalisé s'il est fourni
                    if "name" in payload and payload["name"]:
                        formatted_payload["name"] = payload["name"]
                    
                    # Convertir les frais de service en distributor_fees
                    has_fees = False
                    if "distributor_fees" in payload and payload["distributor_fees"]:
                        try:
                            fee_value = float(payload["distributor_fees"])
                            if fee_value > 0:
                                formatted_payload["distributor_fees"] = fee_value
                                has_fees = True
                                print(f"Frais de service convertis: {fee_value}")
                        except (ValueError, TypeError) as e:
                            print(f"Erreur lors de la conversion des frais: {e}")
                    
                    # Définir le type de frais uniquement si des frais sont définis
                    if has_fees:
                        # Vérifier si le type de devise est spécifié
                        if "currency" in payload and payload["currency"]:
                            # Ne pas inclure la devise dans le payload, ce n'est pas un paramètre attendu par l'API
                            print(f"Devise spécifiée (non envoyée à l'API): {payload['currency']}")
                        
                        # Utiliser "value" comme type de frais par défaut (montant fixe)
                        formatted_payload["distributor_fees_type"] = "value"
                    
                    # Ajouter les métadonnées si présentes
                    if "metadata" in payload:
                        formatted_payload["metadata"] = payload["metadata"]
                
                # Vérifier que le payload est valide avant de l'envoyer
                if not formatted_payload:
                    print("Aucun paramètre valide à envoyer, annulation de la requête")
                    return jsonify({
                        "statusCode": 400,
                        "statusText": "Bad Request",
                        "data": {
                            "description": "Aucun paramètre valide à envoyer. Les paramètres modifiables sont: name, distributor_fees",
                            "message": "bad request"
                        }
                    }), 400
                
                print(f"Payload final formaté pour personnalisation d'offre: {formatted_payload}")
                response = requests.patch(url, headers=headers, json=formatted_payload, verify=False)
                
                # Afficher la réponse brute pour débogage
                print(f"Réponse brute de l'API: {response.text}")
            else:
                response = requests.patch(url, headers=headers, json=payload, verify=False)
        elif http_method == "DELETE":
            response = requests.delete(url, headers=headers, verify=False)
        else:
            return jsonify({"error": f"Méthode HTTP {http_method} non supportée"}), 400
        
        # Log pour debugging
        print(f"API Test Request: {http_method} {url}")
        print(f"Headers: {headers}")
        if params:
            print(f"Params: {params}")
        if payload:
            print(f"Body: {payload}")
        
        # Tente de renvoyer le JSON, sinon renvoie le texte brut
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = {"response": response.text}
        
        return jsonify({
            "statusCode": response.status_code,
            "statusText": response.reason,
            "data": result
        })
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête API: {str(e)}")
        return jsonify({"error": f"Erreur lors de la requête: {str(e)}"}), 500
