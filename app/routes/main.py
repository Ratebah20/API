"""
Routes principales pour l'application web.
"""
from flask import Blueprint, render_template, session, redirect, request, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/change-language/<lang>')
def change_language(lang):
    """Change la langue de l'interface utilisateur."""
    if lang in ['fr', 'en']:
        session['language'] = lang
    # Rediriger vers la page d'où vient la requête ou à la page d'accueil
    return redirect(request.referrer or url_for('main.index'))

@main_bp.route('/')
def index():
    """Page d'accueil du site."""
    return render_template('index.html', title="Orange Travel B2B API")

@main_bp.route('/guide')
def guide():
    """Guide d'intégration en 12 étapes."""
    return render_template('guide.html', title="Guide d'intégration")

@main_bp.route('/simulator')
def simulator():
    """Simulateur d'écrans mobiles."""
    return render_template('simulator.html', title="Simulateur Mobile")

@main_bp.route('/api-tester')
def api_tester():
    """Testeur d'API interactif."""
    return render_template('api_tester.html', title="Testeur d'API")

@main_bp.route('/security')
def security():
    """Page expliquant la sécurité et la gestion des eSIM."""
    return render_template('security.html', title="Sécurité et eSIM")

@main_bp.route('/api/guide/global_stats')
def global_stats():
    """Page de documentation sur les statistiques globales de consommation."""
    return render_template('global_stats.html', title="Statistiques globales de consommation")
