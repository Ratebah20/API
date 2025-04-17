"""
Script pour compiler les fichiers de traduction (version améliorée)
"""
import os
import json
import shutil

# Assurez-vous que les répertoires existent
os.makedirs('translations/fr/LC_MESSAGES', exist_ok=True)
os.makedirs('translations/en/LC_MESSAGES', exist_ok=True)

# Dictionnaire de traductions
translations = {
    # Navigation
    "Accueil": "Home",
    "Documentation": "Documentation",
    "API Tester": "API Tester",
    "Simulateur": "Simulator",
    "Sécurité": "Security",
    "Changer de langue": "Change language",
    "Français": "French",
    "Anglais": "English",
    
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
    "Guide d'intégration": "Integration Guide",
    "Testeur d'API": "API Tester",
    "Simulateur Mobile": "Mobile Simulator",
    "Sécurité & eSIM": "Security & eSIM",
}

# Créer le fichier POT (template)
with open('translations/messages.pot', 'w', encoding='utf-8') as f:
    f.write("""msgid ""
msgstr ""
"Project-Id-Version: Orange Travel B2B Simulator\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: 2025-04-17 19:00+0200\\n"
"PO-Revision-Date: 2025-04-17 19:00+0200\\n"
"Last-Translator: \\n"
"Language-Team: \\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"

""")

    # Ajout des messages msgid
    for msgid in translations:
        f.write(f'\nmsgid "{msgid}"\nmsgstr ""\n')

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
    
    # Ajout des messages: pour le français, la traduction est identique à l'original
    for msgid in translations:
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
    for msgid, msgstr in translations.items():
        f.write(f'\nmsgid "{msgid}"\nmsgstr "{msgstr}"\n')

# Maintenant, nous allons compiler les fichiers .po en .mo
try:
    from babel.messages.mofile import write_mo
    from babel.messages.pofile import read_po
    
    for lang in ['fr', 'en']:
        po_file = f'translations/{lang}/LC_MESSAGES/messages.po'
        mo_file = f'translations/{lang}/LC_MESSAGES/messages.mo'
        
        if os.path.exists(po_file):
            print(f"Compilation du fichier {po_file}...")
            with open(po_file, 'rb') as po_input:
                catalog = read_po(po_input)
            
            with open(mo_file, 'wb') as mo_output:
                write_mo(mo_output, catalog)
                
            print(f"Fichier {mo_file} créé avec succès.")
        else:
            print(f"Le fichier {po_file} n'existe pas.")
    
    print("Compilation des traductions terminée.")
except ImportError:
    print("Erreur: Module babel non trouvé. Impossible de compiler les fichiers .mo")
    print("Veuillez installer Babel avec 'pip install babel'")

print("Fichiers de traduction créés et compilés.")

# Crée un fichier .htaccess pour activer la mise en cache des traductions
with open('translations/.htaccess', 'w', encoding='utf-8') as f:
    f.write("""<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType application/octet-stream "access plus 1 year"
</IfModule>
""")

print("Configuration terminée. Redémarrez votre serveur Flask pour appliquer les changements.")

# Fonction pour réutiliser le code d'écriture des fichiers de traduction
def write_translation_files(translations_dict):
    """Permet de réutiliser le code d'écriture des fichiers de traduction"""
    # Assurez-vous que les répertoires existent
    os.makedirs('translations/fr/LC_MESSAGES', exist_ok=True)
    os.makedirs('translations/en/LC_MESSAGES', exist_ok=True)
    
    # Créer le fichier POT (template)
    with open('translations/messages.pot', 'w', encoding='utf-8') as f:
        f.write("""msgid ""
msgstr ""
"Project-Id-Version: Orange Travel B2B Simulator\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: 2025-04-17 19:00+0200\\n"
"PO-Revision-Date: 2025-04-17 19:00+0200\\n"
"Last-Translator: \\n"
"Language-Team: \\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"

""")

        # Ajout des messages msgid
        for msgid in translations_dict:
            f.write(f'\nmsgid "{msgid}"\nmsgstr ""\n')

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
        
        # Ajout des messages: pour le français, la traduction est identique à l'original
        for msgid in translations_dict:
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
        for msgid, msgstr in translations_dict.items():
            f.write(f'\nmsgid "{msgid}"\nmsgstr "{msgstr}"\n')

    # Compiler les fichiers .po en .mo
    try:
        from babel.messages.mofile import write_mo
        from babel.messages.pofile import read_po
        
        for lang in ['fr', 'en']:
            po_file = f'translations/{lang}/LC_MESSAGES/messages.po'
            mo_file = f'translations/{lang}/LC_MESSAGES/messages.mo'
            
            if os.path.exists(po_file):
                print(f"Compilation du fichier {po_file}...")
                with open(po_file, 'rb') as po_input:
                    catalog = read_po(po_input)
                
                with open(mo_file, 'wb') as mo_output:
                    write_mo(mo_output, catalog)
                    
                print(f"Fichier {mo_file} créé avec succès.")
            else:
                print(f"Le fichier {po_file} n'existe pas.")
        
        print("Compilation des traductions terminée.")
    except ImportError:
        print("Erreur: Module babel non trouvé. Impossible de compiler les fichiers .mo")
        print("Veuillez installer Babel avec 'pip install babel'")
