"""
Routes d'authentification pour l'API Orange Travel B2B.
"""
from flask import Blueprint, request, session, redirect, url_for, current_app, jsonify
import requests
import base64
import json
import urllib3

urllib3.disable_warnings()

auth_bp = Blueprint('auth', __name__)

def get_oauth_token():
    """
    Obtient un token OAuth 2.0 auprès de l'API Orange.
    
    Returns:
        dict: Le token et les informations associées ou None en cas d'erreur
    """
    try:
        client_id = current_app.config['CLIENT_ID']
        client_secret = current_app.config['CLIENT_SECRET']
        token_url = current_app.config['TOKEN_URL']
        
        credentials = f"{client_id}:{client_secret}"
        auth_header = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

        headers = {
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }

        data = {"grant_type": "client_credentials"}

        response = requests.post(token_url, headers=headers, data=data, verify=False)

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Erreur token: {str(e)}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Détails: {e.response.text}")
        return None


@auth_bp.route('/test_auth')
def test_auth():
    """
    Teste l'authentification avec l'API Orange et stocke le token en session.
    """
    result = get_oauth_token()
    if result and "access_token" in result:
        session["access_token"] = result["access_token"]
        return f"""
            <h2>Token obtenu avec succès</h2>
            <pre>{json.dumps(result, indent=2)}</pre>
            <a href="/">Retour au menu</a>
        """
    return f"""
        <h2>Erreur d'authentification</h2>
        <pre>{json.dumps(result, indent=2) if result else "Erreur inconnue"}</pre>
        <a href="/">Retour</a>
    """


@auth_bp.route('/clear')
def clear_session():
    """
    Efface la session en cours.
    """
    session.clear()
    return redirect(url_for('main.index'))


@auth_bp.route('/api/token', methods=['GET'])
def api_get_token():
    """
    Endpoint API pour obtenir un token OAuth (version JSON).
    """
    result = get_oauth_token()
    if result and "access_token" in result:
        session["access_token"] = result["access_token"]
        return jsonify(result)
    return jsonify({"error": "Erreur d'authentification"}), 401
