"""
Initialisation de l'application Flask pour l'API Travel Orange B2B.
"""
from flask import Flask
import os
import sys

# Ajouter le dossier parent au path pour permettre les importations
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config

def create_app(config_name='default'):
    """
    Factory pattern pour créer l'application Flask avec la configuration spécifiée.
    
    Args:
        config_name (str): Nom de la configuration à utiliser ('development', 'testing', 'production')
        
    Returns:
        Flask app: L'application Flask configurée
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # S'assurer que le dossier des clés RSA existe
    os.makedirs(os.path.dirname(app.config['RSA_PRIVATE_KEY_PATH']), exist_ok=True)
    
    # Enregistrement des blueprints - à activer une fois les blueprints créés
    try:
        from .routes.auth import auth_bp
        app.register_blueprint(auth_bp)
    except ImportError:
        app.logger.warning("Blueprint auth_bp non trouvé, ignoré.")
        
    try:
        from .routes.main import main_bp
        app.register_blueprint(main_bp)
    except ImportError:
        app.logger.warning("Blueprint main_bp non trouvé, ignoré.")
        
    try:
        from .routes.api import api_bp
        app.register_blueprint(api_bp, url_prefix='/api')
    except ImportError:
        app.logger.warning("Blueprint api_bp non trouvé, ignoré.")
        
    try:
        from .routes.api_tester import api_tester_bp
        app.register_blueprint(api_tester_bp, url_prefix='')
        app.logger.info("Blueprint api_tester_bp enregistré avec succès")
    except ImportError:
        app.logger.warning("Blueprint api_tester_bp non trouvé, ignoré.")
    
    return app
