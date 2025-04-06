"""
Point d'entrée principal de l'application API Travel Orange B2B.
"""
import os
import sys

# Ajouter le répertoire actuel au path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == "__main__":
    print(f"API Base URL: {app.config['API_BASE_URL']}")
    app.run(debug=True, port=8000)
