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
    
    # Cas spéciaux pour les endpoints avec des actions
    if 'action' in path_params:
        action = path_params.pop('action')
        if f"suppliers/{action}" in endpoints_map:
            endpoint = f"suppliers/{action}"
    
    if endpoint not in endpoints_map and endpoint not in ["countries", "currencies", "live"]:
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
            response = requests.get(url, headers=headers, params=params)
        elif http_method == "POST":
            response = requests.post(url, headers=headers, json=payload)
        elif http_method == "PATCH":
            response = requests.patch(url, headers=headers, json=payload)
        elif http_method == "DELETE":
            response = requests.delete(url, headers=headers)
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
