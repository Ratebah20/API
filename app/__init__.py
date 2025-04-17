"""
Initialisation de l'application Flask pour l'API Travel Orange B2B.
"""
from flask import Flask, request, session, g
from flask_babel import Babel, gettext as _
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
    
    # Clé secrète pour les sessions (nécessaire pour stocker les préférences de langue)
    app.secret_key = os.environ.get('SECRET_KEY', 'orange-travel-b2b-simulator-dev-key')
    # S'assurer que les sessions fonctionnent correctement
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['PERMANENT_SESSION_LIFETIME'] = 3600  # 1 heure
    
    # Configuration pour l'internationalisation
    app.config['BABEL_DEFAULT_LOCALE'] = 'fr'
    # Chemin absolu vers les traductions - normalement ce serait le répertoire relatif 'translations'
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'translations')
    print(f"[DEBUG] Translations directory: {app.config['BABEL_TRANSLATION_DIRECTORIES']}")
    
    # Vérifier que le répertoire de traductions existe
    if not os.path.exists(app.config['BABEL_TRANSLATION_DIRECTORIES']):
        print(f"[ERROR] Le répertoire de traductions n'existe pas: {app.config['BABEL_TRANSLATION_DIRECTORIES']}")
    else:
        print(f"[INFO] Répertoire de traductions trouvé: {app.config['BABEL_TRANSLATION_DIRECTORIES']}")
    
    # Initialisation de Babel
    babel = Babel(app)
    
    @babel.localeselector
    def get_locale():
        # Débogage: afficher les informations sur la session et la langue
        print(f"\n[DEBUG] Session data: {dict(session)}")
        print(f"[DEBUG] Request args: {request.args}")
        
        # Priorité 1: La langue choisie explicitement et stockée en session
        if 'language' in session:
            selected_lang = session['language']
            print(f"[DEBUG] Using language from session: {selected_lang}")
            g.lang_code = selected_lang  # Stocke la langue dans g pour l'utiliser dans les templates
            return selected_lang
            
        # Priorité 2: Le paramètre 'lang' dans l'URL
        lang = request.args.get('lang')
        if lang in ['fr', 'en']:
            # Stocker dans la session pour les requêtes futures
            session['language'] = lang
            session.permanent = True  # Rendre la session permanente
            print(f"[DEBUG] Using language from URL: {lang}")
            g.lang_code = lang
            return lang
            
        # Priorité 3: La langue préférée du navigateur si elle est disponible
        browser_lang = request.accept_languages.best_match(['fr', 'en']) or 'fr'  # Par défaut 'fr'
        print(f"[DEBUG] Using browser language: {browser_lang}")
        
        # Stocke la langue dans g pour l'utiliser dans les templates
        g.lang_code = browser_lang
        return browser_lang
        
    # Rendre g.lang_code disponible dans tous les templates
    @app.before_request
    def before_request():
        if 'language' in session:
            g.lang_code = session['language']
        else:
            g.lang_code = request.accept_languages.best_match(['fr', 'en']) or 'fr'
    
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
