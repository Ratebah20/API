"""
Script pour corriger spécifiquement les problèmes de traduction dans les onglets de la page de sécurité
"""
import os
import re
from pathlib import Path
from complet_translations import traductions_completes, write_translation_files

# Ajout des corrections spécifiques pour les onglets Transmission et Déchiffrement
corrections_specifiques = {
    # Section titres principaux
    "RSA Key Generation": "RSA Key Generation",
    "Public Key Transmission": "Public Key Transmission",
    "Decryption of Activation Codes": "Decryption of Activation Codes",
    
    # Chaînes françaises visibles dans la capture d'écran en mode anglais
    "Lorsque vous recevez un code d'activation chiffré, utilisez votre clé privée pour le déchiffrer et obtenir le code en clair qui pourra être utilisé par le client final.": 
        "When you receive an encrypted activation code, use your private key to decrypt it and obtain the clear code that can be used by the end customer.",
    
    # Valeurs spécifiques dans les onglets
    "clé publique au format PEM": "public key in PEM format",
    "Génération": "Generation",
    "Transmission": "Transmission",
    "Déchiffrement": "Decryption",
    
    # Sections du processus de configuration
    "Why use RSA encryption?": "Why use RSA encryption?",
    "Configuration Process": "Configuration Process",
    "Interactive Demonstration": "Interactive Demonstration",
    "Security Best Practices": "Security Best Practices",
    
    # Éléments du processus de configuration
    "Generate an RSA key pair (private and public key)": "Generate an RSA key pair (private and public key)",
    "Transmit only your public key to Orange via the API": "Transmit only your public key to Orange via the API",
    "Securely store your private key": "Securely store your private key",
    "Receive encrypted activation codes": "Receive encrypted activation codes",
    "Decrypt the codes with your private key": "Decrypt the codes with your private key",
    
    # Never share EVER
    "Never share": "Never share",
    "ever": "ever",
    "your RSA private key": "your RSA private key"
}

# Fusionner les traductions existantes avec les corrections spécifiques
traductions_completes.update(corrections_specifiques)

# Mettre à jour les fichiers de traduction
print("Application des corrections spécifiques pour les onglets Transmission et Déchiffrement...")
write_translation_files(traductions_completes)

print("Corrections appliquées.")
print("Redémarrez votre serveur Flask pour voir les changements.")

# Fonction optionnelle pour vérifier les traductions françaises dans l'interface anglaise
def verifier_sections_non_traduites():
    templates_dir = Path("app/templates")
    security_html = templates_dir / "security.html"
    
    if security_html.exists():
        content = security_html.read_text(encoding='utf-8')
        
        # Liste de phrases françaises communes à rechercher
        phrases_fr = [
            "Lorsque vous recevez",
            "clé publique",
            "clé privée",
            "Déchiffrement",
            "Génération",
            "Transmission"
        ]
        
        print("\nVérification des phrases françaises dans security.html:")
        for phrase in phrases_fr:
            # Chercher les cas où la phrase française n'est pas dans une balise de traduction
            matches = re.findall(f'[^_\\("]{phrase}', content)
            if matches:
                print(f"⚠️ Texte potentiellement non traduit: '{phrase}' trouvé {len(matches)} fois")
            else:
                print(f"✓ '{phrase}' correctement balisé pour la traduction")

# Exécuter la vérification
verifier_sections_non_traduites()
