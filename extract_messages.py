"""
Script pour extraire les messages à traduire des templates et générer les fichiers de traduction.
"""
import os
import json

# Liste des messages à traduire
messages = {
    # Messages pour le simulateur
    "Simulateur d'écrans mobiles": "Mobile Screen Simulator",
    "Ce simulateur vous permet de visualiser l'expérience utilisateur sur mobile pour les différentes fonctionnalités de l'API Orange Travel B2B. Choisissez un scénario pour voir la simulation.": 
        "This simulator allows you to visualize the mobile user experience for the various features of the Orange Travel B2B API. Choose a scenario to see the simulation.",
    "Scénarios disponibles": "Available scenarios",
    "Achat et activation d'eSIM": "eSIM purchase and activation",
    "Gestion de l'eSIM": "eSIM management",
    "Navigation": "Navigation",
    "Étape précédente": "Previous step",
    "Étape suivante": "Next step",
    "Simulation de l'écran mobile": "Mobile screen simulation",
    "Détails de l'interaction": "Interaction details",
    
    # Messages pour le flux d'achat
    "Bienvenue dans l'application": "Welcome to the application",
    "Pour démarrer, appuyez sur le bouton ci-dessous": "To get started, press the button below",
    "Démarrer": "Start",
    "Accès Travel eSIM": "Travel eSIM Access",
    "Sélection du pays": "Country selection",
    "Sélection de l'offre": "Offer selection",
    "Réception de l'eSIM": "eSIM reception",
    "Déchiffrement de l'eSIM": "eSIM decryption",
    "Installation de l'eSIM": "eSIM installation",
    "Activation de l'eSIM": "eSIM activation",
    
    # Messages pour le flux de gestion
    "Réception du profil": "Profile reception",
    "Mon eSIM": "My eSIM",
    "Informations fournisseur": "Supplier information",
    "Type d'eSIM": "eSIM type",
    "Information MSISDN": "MSISDN information",
    "Solde d'utilisation": "Usage balance",
    
    # Messages généraux
    "Changer de langue": "Change language",
    "Français": "French",
    "Anglais": "English",
    "Accueil": "Home",
    "Documentation": "Documentation",
    "Simulateur": "Simulator",
    "API Tester": "API Tester",
    "Sécurité": "Security",
}

# Création du répertoire pour les traductions françaises
os.makedirs('translations/fr/LC_MESSAGES', exist_ok=True)
# Création du répertoire pour les traductions anglaises
os.makedirs('translations/en/LC_MESSAGES', exist_ok=True)

# Création du fichier de traduction français (messages.po)
with open('translations/fr/LC_MESSAGES/messages.po', 'w', encoding='utf-8') as f:
    f.write("""msgid ""
msgstr ""
"Project-Id-Version: Orange Travel B2B Simulator\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: 2025-04-17 19:00+0200\\n"
"PO-Revision-Date: 2025-04-17 19:00+0200\\n"
"Last-Translator: \\n"
"Language-Team: French\\n"
"Language: fr\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=(n > 1);\\n"

""")
    
    # Ajout des messages
    for msgid in messages:
        f.write(f'\nmsgid "{msgid}"\nmsgstr "{msgid}"\n')

# Création du fichier de traduction anglais (messages.po)
with open('translations/en/LC_MESSAGES/messages.po', 'w', encoding='utf-8') as f:
    f.write("""msgid ""
msgstr ""
"Project-Id-Version: Orange Travel B2B Simulator\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: 2025-04-17 19:00+0200\\n"
"PO-Revision-Date: 2025-04-17 19:00+0200\\n"
"Last-Translator: \\n"
"Language-Team: English\\n"
"Language: en\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\\n"

""")
    
    # Ajout des messages avec traductions
    for msgid, msgstr in messages.items():
        f.write(f'\nmsgid "{msgid}"\nmsgstr "{msgstr}"\n')

print("Fichiers de traduction créés avec succès dans le dossier 'translations'.")
