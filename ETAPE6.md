# Étape 6 : Gestion Sécurisée des eSIM (Security Management)

## Objectif de cette étape

Cette étape explique comment sécuriser techniquement les transactions eSIM en utilisant un chiffrement RSA afin de protéger les données sensibles telles que les codes d’activation.

## Pourquoi sécuriser les transactions eSIM ?

La sécurisation des transactions eSIM est essentielle pour :

- Protéger le code d’activation de l’eSIM contre toute interception ou utilisation frauduleuse.
- Assurer une confidentialité maximale des données sensibles lors des échanges avec Orange.

## Génération et Gestion des Clés RSA

Le distributeur doit générer une paire de clés RSA pour sécuriser les informations sensibles échangées avec Orange :

### 1. Génération des clés RSA

**Commande OpenSSL :**

```bash
openssl genrsa -out distributor_private.pem 4096
openssl rsa -in distributor_private.pem -pubout -out distributor_public.pem
```

- `distributor_private.pem` : clé privée à garder confidentielle.
- `distributor_public.pem` : clé publique à transmettre à Orange.

### 2. Transmission de la clé publique à Orange

Transmettez la clé publique via l'API :

```json
POST /distributors/keys
{
  "public_key": "votre clé publique RSA"
}
```

- Une seule clé publique autorisée par distributeur à la fois.
- Toute nouvelle clé remplace définitivement la précédente (pas de retour arrière).

## Chiffrement et Déchiffrement des Codes d’Activation

- Orange chiffre les codes d’activation des eSIM avec votre clé publique.
- Vous déchiffrez ces codes uniquement avec votre clé privée.

### Exemple de Déchiffrement (Python)

```python
def decryptRSA(text_base64, private_key):
    text_bytes = base64.b64decode(text_base64)
    text_clear_bytes = private_key.decrypt(
        text_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return text_clear_bytes.decode('utf-8')
```

## Bonnes Pratiques

- Stockez votre clé privée dans un environnement sécurisé.
- Renouvelez régulièrement vos clés pour maintenir une sécurité optimale.
- Remplacez immédiatement votre clé si vous suspectez une compromission.

Cette étape assure une sécurité robuste dans la gestion des transactions eSIM, essentielle pour protéger vos clients et votre entreprise.