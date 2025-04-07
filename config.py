"""
Configuration du projet API Travel Orange B2B.
"""
import os
import secrets

class Config:
    """Configuration de base pour l'application Flask."""
    # Secret key pour les sessions et les tokens CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key_123'
    
    # Configuration pour l'API Orange Travel B2B
    CLIENT_ID = os.environ.get('CLIENT_ID') or "8IOgBzqwzfA2PDWISBO4hKvMN1XBRaBr"
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or "Yxt8oBhHQhf3FfEQl1L4VY3U0XSo3ARCApRIRClVfiHV"
    TOKEN_URL = "https://api.orange.com/oauth/v3/token"
    API_BASE_URL = "https://api.orange.com/travel-b2b-sandbox/v1"
    
    # Mapping des endpoints
    ENDPOINTS = {
        # Endpoints de base - documentation consultable via /guide
        # GET - Test de connexion et informations de version
        "live": "live",
        # GET - Liste des pays avec codes ISO, noms et préfixes téléphoniques
        "countries": "countries",
        # GET - Liste des devises disponibles avec taux de conversion
        "currencies": "currencies",
        
        # Offres
        # GET - Liste des offres disponibles pour le distributeur
        "offers": "distributors/offers",
        # GET - Détails d'une offre spécifique
        "offers/{offer_id}": "distributors/offers/{offer_id}",
        # PATCH - Personnaliser une offre (nom, frais, métadonnées)
        "offers/customize/{offer_id}": "distributors/offers/{offer_id}",
        
        # Transactions
        # GET - Liste des transactions avec filtres possibles
        # POST - Créer une nouvelle transaction
        "transactions": "distributors/transactions",
        # GET - Détails d'une transaction spécifique
        "transactions/{transaction_id}": "distributors/transactions/{transaction_id}",
        # GET - Nombre de transactions selon filtres
        "transactions_count": "distributors/transactions/count",
        
        # Fournisseurs et services
        # GET - Liste des fournisseurs disponibles
        "suppliers": "distributors/suppliers",
        # GET - Vérifier le statut d'une carte SIM/eSIM
        "suppliers/simstatus": "distributors/suppliers/{supplier_id}/simstatus",
        # GET - Récupérer les données de consommation
        "suppliers/usagebalances": "distributors/suppliers/{supplier_id}/usagebalances",
        # GET - Récupérer les statistiques globales
        "suppliers/globalbalances": "distributors/suppliers/{supplier_id}/globalbalances",
        
        # Gestion des clés de sécurité
        # GET - Récupérer la clé publique RSA actuelle
        # POST - Définir une nouvelle clé publique RSA
        "keys": "distributors/keys"
    }
    
    # Configuration pour la gestion des clés RSA
    RSA_KEY_SIZE = 4096
    RSA_PRIVATE_KEY_PATH = os.environ.get('RSA_PRIVATE_KEY_PATH') or 'keys/distributor_private.pem'
    RSA_PUBLIC_KEY_PATH = os.environ.get('RSA_PUBLIC_KEY_PATH') or 'keys/distributor_public.pem'


class DevelopmentConfig(Config):
    """Configuration pour l'environnement de développement."""
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Configuration pour l'environnement de test."""
    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    """Configuration pour l'environnement de production."""
    DEBUG = False
    TESTING = False
    # En production, assurez-vous de définir une SECRET_KEY sécurisée via une variable d'environnement


# Configuration par défaut à utiliser
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
