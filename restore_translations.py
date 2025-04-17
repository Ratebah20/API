"""
Script pour restaurer le fonctionnement correct des traductions
"""
import os
import shutil
from pathlib import Path
from complet_translations import traductions_completes, write_translation_files

# Fonction pour restaurer les traductions
def restaurer_traductions():
    # Traductions spécifiques pour la page de sécurité correctement formatées
    traductions_securite = {
        # Titre principal
        "Sécurité et gestion des eSIM": "eSIM Security and Management",
        "Cette section explique les aspects de sécurité liés à l'API Orange Travel B2B, notamment la gestion sécurisée des eSIMs via le chiffrement RSA et les meilleures pratiques à suivre.": 
            "This section explains the security aspects related to the Orange Travel B2B API, particularly the secure management of eSIMs via RSA encryption and the best practices to follow.",
        
        # Section RSA
        "Chiffrement RSA pour les eSIM": "RSA Encryption for eSIMs",
        "Pourquoi utiliser le chiffrement RSA ?": "Why use RSA encryption?",
        "Les codes d'activation des eSIMs sont des données sensibles qui doivent être protégées. Le chiffrement RSA assure que seul le destinataire légitime (vous, le distributeur) peut déchiffrer ces codes avec sa clé privée.": 
            "eSIM activation codes are sensitive data that must be protected. RSA encryption ensures that only the legitimate recipient (you, the distributor) can decrypt these codes with their private key.",
        
        # Processus
        "Processus de configuration": "Configuration Process",
        "Générer une paire de clés RSA (clé privée et publique)": "Generate an RSA key pair (private and public key)",
        "Transmettre uniquement votre clé publique à Orange via l'API": "Transmit only your public key to Orange via the API",
        "Conserver en toute sécurité votre clé privée": "Securely store your private key",
        "Recevoir les codes d'activation chiffrés": "Receive encrypted activation codes",
        "Déchiffrer les codes avec votre clé privée": "Decrypt the codes with your private key",
        
        # Démo interactive
        "Démonstration interactive": "Interactive Demonstration",
        "Génération": "Generation",
        "Transmission": "Transmission",
        "Déchiffrement": "Decryption",
        
        # Génération des clés
        "Génération des clés RSA": "RSA Key Generation",
        "# Générer une paire de clés RSA de 4096 bits": "# Generate a 4096-bit RSA key pair",
        "Ces commandes génèrent une clé privée (à conserver en toute sécurité) et une clé publique (à transmettre à Orange).": 
            "These commands generate a private key (to be kept secure) and a public key (to be shared with Orange).",
        
        # Transmission
        "Transmission de la clé publique": "Public Key Transmission",
        "clé publique au format PEM": "public key in PEM format",
        "La clé publique est transmise à Orange via l'endpoint dédié pour être utilisée dans le chiffrement des futurs codes d'activation eSIM.": 
            "The public key is transmitted to Orange via the dedicated endpoint to be used in the encryption of future eSIM activation codes.",
        
        # Déchiffrement
        "Déchiffrement des codes d'activation": "Decryption of Activation Codes",
        "# Code d'activation chiffré reçu lors d'une transaction eSIM": "# Encrypted activation code received during an eSIM transaction",
        "base64_encoded_encrypted_data": "base64_encoded_encrypted_data",
        "# Déchiffrement avec la clé privée": "# Decryption with the private key",
        "Lorsque vous recevez un code d'activation chiffré, utilisez votre clé privée pour le déchiffrer et obtenir le code en clair qui pourra être utilisé par le client final.": 
            "When you receive an encrypted activation code, use your private key to decrypt it and obtain the clear code that can be used by the end customer.",
        
        # Bonnes pratiques
        "Bonnes pratiques de sécurité": "Security Best Practices",
        "Ne partagez": "Never share",
        "jamais": "ever",
        "votre clé privée RSA": "your RSA private key",
        "Stockez la clé privée de manière sécurisée (coffre-fort numérique, HSM)": "Store the private key securely (digital vault, HSM)",
        "Renouvelez régulièrement vos clés RSA (tous les 6 mois recommandé)": "Regularly renew your RSA keys (every 6 months recommended)",
        "Utilisez toujours HTTPS/TLS pour les communications avec l'API": "Always use HTTPS/TLS for communications with the API",
        "Protégez les codes d'activation déchiffrés en transit vers les utilisateurs finaux": "Protect decrypted activation codes in transit to end users",
        "Mettez en place une journalisation des opérations sensibles": "Implement logging for sensitive operations"
    }
    
    # Ajouter les traductions de sécurité dans le dictionnaire principal
    for key, value in traductions_securite.items():
        traductions_completes[key] = value
    
    # Écrire les fichiers de traduction
    print("Restauration des traductions en cours...")
    write_translation_files(traductions_completes)
    print("Traductions restaurées avec succès.")

if __name__ == "__main__":
    restaurer_traductions()
    print("Redémarrez votre serveur Flask pour appliquer les changements.")
