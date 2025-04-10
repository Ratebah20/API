#!/usr/bin/env python
"""
Script pour déchiffrer un code d'activation eSIM avec une clé privée RSA.
"""
import base64
import argparse
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

def decrypt_activation_code(encrypted_code, private_key_path, password=None):
    """
    Déchiffre un code d'activation eSIM à l'aide d'une clé privée RSA.
    
    Args:
        encrypted_code (str): Le code d'activation chiffré en base64
        private_key_path (str): Chemin vers le fichier de clé privée PEM
        password (bytes, optional): Mot de passe de la clé privée si elle est protégée
        
    Returns:
        str: Le code d'activation déchiffré
    """
    try:
        # Décoder le code chiffré de base64
        encrypted_data = base64.b64decode(encrypted_code)
        
        # Charger la clé privée
        with open(private_key_path, 'rb') as key_file:
            private_key = load_pem_private_key(
                key_file.read(),
                password=password
            )
        
        # Déchiffrer le code
        decrypted_data = private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        # Convertir en chaîne de caractères
        return decrypted_data.decode('utf-8')
    
    except Exception as e:
        print(f"Erreur lors du déchiffrement: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Déchiffrer un code d\'activation eSIM')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--code', '-c', help='Code d\'activation chiffré en base64')
    group.add_argument('--file', '-f', help='Fichier contenant le code d\'activation chiffré')
    parser.add_argument('--key', '-k', default='distributor_private.pem', 
                        help='Chemin vers la clé privée (par défaut: distributor_private.pem)')
    parser.add_argument('--password', '-p', help='Mot de passe de la clé privée (si protégée)')
    
    args = parser.parse_args()
    
    # Lire le code chiffré depuis un fichier si spécifié
    if args.file:
        try:
            with open(args.file, 'r') as f:
                encrypted_code = f.read().strip()
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier: {str(e)}")
            return
    else:
        encrypted_code = args.code
    
    password_bytes = args.password.encode('utf-8') if args.password else None
    
    decrypted_code = decrypt_activation_code(
        encrypted_code, 
        args.key,
        password_bytes
    )
    
    if decrypted_code:
        print("Code d'activation déchiffré avec succès:")
        print(decrypted_code)
    else:
        print("Échec du déchiffrement du code d'activation.")

if __name__ == "__main__":
    main()
