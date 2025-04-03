# Étape 7 : Transaction eSIM

## Objectif de cette étape

Cette étape décrit précisément comment réaliser techniquement une transaction eSIM avec l'API Orange Travel B2B. L'objectif est d'automatiser entièrement le processus d'achat et d'activation des eSIM pour le client final.

## Pourquoi automatiser les transactions eSIM ?

- Faciliter et accélérer le processus d'achat et d'activation des eSIM.
- Assurer une sécurité optimale des données sensibles.
- Simplifier le suivi des transactions et la gestion des stocks.

## Déroulement d’une transaction eSIM

### 1. Création d’une transaction eSIM

Le distributeur envoie une requête API minimale contenant uniquement l'identifiant de l'offre :

**Exemple de requête :**

```json
POST /distributors/transactions
{
    "offer_id": "id_offre_esim"
}
```

### 2. Traitement et vérifications côté API

L'API effectue plusieurs vérifications importantes :

- Disponibilité d'une clé publique RSA (pour le chiffrement).
- Vérification du stock disponible (bucket).

En cas d'échec (absence de clé RSA ou stock insuffisant), une réponse explicative est immédiatement renvoyée.

### 3. Succès d’une transaction eSIM

En cas de succès :

- L'API génère les informations spécifiques de l'eSIM, dont le code d’activation.
- Le code d’activation est chiffré avec la clé publique RSA du distributeur.

**Exemple de réponse réussie :**

```json
{
    "status": "ok",
    "product_type": "eSim",
    "parameters": {
        "msisdn": "0678578522",
        "activation_code": "Me3ddE4i-S3k...",
        "pin_code": "0000",
        "puk": "71289750"
    }
}
```

### 4. Déchiffrement du code d’activation

Le distributeur déchiffre le code reçu avec sa clé privée RSA avant de l’envoyer au client final sous forme de QR code ou code manuel.

**Exemple de déchiffrement (Python) :**

```python
def decryptRSA(encoded_text, private_key):
    text_bytes = base64.b64decode(encoded_text)
    decrypted_bytes = private_key.decrypt(
        text_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_bytes.decode('utf-8')
```

## Bonnes pratiques

- Implémentez une gestion rigoureuse des réponses API.
- Assurez-vous d’une sécurité optimale du processus de déchiffrement.
- Gérez efficacement le stock pour éviter des refus inutiles.

Cette étape garantit un processus sécurisé, rapide et efficace pour distribuer et activer les eSIM auprès des clients finaux.

