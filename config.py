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
        "countries": "countries",
        "live": "live",
        "currencies": "currencies",
        
        # Offres
        "offers": "distributors/offers",
        
        # Transactions
        "transactions": "distributors/transactions",
        "transactions_count": "distributors/transactions/count",
        
        # Fournisseurs et services
        "suppliers": "distributors/suppliers",
        "suppliers/simstatus": "distributors/suppliers/{supplier_id}/simstatus",
        "suppliers/usagebalances": "distributors/suppliers/{supplier_id}/usagebalances",
        "suppliers/globalbalances": "distributors/suppliers/{supplier_id}/globalbalances",
        
        # Gestion des clés de sécurité
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
