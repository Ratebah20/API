"""
Routes principales pour l'application web.
"""
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

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
