"""
Script pour mettre à jour les fichiers de traduction avec les nouveaux textes
"""
import os
from make_translations import translations

# Ajout des nouvelles traductions
new_translations = {
    # Textes du flux d'achat
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
    
    # Pays
    "France": "France",
    "Espagne": "Spain",
    "Italie": "Italy",
    "Allemagne": "Germany",
    
    # Textes API
    "Manipulation côté client": "Client-side processing",
    "Aucun appel API à cette étape": "No API call at this step",
    "Récupération des offres disponibles, filtrées par pays.": "Retrieving available offers, filtered by country.",
    "Aucun appel API, filtrage des données déjà reçues.": "No API call, filtering data already received.",
    "Récupération des détails de l'offre sélectionnée.": "Retrieving selected offer details.",
    "Création d'une transaction pour obtenir une eSIM.": "Creating a transaction to obtain an eSIM.",
    "Utilisation de la clé privée": "Using the private key",
    "Déchiffrement du code d'activation à l'aide de la clé privée du distributeur.": "Decryption of activation code using the distributor's private key.",
    "Redirection système": "System redirection",
    "Redirection vers les paramètres du téléphone pour installer le profil eSIM.": "Redirecting to phone settings to install the eSIM profile.",
    "Opération système": "System operation",
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
    "Initialisation de l'application.": "Application initialization."
}

# Fusionner les traductions existantes avec les nouvelles
translations.update(new_translations)

# Écrire les traductions mises à jour
print("Mise à jour des fichiers de traduction...")
from make_translations import write_translation_files
write_translation_files(translations)

print("Traductions mises à jour et compilées.")
print("Redémarrez votre serveur Flask pour appliquer les changements.")
