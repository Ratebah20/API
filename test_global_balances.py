#!/usr/bin/env python
"""
Script pour tester l'endpoint des statistiques globales de l'API Orange Travel B2B
avec différentes combinaisons de paramètres.
"""
import requests
import json
import sys
from datetime import datetime, timedelta
import urllib3

# Désactiver les avertissements SSL pour les tests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
API_BASE_URL = "https://api.orange.com/travel-b2b-sandbox/v1"
TOKEN_URL = "https://api.orange.com/oauth/v3/token"
CLIENT_ID = "8IOgBzqwzfA2PDWISBO4hKvMN1XBRaBr"
CLIENT_SECRET = "Yxt8oBhHQhf3FfEQl1L4VY3U0XSo3ARCApRIRClVfiHV"

# ID du fournisseur à tester
DEFAULT_SUPPLIER_ID = "92d376d4-0c18-4da8-9e6e-4dd173bc554e"

def get_access_token():
    """Obtenir un token d'accès OAuth 2.0"""
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    data = {
        "grant_type": "client_credentials"
    }
    
    print("Demande de token d'accès...")
    response = requests.post(
        TOKEN_URL,
        headers=headers,
        data=data,
        auth=(CLIENT_ID, CLIENT_SECRET),
        verify=False
    )
    
    if response.status_code == 200:
        token_data = response.json()
        print(f"Token obtenu avec succès (expire dans {token_data.get('expires_in')} secondes)")
        return token_data.get("access_token")
    else:
        print(f"Erreur lors de la récupération du token: {response.status_code}")
        print(f"Réponse: {response.text}")
        return None

def test_global_balances(access_token, supplier_id, start_date, end_date, zone_level):
    """
    Tester l'endpoint des statistiques globales avec les paramètres spécifiés
    
    Args:
        access_token (str): Token d'accès OAuth 2.0
        supplier_id (str): ID du fournisseur
        start_date (str): Date de début au format YYYY-MM-DD
        end_date (str): Date de fin au format YYYY-MM-DD
        zone_level (str): Niveau de zone (region ou country)
    """
    endpoint = f"distributors/suppliers/{supplier_id}/globalbalances"
    url = f"{API_BASE_URL}/{endpoint}"
    
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "zoneLevel": zone_level
    }
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }
    
    print("\n" + "="*80)
    print(f"Test avec les paramètres suivants:")
    print(f"  - Fournisseur: {supplier_id}")
    print(f"  - Date de début: {start_date}")
    print(f"  - Date de fin: {end_date}")
    print(f"  - Niveau de zone: {zone_level}")
    print(f"URL: {url}")
    print(f"Paramètres: {params}")
    print("="*80)
    
    try:
        response = requests.get(url, headers=headers, params=params, verify=False)
        
        print(f"Code de statut: {response.status_code}")
        print(f"En-têtes de réponse: {dict(response.headers)}")
        
        try:
            json_response = response.json()
            print(f"Réponse JSON: {json.dumps(json_response, indent=2, ensure_ascii=False)}")
        except json.JSONDecodeError:
            print(f"Réponse (non-JSON): {response.text}")
        
        return response.status_code == 200
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête: {str(e)}")
        return False

def run_test_suite():
    """Exécuter une série de tests avec différentes combinaisons de paramètres"""
    access_token = get_access_token()
    if not access_token:
        print("Impossible d'obtenir un token d'accès. Arrêt des tests.")
        return
    
    supplier_id = DEFAULT_SUPPLIER_ID
    
    # Liste des tests à effectuer
    tests = [
        # Test avec des dates passées (2023)
        {
            "start_date": "2023-01-01",
            "end_date": "2023-01-31",
            "zone_level": "region"
        },
        # Test avec une période très courte
        {
            "start_date": "2023-01-01",
            "end_date": "2023-01-07",
            "zone_level": "region"
        },
        # Test avec le niveau de zone "country"
        {
            "start_date": "2023-01-01",
            "end_date": "2023-01-31",
            "zone_level": "country"
        },
        # Test avec des dates récentes (2024)
        {
            "start_date": "2024-01-01",
            "end_date": "2024-01-31",
            "zone_level": "region"
        },
        # Test avec des dates futures (2025)
        {
            "start_date": "2025-01-01",
            "end_date": "2025-01-31",
            "zone_level": "region"
        },
        # Test avec une période de 3 mois
        {
            "start_date": "2023-01-01",
            "end_date": "2023-03-31",
            "zone_level": "region"
        }
    ]
    
    successful_tests = 0
    
    for i, test in enumerate(tests):
        print(f"\nTest {i+1}/{len(tests)}")
        success = test_global_balances(
            access_token,
            supplier_id,
            test["start_date"],
            test["end_date"],
            test["zone_level"]
        )
        
        if success:
            successful_tests += 1
    
    print(f"\nRésumé: {successful_tests}/{len(tests)} tests réussis")

def interactive_mode():
    """Mode interactif pour tester des paramètres personnalisés"""
    access_token = get_access_token()
    if not access_token:
        print("Impossible d'obtenir un token d'accès. Arrêt du programme.")
        return
    
    while True:
        print("\n" + "="*50)
        print("Mode interactif - Testeur d'API Global Balances")
        print("="*50)
        
        supplier_id = input(f"ID du fournisseur [{DEFAULT_SUPPLIER_ID}]: ") or DEFAULT_SUPPLIER_ID
        
        # Date de début
        default_start = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        start_date = input(f"Date de début (YYYY-MM-DD) [{default_start}]: ") or default_start
        
        # Date de fin
        default_end = datetime.now().strftime("%Y-%m-%d")
        end_date = input(f"Date de fin (YYYY-MM-DD) [{default_end}]: ") or default_end
        
        # Niveau de zone
        zone_level = input("Niveau de zone (region/country) [region]: ") or "region"
        
        test_global_balances(access_token, supplier_id, start_date, end_date, zone_level)
        
        if input("\nContinuer avec d'autres paramètres? (o/n) [o]: ").lower() not in ["o", "oui", ""]:
            break

if __name__ == "__main__":
    print("Testeur d'API Orange Travel B2B - Statistiques Globales")
    print("="*60)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode()
    else:
        print("Exécution de la suite de tests automatique...")
        print("Pour le mode interactif, utilisez: python test_global_balances.py --interactive")
        run_test_suite()
