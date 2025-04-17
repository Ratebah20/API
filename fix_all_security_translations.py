"""
Script pour assurer une traduction complète et correcte de la page de sécurité
"""
import os
import re
from pathlib import Path
from complet_translations import traductions_completes, write_translation_files

# Fonction pour réparer les traductions manquantes
def reparer_traductions_securite():
    # Récupérer le contenu de la page security.html
    security_path = Path("app/templates/security.html")
    if not security_path.exists():
        print(f"ERREUR: {security_path} introuvable!")
        return
    
    content = security_path.read_text(encoding='utf-8')
    
    # Liste de tous les textes français visibles dans le template
    textes_francais = [
        # Titres principaux
        "Sécurité et gestion des eSIM",
        "Cette section explique les aspects de sécurité liés à l'API Orange Travel B2B",
        "la gestion sécurisée des eSIMs via le chiffrement RSA et les meilleures pratiques à suivre",
        "Chiffrement RSA pour les eSIM",
        "RSA Encryption for eSIMs",
        
        # Section Pourquoi utiliser RSA
        "Pourquoi utiliser le chiffrement RSA ?",
        "Why use RSA encryption?",
        "Les codes d'activation des eSIMs sont des données sensibles qui doivent être protégées",
        "Le chiffrement RSA assure que seul le destinataire légitime (vous, le distributeur) peut déchiffrer ces codes avec sa clé privée",
        
        # Processus de configuration
        "Processus de configuration",
        "Configuration Process",
        "Générer une paire de clés RSA",
        "Transmettre uniquement votre clé publique",
        "Conserver en toute sécurité votre clé privée",
        "Recevoir les codes d'activation chiffrés",
        "Déchiffrer les codes avec votre clé privée",
        
        # Démo interactive
        "Démonstration interactive",
        "Interactive Demonstration",
        "Génération",
        "Generation",
        "Transmission",
        "Déchiffrement",
        "Decryption",
        
        # Génération
        "Génération des clés RSA",
        "RSA Key Generation",
        "# Générer une paire de clés RSA de 4096 bits",
        "Ces commandes génèrent une clé privée (à conserver en toute sécurité) et une clé publique (à transmettre à Orange)",
        
        # Transmission
        "Transmission de la clé publique",
        "Public Key Transmission",
        "clé publique au format PEM",
        "La clé publique est transmise à Orange via l'endpoint dédié pour être utilisée dans le chiffrement des futurs codes d'activation eSIM",
        
        # Déchiffrement
        "Déchiffrement des codes d'activation",
        "Decryption of Activation Codes",
        "# Code d'activation chiffré reçu lors d'une transaction eSIM",
        "# Déchiffrement avec la clé privée",
        "Lorsque vous recevez un code d'activation chiffré, utilisez votre clé privée pour le déchiffrer et obtenir le code en clair qui pourra être utilisé par le client final",
        
        # Bonnes pratiques
        "Bonnes pratiques de sécurité",
        "Security Best Practices",
        "Ne partagez",
        "jamais",
        "votre clé privée RSA",
        "Stockez la clé privée de manière sécurisée",
        "Renouvelez régulièrement vos clés RSA",
        "Utilisez toujours HTTPS/TLS pour les communications avec l'API",
        "Protégez les codes d'activation déchiffrés en transit vers les utilisateurs finaux",
        "Mettez en place une journalisation des opérations sensibles"
    ]
    
    # Dictionnaire complet de traductions pour la page de sécurité
    traductions_securite = {
        # Titres principaux
        "Sécurité et gestion des eSIM": "eSIM Security and Management",
        "Cette section explique les aspects de sécurité liés à l'API Orange Travel B2B, notamment la gestion sécurisée des eSIMs via le chiffrement RSA et les meilleures pratiques à suivre.": 
            "This section explains the security aspects related to the Orange Travel B2B API, particularly the secure management of eSIMs via RSA encryption and the best practices to follow.",
        "Chiffrement RSA pour les eSIM": "RSA Encryption for eSIMs",
        
        # Section Pourquoi utiliser RSA
        "Pourquoi utiliser le chiffrement RSA ?": "Why use RSA encryption?",
        "Les codes d'activation des eSIMs sont des données sensibles qui doivent être protégées. Le chiffrement RSA assure que seul le destinataire légitime (vous, le distributeur) peut déchiffrer ces codes avec sa clé privée.": 
            "eSIM activation codes are sensitive data that must be protected. RSA encryption ensures that only the legitimate recipient (you, the distributor) can decrypt these codes with their private key.",
        
        # Processus de configuration
        "Processus de configuration": "Configuration Process",
        "Configuration Process": "Configuration Process",
        "Générer une paire de clés RSA (clé privée et publique)": "Generate an RSA key pair (private and public key)",
        "Transmettre uniquement votre clé publique à Orange via l'API": "Transmit only your public key to Orange via the API",
        "Conserver en toute sécurité votre clé privée": "Securely store your private key",
        "Recevoir les codes d'activation chiffrés": "Receive encrypted activation codes",
        "Déchiffrer les codes avec votre clé privée": "Decrypt the codes with your private key",
        
        # Pour les éléments déjà en anglais dans le template
        "Generate an RSA key pair (private and public key)": "Generate an RSA key pair (private and public key)",
        "Transmit only your public key to Orange via the API": "Transmit only your public key to Orange via the API",
        "Securely store your private key": "Securely store your private key",
        "Receive encrypted activation codes": "Receive encrypted activation codes",
        "Decrypt the codes with your private key": "Decrypt the codes with your private key",
        
        # Démo interactive
        "Démonstration interactive": "Interactive Demonstration",
        "Interactive Demonstration": "Interactive Demonstration",
        "Génération": "Generation",
        "Generation": "Generation",
        "Transmission": "Transmission",
        "Déchiffrement": "Decryption",
        "Decryption": "Decryption",
        
        # Génération
        "Génération des clés RSA": "RSA Key Generation",
        "RSA Key Generation": "RSA Key Generation",
        "# Générer une paire de clés RSA de 4096 bits": "# Generate a 4096-bit RSA key pair",
        "Ces commandes génèrent une clé privée (à conserver en toute sécurité) et une clé publique (à transmettre à Orange).": 
            "These commands generate a private key (to be kept secure) and a public key (to be shared with Orange).",
        
        # Transmission
        "Transmission de la clé publique": "Public Key Transmission",
        "Public Key Transmission": "Public Key Transmission",
        "clé publique au format PEM": "public key in PEM format",
        "La clé publique est transmise à Orange via l'endpoint dédié pour être utilisée dans le chiffrement des futurs codes d'activation eSIM.": 
            "The public key is transmitted to Orange via the dedicated endpoint to be used in the encryption of future eSIM activation codes.",
        
        # Déchiffrement
        "Déchiffrement des codes d'activation": "Decryption of Activation Codes",
        "Decryption of Activation Codes": "Decryption of Activation Codes",
        "# Code d'activation chiffré reçu lors d'une transaction eSIM": "# Encrypted activation code received during an eSIM transaction",
        "base64_encoded_encrypted_data": "base64_encoded_encrypted_data",
        "# Déchiffrement avec la clé privée": "# Decryption with the private key",
        "Lorsque vous recevez un code d'activation chiffré, utilisez votre clé privée pour le déchiffrer et obtenir le code en clair qui pourra être utilisé par le client final.": 
            "When you receive an encrypted activation code, use your private key to decrypt it and obtain the clear code that can be used by the end customer.",
        
        # Bonnes pratiques
        "Bonnes pratiques de sécurité": "Security Best Practices",
        "Security Best Practices": "Security Best Practices",
        "Ne partagez": "Never share",
        "jamais": "ever",
        "votre clé privée RSA": "your RSA private key",
        "Stockez la clé privée de manière sécurisée (coffre-fort numérique, HSM)": "Store the private key securely (digital vault, HSM)",
        "Renouvelez régulièrement vos clés RSA (tous les 6 mois recommandé)": "Regularly renew your RSA keys (every 6 months recommended)",
        "Utilisez toujours HTTPS/TLS pour les communications avec l'API": "Always use HTTPS/TLS for communications with the API",
        "Protégez les codes d'activation déchiffrés en transit vers les utilisateurs finaux": "Protect decrypted activation codes in transit to end users",
        "Mettez en place une journalisation des opérations sensibles": "Implement logging for sensitive operations"
    }
    
    # Mise à jour du dictionnaire principal de traductions
    for key, value in traductions_securite.items():
        traductions_completes[key] = value
    
    # Écrire les traductions complètes et les compiler
    print("Application des traductions complètes pour la page de sécurité...")
    write_translation_files(traductions_completes)
    
    # Vérifier que tous les textes français sont bien identifiés pour traduction
    print("\nVérification des textes français non traduits dans le template:")
    for texte in textes_francais:
        # Vérifier si le texte est entre balises de traduction
        if texte in content and f'{{{{ _("{texte}") }}}}' not in content and texte != "RSA Encryption for eSIMs" and texte != "Configuration Process" and texte != "Interactive Demonstration" and texte != "Generation" and texte != "Transmission" and texte != "Decryption" and texte != "RSA Key Generation" and texte != "Public Key Transmission" and texte != "Decryption of Activation Codes" and texte != "Security Best Practices":
            print(f"⚠️ TEXTE NON TRADUIT: '{texte}'")
        else:
            if texte not in traductions_securite and texte != "RSA Encryption for eSIMs" and texte != "Configuration Process" and texte != "Interactive Demonstration" and texte != "Generation" and texte != "Transmission" and texte != "Decryption" and texte != "RSA Key Generation" and texte != "Public Key Transmission" and texte != "Decryption of Activation Codes" and texte != "Security Best Practices":
                print(f"⚠️ TEXTE SANS TRADUCTION DANS LE DICTIONNAIRE: '{texte}'")
    
    print("\nTraductions appliquées. Veuillez redémarrer le serveur Flask.")

if __name__ == "__main__":
    reparer_traductions_securite()
