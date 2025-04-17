import os
import json
import subprocess
from flask_babel import Babel
from babel.messages.pofile import read_po, write_po
from babel.messages.mofile import write_mo

# Dictionnaire des traductions pour l'API Tester
translations = {
    # Titres et en-têtes
    "Testeur d'API": {
        "en": "API Tester"
    },
    "Cet outil vous permet de tester directement les différents endpoints de l'API Orange Travel B2B et de visualiser les réponses de manière formatée.": {
        "en": "This tool allows you to directly test the different endpoints of the Orange Travel B2B API and view the responses in a formatted way."
    },
    "Vous devez vous authentifier avant de pouvoir tester l'API.": {
        "en": "You must authenticate before you can test the API."
    },
    "S'authentifier": {
        "en": "Authenticate"
    },
    "Sélectionner un endpoint": {
        "en": "Select an endpoint"
    },
    
    # Catégories d'endpoints
    "Informations de base": {
        "en": "Basic information"
    },
    "Gestion des offres": {
        "en": "Offer management"
    },
    "Gestion des transactions": {
        "en": "Transaction management"
    },
    "Gestion des fournisseurs et eSIM": {
        "en": "Supplier and eSIM management"
    },
    "Gestion des clés RSA": {
        "en": "RSA key management"
    },
    
    # Boutons d'endpoints
    "Test de connexion": {
        "en": "Connection test"
    },
    "Liste des pays": {
        "en": "Country list"
    },
    "Liste des devises": {
        "en": "Currency list"
    },
    "Liste des offres": {
        "en": "Offer list"
    },
    "Détails d'une offre": {
        "en": "Offer details"
    },
    "Personnaliser une offre": {
        "en": "Customize an offer"
    },
    "Liste des transactions": {
        "en": "Transaction list"
    },
    "Créer une transaction": {
        "en": "Create a transaction"
    },
    "Détails d'une transaction": {
        "en": "Transaction details"
    },
    "Nombre de transactions": {
        "en": "Transaction count"
    },
    "Liste des fournisseurs": {
        "en": "Supplier list"
    },
    "Statut d'une SIM/eSIM": {
        "en": "SIM/eSIM status"
    },
    "Consommations d'une SIM": {
        "en": "SIM usage"
    },
    "Statistiques globales": {
        "en": "Global statistics"
    },
    "Récupérer clé publique": {
        "en": "Get public key"
    },
    "Configurer clé publique": {
        "en": "Configure public key"
    },
    
    # Paramètres
    "Paramètres": {
        "en": "Parameters"
    },
    "Aucun paramètre requis pour cet endpoint.": {
        "en": "No parameters required for this endpoint."
    },
    "Guide du développeur": {
        "en": "Developer Guide"
    },
    "Cet endpoint renvoie la liste complète des offres disponibles pour le distributeur. Les offres peuvent être de différents types :": {
        "en": "This endpoint returns the complete list of offers available to the distributor. Offers can be of different types:"
    },
    "Recharges (topup)": {
        "en": "Top-ups (topup)"
    },
    "eSIM": {
        "en": "eSIM"
    },
    "Cartes SIM": {
        "en": "SIM cards"
    },
    "Crédit, données, minutes ou SMS": {
        "en": "Credit, data, minutes or SMS"
    },
    "Cartes SIM virtuelles avec différents forfaits": {
        "en": "Virtual SIM cards with different plans"
    },
    "Cartes SIM physiques": {
        "en": "Physical SIM cards"
    },
    "Utilisez la pagination pour gérer de grandes listes d'offres.": {
        "en": "Use pagination to manage large lists of offers."
    },
    
    # Labels de formulaire communs
    "Page": {
        "en": "Page"
    },
    "Nombre par page": {
        "en": "Items per page"
    },
    "ID de l'offre": {
        "en": "Offer ID"
    },
    "Nom personnalisé": {
        "en": "Custom name"
    },
    "Frais de service": {
        "en": "Service fee"
    },
    "Devise des frais": {
        "en": "Fee currency"
    },
    "Date de début": {
        "en": "Start date"
    },
    "Date de fin": {
        "en": "End date"
    },
    "Statut": {
        "en": "Status"
    },
    "Tous": {
        "en": "All"
    },
    "Créée": {
        "en": "Created"
    },
    "En attente": {
        "en": "Pending"
    },
    "Réussie": {
        "en": "Successful"
    },
    "Échouée": {
        "en": "Failed"
    },
    "Expirée": {
        "en": "Expired"
    },
    "ID de la transaction": {
        "en": "Transaction ID"
    },
    "Type de transaction": {
        "en": "Transaction type"
    },
    "ID utilisateur (optionnel)": {
        "en": "User ID (optional)"
    },
    "Numéro de téléphone (MSISDN)": {
        "en": "Phone number (MSISDN)"
    },
    "Format : 9 derniers chiffres du numéro (sans préfixe international)": {
        "en": "Format: Last 9 digits of the number (without international prefix)"
    },
    "NSCE (ID court de la SIM)": {
        "en": "NSCE (SIM short ID)"
    },
    "Utilisez le NSCE de la SIM (visible dans les détails de transaction)": {
        "en": "Use the SIM's NSCE (visible in transaction details)"
    },
    "Aucun paramètre supplémentaire n'est requis pour l'activation d'une eSIM. Les codes d'activation seront générés automatiquement et retournés dans la réponse (chiffrés).": {
        "en": "No additional parameters are required for eSIM activation. Activation codes will be automatically generated and returned in the response (encrypted)."
    },
    "ID du client": {
        "en": "Client ID"
    },
    "Prénom du client": {
        "en": "Client's first name"
    },
    "Nom du client": {
        "en": "Client's last name"
    },
    "Email du client": {
        "en": "Client's email"
    },
    "Date de naissance": {
        "en": "Birth date"
    },
    "ID du fournisseur": {
        "en": "Supplier ID"
    },
    "ICCID (optionnel)": {
        "en": "ICCID (optional)"
    },
    "Niveau de zone": {
        "en": "Zone level"
    },
    "Région": {
        "en": "Region"
    },
    "Pays": {
        "en": "Country"
    },
    "Encodage": {
        "en": "Encoding"
    },
    "Par défaut": {
        "en": "Default"
    },
    "Base64": {
        "en": "Base64"
    },
    "Type de clé": {
        "en": "Key type"
    },
    "Valeur de la clé publique": {
        "en": "Public key value"
    },
    
    # Interface et boutons
    "Exécuter la requête": {
        "en": "Execute request"
    },
    "Réponse API": {
        "en": "API Response"
    },
    "Fonctionnalités à venir": {
        "en": "Upcoming features"
    },
    "Sauvegarde des requêtes précédentes": {
        "en": "Save previous requests"
    },
    "Génération de code pour différents langages de programmation": {
        "en": "Code generation for different programming languages"
    },
    "Mode comparaison des réponses": {
        "en": "Response comparison mode"
    },
    
    # Messages et guides détaillés
    "Cet endpoint renvoie les détails complets d'une offre spécifique, notamment :": {
        "en": "This endpoint returns the complete details of a specific offer, including:"
    },
    "Informations sur le produit associé (type, couverture, validité)": {
        "en": "Information about the associated product (type, coverage, validity)"
    },
    "Prix et frais de distribution": {
        "en": "Price and distribution fees"
    },
    "Solde du bucket (pour les offres de type topup)": {
        "en": "Bucket balance (for topup offers)"
    },
    "Métadonnées spécifiques au type de produit": {
        "en": "Metadata specific to the product type"
    },
    "Ces informations sont essentielles avant de créer une transaction.": {
        "en": "This information is essential before creating a transaction."
    },
    "Cet endpoint permet de personnaliser certains paramètres d'une offre existante :": {
        "en": "This endpoint allows you to customize certain parameters of an existing offer:"
    },
    "Nom personnalisé pour l'affichage côté client": {
        "en": "Custom name for client-side display"
    },
    "Marge (markup) appliquée au prix de base": {
        "en": "Markup applied to the base price"
    },
    "Devise de la marge": {
        "en": "Markup currency"
    },
    "Métadonnées personnalisées": {
        "en": "Custom metadata"
    },
    "Cette personnalisation n'affecte pas les caractéristiques techniques du produit sous-jacent.": {
        "en": "This customization does not affect the technical characteristics of the underlying product."
    },
    "Cet endpoint renvoie l'historique des transactions avec possibilité de filtrage :": {
        "en": "This endpoint returns the transaction history with filtering options:"
    },
    "Filtrage par période (startDate, endDate)": {
        "en": "Filtering by period (startDate, endDate)"
    },
    "Filtrage par statut (created, pending, ok, ko, expired)": {
        "en": "Filtering by status (created, pending, ok, ko, expired)"
    },
    "Pagination pour gérer de grands volumes": {
        "en": "Pagination to manage large volumes"
    },
    "Les transactions peuvent concerner des recharges, des activations d'eSIM ou des cartes SIM physiques.": {
        "en": "Transactions can involve recharges, eSIM activations, or physical SIM cards."
    },
    "Cet endpoint renvoie les détails complets d'une transaction spécifique :": {
        "en": "This endpoint returns the complete details of a specific transaction:"
    },
    "Statut actuel et historique des changements": {
        "en": "Current status and change history"
    },
    "Informations sur l'offre et le produit associés": {
        "en": "Information about the associated offer and product"
    },
    "Détails de facturation et prix": {
        "en": "Billing details and prices"
    },
    "Paramètres spécifiques (MSISDN, ICCID, codes d'activation pour eSIM, etc.)": {
        "en": "Specific parameters (MSISDN, ICCID, activation codes for eSIM, etc.)"
    },
    "Pour les transactions d'eSIM, les données sensibles sont chiffrées avec la clé RSA du distributeur.": {
        "en": "For eSIM transactions, sensitive data is encrypted with the distributor's RSA key."
    },
    "Cet endpoint permet de créer une nouvelle transaction. Le type de transaction détermine les paramètres requis :": {
        "en": "This endpoint allows you to create a new transaction. The transaction type determines the required parameters:"
    },
    "Recharge Orange/Espagne": {
        "en": "Orange/Spain Top-up"
    },
    "Nécessite un MSISDN (numéro de téléphone)": {
        "en": "Requires an MSISDN (phone number)"
    },
    "Recharge Welcome Travelers": {
        "en": "Welcome Travelers Top-up"
    },
    "Nécessite le NSCE (numéro court)": {
        "en": "Requires the NSCE (short number)"
    },
    "Uniquement l'ID de l'offre est nécessaire": {
        "en": "Only the offer ID is required"
    },
    "L'ID de l'offre est toujours obligatoire et doit correspondre à une offre active.": {
        "en": "The offer ID is always mandatory and must correspond to an active offer."
    },
    "Pour les transactions eSIM, les codes d'activation retournés sont chiffrés avec la clé publique RSA du distributeur et doivent être déchiffrés avec la clé privée correspondante.": {
        "en": "For eSIM transactions, the returned activation codes are encrypted with the distributor's RSA public key and must be decrypted with the corresponding private key."
    },
    "Cet endpoint permet de compter le nombre de transactions selon différents critères :": {
        "en": "This endpoint allows you to count the number of transactions according to different criteria:"
    },
    "Comptage par période (startDate, endDate)": {
        "en": "Counting by period (startDate, endDate)"
    },
    "Comptage par statut (created, pending, ok, ko, expired)": {
        "en": "Counting by status (created, pending, ok, ko, expired)"
    },
    "Utile pour les statistiques et rapports": {
        "en": "Useful for statistics and reports"
    },
    "Cette fonction est particulièrement utile pour les tableaux de bord et les rapports d'activité.": {
        "en": "This function is particularly useful for dashboards and activity reports."
    },
    "Cet endpoint permet de créer différents types de transactions selon le type de produit associé à l'offre :": {
        "en": "This endpoint allows you to create different types of transactions depending on the type of product associated with the offer:"
    },
    "Recharge (topup)": {
        "en": "Top-up"
    },
    "Recharge de crédit, données, minutes ou SMS pour une carte SIM existante": {
        "en": "Credit, data, minutes or SMS top-up for an existing SIM card"
    },
    "Fourniture d'une carte SIM virtuelle avec un profil prédéfini": {
        "en": "Provision of a virtual SIM card with a predefined profile"
    },
    "Activation d'une carte SIM physique": {
        "en": "Activation of a physical SIM card"
    },
    "Les paramètres requis varient selon le type d'opération. Pour une recharge, le paramètre": {
        "en": "The required parameters vary according to the type of operation. For a top-up, the parameter"
    },
    "Cet endpoint renvoie la liste des fournisseurs disponibles pour le distributeur :": {
        "en": "This endpoint returns the list of suppliers available to the distributor:"
    },
    "Fournisseurs d'eSIM (opérateurs virtuels)": {
        "en": "eSIM suppliers (virtual operators)"
    },
    "Fournisseurs de recharges (opérateurs locaux)": {
        "en": "Top-up suppliers (local operators)"
    },
    "Statut de chaque fournisseur (approved, revoked, pending)": {
        "en": "Status of each supplier (approved, revoked, pending)"
    },
    "L'ID du fournisseur est nécessaire pour les opérations liées aux SIM et aux recharges.": {
        "en": "The supplier ID is necessary for operations related to SIMs and top-ups."
    },
    "Cet endpoint permet de vérifier le statut d'une carte SIM/eSIM. Les statuts possibles incluent :": {
        "en": "This endpoint allows you to check the status of a SIM/eSIM card. Possible statuses include:"
    },
    "free": {
        "en": "free"
    },
    "not installed": {
        "en": "not installed"
    },
    "available": {
        "en": "available"
    },
    "suspended": {
        "en": "suspended"
    },
    "Disponible": {
        "en": "Available"
    },
    "Non installée": {
        "en": "Not installed"
    },
    "Disponible et active": {
        "en": "Available and active"
    },
    "Suspendue (diverses raisons)": {
        "en": "Suspended (various reasons)"
    },
    "Vous pouvez identifier la SIM soit par l'ID de transaction, soit par l'ICCID directement.": {
        "en": "You can identify the SIM either by the transaction ID or directly by the ICCID."
    },
    "Cet endpoint permet de consulter les consommations et soldes restants d'une carte SIM/eSIM :": {
        "en": "This endpoint allows you to consult the consumption and remaining balances of a SIM/eSIM card:"
    },
    "Données restantes (Mo/Go)": {
        "en": "Remaining data (MB/GB)"
    },
    "Temps d'appel restant (minutes/heures)": {
        "en": "Remaining call time (minutes/hours)"
    },
    "SMS restants": {
        "en": "Remaining SMS"
    },
    "Dates d'activation et d'expiration": {
        "en": "Activation and expiration dates"
    },
    "Ces informations sont essentielles pour suivre l'utilisation et déterminer si une recharge est nécessaire.": {
        "en": "This information is essential for tracking usage and determining if a top-up is necessary."
    },
    "Cet endpoint fournit des statistiques globales de consommation pour une période donnée :": {
        "en": "This endpoint provides global consumption statistics for a given period:"
    },
    "Consommation totale par région ou pays (selon zoneLevel)": {
        "en": "Total consumption by region or country (according to zoneLevel)"
    },
    "Période maximale de 6 mois": {
        "en": "Maximum period of 6 months"
    },
    "Détails par type de consommation (data, voix, SMS)": {
        "en": "Details by consumption type (data, voice, SMS)"
    },
    "Ces statistiques sont particulièrement utiles pour analyser les tendances d'utilisation et optimiser les offres.": {
        "en": "These statistics are particularly useful for analyzing usage trends and optimizing offers."
    },
    "Cet endpoint permet de récupérer la clé publique RSA actuellement configurée :": {
        "en": "This endpoint allows you to retrieve the currently configured RSA public key:"
    },
    "Utilisée pour vérifier que la bonne clé est configurée": {
        "en": "Used to verify that the correct key is configured"
    },
    "Option d'encodage en base64 disponible": {
        "en": "Base64 encoding option available"
    },
    "Essentielle pour le système de chiffrement des données sensibles": {
        "en": "Essential for the sensitive data encryption system"
    },
    "La clé publique est utilisée par l'API pour chiffrer les données sensibles comme les codes d'activation d'eSIM.": {
        "en": "The public key is used by the API to encrypt sensitive data such as eSIM activation codes."
    },
    "Cet endpoint permet de configurer une nouvelle clé publique RSA pour le chiffrement :": {
        "en": "This endpoint allows you to configure a new RSA public key for encryption:"
    },
    "Remplace la clé précédemment configurée": {
        "en": "Replaces the previously configured key"
    },
    "Doit être au format PEM standard": {
        "en": "Must be in standard PEM format"
    },
    "La clé privée correspondante doit être conservée de manière sécurisée côté client": {
        "en": "The corresponding private key must be securely stored on the client side"
    },
    "Important": {
        "en": "Important"
    },
    "Après changement de clé, les données précédemment chiffrées ne pourront plus être déchiffrées avec la nouvelle clé privée.": {
        "en": "After changing the key, previously encrypted data can no longer be decrypted with the new private key."
    },
    
    # JavaScript textes
    "DOM chargé, initialisation du testeur API": {
        "en": "DOM loaded, initializing API tester"
    },
    "Bouton d'exécution:": {
        "en": "Execute button:"
    },
    "Zone de résultat:": {
        "en": "Result area:"
    },
    "Label de statut:": {
        "en": "Status label:"
    },
    "Le bouton d'exécution n'a pas été trouvé!": {
        "en": "The execute button was not found!"
    },
    "ID de l'offre requis": {
        "en": "Offer ID required"
    },
    "L'ID de l'offre est obligatoire": {
        "en": "The offer ID is mandatory"
    },
    "Le numéro de téléphone (MSISDN) est obligatoire pour une recharge Orange/Espagne": {
        "en": "The phone number (MSISDN) is mandatory for an Orange/Spain top-up"
    },
    "Recharge Orange/Espagne (MSISDN)": {
        "en": "Orange/Spain Top-up (MSISDN)"
    },
    "Recharge Welcome Travelers (NSCE)": {
        "en": "Welcome Travelers Top-up (NSCE)"
    },
    "Activation eSIM": {
        "en": "eSIM Activation"
    }
}

def update_existing_translation_file(filepath, new_translations, language):
    """Met à jour un fichier de traduction existant avec de nouvelles traductions."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            catalog = read_po(f)
        
        # Ajouter ou mettre à jour les messages
        for message_id, translations_dict in new_translations.items():
            if language in translations_dict:
                translation = translations_dict[language]
                if message_id in catalog:
                    # Mettre à jour un message existant
                    catalog[message_id].string = translation
                else:
                    # Ajouter un nouveau message
                    from babel.messages.catalog import Message
                    catalog[message_id] = Message(message_id, string=translation)
        
        # Enregistrer le catalogue mis à jour
        with open(filepath, 'wb') as f:
            write_po(f, catalog)
        
        return True
    except Exception as e:
        print(f"Erreur lors de la mise à jour du fichier de traduction {filepath}: {e}")
        return False

def compile_translations():
    """Compile les fichiers .po en fichiers .mo."""
    try:
        for lang in ['fr', 'en']:
            po_file_path = f"translations/{lang}/LC_MESSAGES/messages.po"
            mo_file_path = f"translations/{lang}/LC_MESSAGES/messages.mo"
            
            # Vérifier que le fichier .po existe
            if not os.path.exists(po_file_path):
                print(f"Fichier {po_file_path} introuvable.")
                continue
            
            print(f"Compilation du fichier {po_file_path}...")
            
            # Lire le fichier .po
            with open(po_file_path, 'r', encoding='utf-8') as f:
                catalog = read_po(f)
            
            # Écrire le fichier .mo
            with open(mo_file_path, 'wb') as f:
                write_mo(f, catalog)
            
            print(f"Fichier {mo_file_path} créé avec succès.")
        
        print("Compilation des traductions terminée.")
        return True
    except Exception as e:
        print(f"Erreur lors de la compilation des traductions: {e}")
        return False

def main():
    # Mettre à jour les fichiers de traduction pour l'API Tester
    print("Mise à jour des fichiers de traduction pour l'API Tester...")
    
    # Mettre à jour le fichier de traduction anglais
    en_po_file = "translations/en/LC_MESSAGES/messages.po"
    if os.path.exists(en_po_file):
        update_existing_translation_file(en_po_file, translations, 'en')
    
    # Mettre à jour le fichier de traduction français (identité)
    fr_po_file = "translations/fr/LC_MESSAGES/messages.po"
    if os.path.exists(fr_po_file):
        # Pour le français, nous utilisons les clés comme traductions (identité)
        fr_translations = {k: {"fr": k} for k in translations.keys()}
        update_existing_translation_file(fr_po_file, fr_translations, 'fr')
    
    # Compiler les traductions
    compile_translations()
    
    print("Traductions mises à jour et compilées.")
    print("Redémarrez votre serveur Flask pour appliquer les changements.")

if __name__ == "__main__":
    main()
