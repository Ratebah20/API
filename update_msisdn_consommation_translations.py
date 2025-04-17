"""
Script pour mettre à jour les fichiers de traduction avec les nouveaux textes des sections MSISDN et Consommation
"""
import os
from complet_translations import traductions_completes, write_translation_files

# Ajout des nouvelles traductions MSISDN et Consommation
nouvelles_traductions = {
    # Écran MSISDN
    "Récupération des informations MSISDN": "Retrieving MSISDN information",
    "Numéro de téléphone associé": "Associated phone number",
    "MSISDN: Numéro d'abonné mobile international": "MSISDN: Mobile Subscriber ISDN Number",
    "Format local": "Local format",
    "Opérateur d'attribution": "Allocation operator",
    "Type de numéro": "Number type",
    "Mobile": "Mobile",
    "Ce numéro est associé à votre eSIM mais n'est pas utilisable pour les appels vocaux ou SMS avec ce forfait data uniquement.": "This number is associated with your eSIM but cannot be used for voice calls or SMS with this data-only plan.",
    
    # Écran Consommation
    "Consultation du solde et de la consommation": "Balance and usage information",
    "Expire dans:": "Expires in:",
    "jours": "days",
    "Rafraîchir": "Refresh",
    "Données utilisées": "Data used",
    "restant": "remaining",
    "Historique de consommation": "Usage history",
    "Aujourd'hui": "Today",
    "Hier": "Yesterday",
    "Télécharger le rapport complet": "Download complete report",
    
    # Compatibilité appareils
    "iPhone (XR et +)": "iPhone (XR and later)",
    "Samsung (S20 et +)": "Samsung (S20 and later)",
    "Google Pixel": "Google Pixel",
    "iPad (Pro, Air)": "iPad (Pro, Air)"
}

# Fusionner les traductions existantes avec les nouvelles
traductions_completes.update(nouvelles_traductions)

# Écrire les traductions mises à jour
print("Mise à jour des fichiers de traduction pour MSISDN et Consommation...")
write_translation_files(traductions_completes)

print("Traductions mises à jour et compilées.")
print("Redémarrez votre serveur Flask pour appliquer les changements.")
