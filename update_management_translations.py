"""
Script pour mettre à jour les fichiers de traduction avec les nouveaux textes du flux de gestion
"""
import os
from make_translations import translations, write_translation_files

# Ajout des nouvelles traductions du flux de gestion
new_translations = {
    # Profil eSIM
    "Profil eSIM": "eSIM Profile",
    "eSIM active": "Active eSIM",
    "Plan:": "Plan:",
    "Data 5GB": "Data 5GB",
    "Validité:": "Validity:",
    "5 jours restants": "5 days remaining",
    "ICCID:": "ICCID:",
    "Gérer cette eSIM": "Manage this eSIM",
    
    # Gestion eSIM
    "Gestion de l'eSIM": "eSIM Management", 
    "Actif": "Active",
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
    "Data uniquement": "Data only",
    "Réseaux:": "Networks:",
    "Compatibilité": "Compatibility",
    "Cette eSIM est compatible avec les appareils suivants:": "This eSIM is compatible with the following devices:",
    
    # Autres traductions à ajouter
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
    "Validité:": "Validity:",
    "Expire le:": "Expires on:",
    "Dernière mise à jour:": "Last updated:"
}

# Fusionner les traductions existantes avec les nouvelles
translations.update(new_translations)

# Écrire les traductions mises à jour
print("Mise à jour des fichiers de traduction...")
write_translation_files(translations)

print("Traductions mises à jour et compilées.")
print("Redémarrez votre serveur Flask pour appliquer les changements.")
