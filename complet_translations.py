"""
Script pour mettre à jour tous les fichiers de traduction avec l'ensemble complet des textes
"""
import os
from make_translations import write_translation_files

# Dictionnaire complet des traductions
traductions_completes = {
    # Textes généraux
    "Simulateur d'écrans mobiles": "Mobile Screen Simulator",
    "Ce simulateur vous permet de visualiser l'expérience utilisateur sur mobile pour les différentes fonctionnalités de l'API Orange Travel B2B. Choisissez un scénario pour voir la simulation.": "This simulator allows you to visualize the mobile user experience for the various features of the Orange Travel B2B API. Choose a scenario to see the simulation.",
    "Scénarios disponibles": "Available scenarios",
    "Achat et activation d'eSIM": "eSIM Purchase and Activation",
    "Gestion de l'eSIM": "eSIM Management",
    "Endpoint API": "API Endpoint",
    
    # Textes flux d'achat
    "Connectivité internationale": "International connectivity",
    "Bienvenue": "Welcome",
    "Accédez à internet partout dans le monde avec nos solutions eSIM": "Access the internet anywhere in the world with our eSIM solutions",
    "Commencer": "Start",
    "Lancement de l'application": "Application launch",
    "Authentification en cours...": "Authentication in progress...",
    "Authentification avec les identifiants du distributeur": "Authentication with distributor credentials",
    "Continuer": "Continue",
    "Appel API pour l'authentification": "API call for authentication",
    "Choisissez votre destination": "Choose your destination",
    "Récupération des destinations disponibles": "Retrieving available destinations",
    
    # Pays et destinations
    "France": "France",
    "Espagne": "Spain",
    "Italie": "Italy",
    "Allemagne": "Germany",
    
    # Sélection pays et offres
    "Filtrage des offres disponibles pour l'Espagne": "Filtering offers available for Spain",
    "Offres disponibles": "Available offers",
    "Espagne Data 5GB": "Spain Data 5GB",
    "Espagne Data 10GB": "Spain Data 10GB",
    "7 jours - Data: 5GB - Validité: 7 jours": "7 days - Data: 5GB - Validity: 7 days",
    "14 jours - Data: 10GB - Validité: 14 jours": "14 days - Data: 10GB - Validity: 14 days",
    "Détails de l'offre": "Offer details",
    "Récupération des détails de l'offre": "Retrieving offer details",
    "Prix:": "Price:",
    "Données:": "Data:",
    "Validité:": "Validity:",
    "7 jours": "7 days",
    "Couverture:": "Coverage:",
    "Type:": "Type:",
    "Data uniquement": "Data only",
    "Acheter": "Buy",
    
    # Transaction et activation
    "Achat en cours": "Purchase in progress",
    "Création d'une transaction": "Creating a transaction",
    "Achat effectué avec succès": "Purchase successfully completed",
    "Transaction ID:": "Transaction ID:",
    "eSIM profil crypté reçu": "Encrypted eSIM profile received",
    "Déchiffrer le profil eSIM": "Decrypt eSIM profile",
    "Déchiffrement": "Decryption",
    "Opération de déchiffrement": "Decryption operation",
    "Utilisation de la clé privée": "Using the private key",
    "Déchiffrement en cours...": "Decryption in progress...",
    "---- BEGIN eSIM PROFILE ----": "---- BEGIN eSIM PROFILE ----",
    "ICCID:": "ICCID:",
    "---- END eSIM PROFILE ----": "---- END eSIM PROFILE ----",
    "Installer le profil eSIM": "Install eSIM profile",
    "Installation": "Installation",
    "Redirection système": "System redirection",
    "Installation via paramètres du téléphone": "Installation via phone settings",
    "Paramètres système": "System settings",
    "Voulez-vous installer ce profil eSIM ?": "Do you want to install this eSIM profile?",
    "Annuler": "Cancel",
    "Installer": "Install",
    "L'installation de l'eSIM nécessite une redirection vers les paramètres système": "eSIM installation requires redirection to system settings",
    "Activation": "Activation",
    "Activation système": "System activation",
    "Activation du profil eSIM": "Activating eSIM profile",
    "eSIM activée avec succès": "eSIM successfully activated",
    "Votre eSIM est maintenant prête à être utilisée": "Your eSIM is now ready to use",
    "Nom:": "Name:",
    "État:": "Status:",
    "Actif": "Active",
    "Gérer mon eSIM": "Manage my eSIM",
    
    # Textes flux de gestion
    "Profil eSIM": "eSIM Profile",
    "eSIM active": "Active eSIM",
    "Plan:": "Plan:",
    "Data 5GB": "Data 5GB",
    "5 jours restants": "5 days remaining",
    "Gérer cette eSIM": "Manage this eSIM",
    
    # Gestion eSIM
    "Gestion de l'eSIM": "eSIM Management", 
    "Informations fournisseur": "Supplier Information",
    "Type d'eSIM": "eSIM Type",
    "MSISDN (numéro)": "MSISDN (number)",
    "Solde et consommation": "Balance and Usage",
    
    # Informations fournisseur
    "Fournisseur": "Supplier",
    "Informations sur le fournisseur de l'eSIM": "Information about the eSIM supplier",
    "Orange Spain": "Orange Spain",
    "ID Fournisseur": "Supplier ID",
    "Pays d'opération": "Operating Country",
    "Type de réseau": "Network Type",
    "4G/5G": "4G/5G",
    "Support technique": "Technical Support",
    
    # Type d'eSIM
    "Caractéristiques techniques": "Technical Specifications",
    "Type de profil:": "Profile Type:",
    "Consommateur": "Consumer",
    "Version:": "Version:",
    "Capacité:": "Capacity:",
    "Réseaux:": "Networks:",
    "Compatibilité": "Compatibility",
    "Cette eSIM est compatible avec les appareils suivants:": "This eSIM is compatible with the following devices:",
    
    # Autres traductions 
    "iPhone 12 et +": "iPhone 12 and later",
    "Samsung Galaxy S21 et +": "Samsung Galaxy S21 and later",
    "Google Pixel 6 et +": "Google Pixel 6 and later",
    "Numéro associé": "Associated Number",
    "Ce profil eSIM a le numéro téléphonique suivant:": "This eSIM profile has the following phone number:",
    "Non disponible": "Not available",
    "Certaines eSIM de type données uniquement n'ont pas de numéro associé.": "Some data-only eSIMs do not have an associated number.",
    "Consommation": "Usage",
    "Données utilisées:": "Data used:",
    "sur": "of",
    "Temps restant:": "Time remaining:",
    "Expire le:": "Expires on:",
    "Dernière mise à jour:": "Last updated:",
    
    # Textes API
    "Manipulation côté client": "Client-side processing",
    "Aucun appel API à cette étape": "No API call at this step",
    "Récupération des offres disponibles, filtrées par pays.": "Retrieving available offers, filtered by country.",
    "Aucun appel API, filtrage des données déjà reçues.": "No API call, filtering data already received.",
    "Récupération des détails de l'offre sélectionnée.": "Retrieving selected offer details.",
    "Création d'une transaction pour obtenir une eSIM.": "Creating a transaction to obtain an eSIM.",
    "Déchiffrement du code d'activation à l'aide de la clé privée du distributeur.": "Decryption of activation code using the distributor's private key.",
    "Redirection vers les paramètres du téléphone pour installer le profil eSIM.": "Redirecting to phone settings to install the eSIM profile.",
    "Activation du profil eSIM installé sur l'appareil.": "Activating the eSIM profile installed on the device.",
    "Affichage des détails de l'eSIM": "Displaying eSIM details",
    "Informations sur le profil eSIM déjà installé.": "Information about the already installed eSIM profile.",
    "Navigation interne": "Internal navigation", 
    "Accès à la section de gestion des eSIM.": "Access to the eSIM management section.",
    "Récupération des informations sur le fournisseur de l'eSIM.": "Retrieving information about the eSIM supplier.",
    "Affichage des propriétés": "Displaying properties",
    "Affichage des caractéristiques spécifiques de l'eSIM.": "Displaying specific characteristics of the eSIM.",
    "Récupération du numéro MSISDN associé à l'eSIM, si disponible.": "Retrieving the MSISDN number associated with the eSIM, if available.",
    "Récupération des informations de consommation pour l'eSIM.": "Retrieving usage information for the eSIM.",
    "Initialisation de l'application.": "Application initialization.",
    "Authentification et obtention du token d'accès.": "Authentication and obtaining access token."
}

# Écrire les traductions mises à jour
print("Génération des fichiers de traduction complets...")
write_translation_files(traductions_completes)

print("Fichiers de traduction complétés et compilés.")
print("Redémarrez votre serveur Flask pour appliquer les changements.")
