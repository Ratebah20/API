from flask import Flask, request, session, redirect, url_for
import requests
import urllib3
import json
import base64

urllib3.disable_warnings()

app = Flask(__name__)
app.secret_key = "secret_key_123"

# Configuration
CLIENT_ID = "8IOgBzqwzfA2PDWISBO4hKvMN1XBRaBr"
CLIENT_SECRET = "Yxt8oBhHQhf3FfEQl1L4VY3U0XSo3ARCApRIRClVfiHV"
TOKEN_URL = "https://api.orange.com/oauth/v3/token"
API_BASE_URL = "https://api.orange.com/travel-b2b-sandbox/v1"

# Mapping des endpoints
ENDPOINTS = {
    "countries": "countries",
    "live": "live",
    "currencies": "currencies",
    "offers": "distributors/offers",
    "transactions": "distributors/transactions",
    "suppliers": "distributors/suppliers",
}


@app.route("/")
def index():
    return """
        <h1>Orange Travel B2B API Test</h1>
        <a href="/test_auth">1. Tester l'authentification</a><br>
        <a href="/test_api/countries">2. Liste des pays</a><br>
        <a href="/test_api/live">3. Live</a><br>
        <a href="/test_api/currencies">4. Currencies</a><br>
        <a href="/test_api/offers">5. List of Offers</a><br>
        <a href="/test_api/transactions">6. List of transactions</a><br>
        <a href="/test_api/suppliers">7. List of suppliers</a><br>

    """


def get_oauth_token():
    try:
        credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
        auth_header = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

        headers = {
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }

        data = {"grant_type": "client_credentials"}

        response = requests.post(TOKEN_URL, headers=headers, data=data, verify=False)

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Erreur token: {str(e)}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Détails: {e.response.text}")
        return None


def make_api_request(endpoint, access_token, params=None):
    """Fait une requête à l'API avec le token"""
    full_url = f"{API_BASE_URL}/{ENDPOINTS[endpoint]}"
    headers = {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}

    print(f"Calling API: {full_url}")
    print(f"Headers: {headers}")
    if params:
        print(f"Params: {params}")

    try:
        response = requests.get(full_url, headers=headers, params=params, verify=False)

        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur API: {str(e)}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Détails: {e.response.text}")
        return None


@app.route("/test_auth")
def test_auth():
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


@app.route("/test_api/<endpoint>")
def test_api(endpoint):
    if "access_token" not in session:
        return redirect(url_for("test_auth"))

    if endpoint not in ENDPOINTS:
        return "Endpoint non valide", 400

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
        return f"""
            <h2>Réponse API - {endpoint}</h2>
            <pre>{json.dumps(result, indent=2)}</pre>
            <a href="/">Retour au menu</a>
        """
    return f"""
        <h2>Erreur API - {endpoint}</h2>
        <p>Vérifiez les logs du serveur pour plus de détails</p>
        <a href="/">Retour au menu</a>
    """


@app.route("/clear")
def clear_session():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    if CLIENT_ID == "votre_client_id" or CLIENT_SECRET == "votre_client_secret":
        print("⚠️ Configurez CLIENT_ID et CLIENT_SECRET")

    print(f"API Base URL: {API_BASE_URL}")
    app.run(debug=True, port=8000)
