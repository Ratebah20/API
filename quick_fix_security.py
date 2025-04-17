"""
Script simplifié pour corriger définitivement les traductions de la page de sécurité
"""
import os
from pathlib import Path
from make_translations import write_translation_files

# Dictionnaire spécifique pour les textes de la page de sécurité
traductions_securite = {
    # Titres principaux
    "eSIM Security and Management": "eSIM Security and Management",
    "This section explains the security aspects related to the Orange Travel B2B API, particularly the secure management of eSIMs via RSA encryption and the best practices to follow.": 
        "This section explains the security aspects related to the Orange Travel B2B API, particularly the secure management of eSIMs via RSA encryption and the best practices to follow.",
    "RSA Encryption for eSIMs": "RSA Encryption for eSIMs",
    
    # Section Pourquoi utiliser RSA
    "Why use RSA encryption?": "Why use RSA encryption?",
    "eSIM activation codes are sensitive data that must be protected. RSA encryption ensures that only the legitimate recipient (you, the distributor) can decrypt these codes with their private key.": 
        "eSIM activation codes are sensitive data that must be protected. RSA encryption ensures that only the legitimate recipient (you, the distributor) can decrypt these codes with their private key.",
    
    # Processus de configuration
    "Configuration Process": "Configuration Process",
    "Generate an RSA key pair (private and public key)": "Generate an RSA key pair (private and public key)",
    "Transmit only your public key to Orange via the API": "Transmit only your public key to Orange via the API",
    "Securely store your private key": "Securely store your private key",
    "Receive encrypted activation codes": "Receive encrypted activation codes",
    "Decrypt the codes with your private key": "Decrypt the codes with your private key",
    
    # Démo interactive
    "Interactive Demonstration": "Interactive Demonstration",
    "Generation": "Generation",
    "Transmission": "Transmission",
    "Decryption": "Decryption",
    
    # Génération
    "RSA Key Generation": "RSA Key Generation",
    "# Generate a 4096-bit RSA key pair": "# Generate a 4096-bit RSA key pair",
    "These commands generate a private key (to be kept secure) and a public key (to be shared with Orange).": 
        "These commands generate a private key (to be kept secure) and a public key (to be shared with Orange).",
    
    # Transmission
    "Public Key Transmission": "Public Key Transmission",
    "public key in PEM format": "public key in PEM format",
    "The public key is transmitted to Orange via the dedicated endpoint to be used in the encryption of future eSIM activation codes.": 
        "The public key is transmitted to Orange via the dedicated endpoint to be used in the encryption of future eSIM activation codes.",
    
    # Déchiffrement
    "Decryption of Activation Codes": "Decryption of Activation Codes",
    "# Encrypted activation code received during an eSIM transaction": "# Encrypted activation code received during an eSIM transaction",
    "# Decryption with the private key": "# Decryption with the private key",
    "When you receive an encrypted activation code, use your private key to decrypt it and obtain the clear code that can be used by the end customer.": 
        "When you receive an encrypted activation code, use your private key to decrypt it and obtain the clear code that can be used by the end customer.",
    
    # Bonnes pratiques
    "Security Best Practices": "Security Best Practices",
    "Never share": "Never share",
    "ever": "ever",
    "your RSA private key": "your RSA private key",
    "Store the private key securely (digital vault, HSM)": "Store the private key securely (digital vault, HSM)",
    "Regularly renew your RSA keys (every 6 months recommended)": "Regularly renew your RSA keys (every 6 months recommended)",
    "Always use HTTPS/TLS for communications with the API": "Always use HTTPS/TLS for communications with the API",
    "Protect decrypted activation codes in transit to end users": "Protect decrypted activation codes in transit to end users",
    "Implement logging for sensitive operations": "Implement logging for sensitive operations"
}

# Traductions en français
french_traductions = {key: key for key in traductions_securite}

# Créer un dictionnaire complet
all_translations = {}

# Ajouter toutes les traductions (français -> anglais)
for fr, en in zip(french_traductions.values(), traductions_securite.values()):
    all_translations[fr] = en

# Écrire les traductions
print("Mise à jour des traductions...")
write_translation_files(all_translations)

print("Traductions mises à jour. Redémarrez le serveur Flask.")
