# Documentation de Référence de l'API Orange Travel B2B

## Table des matières

1. [Prérequis d'authentification](#prérequis-dauthentification)
2. [URL de base](#url-de-base)
3. [Entités gérées par l'API Travel B2B](#entités-gérées-par-lapi-travel-b2b)
4. [Personnalisation des offres](#personnalisation-des-offres)
5. [Gestion des prix](#gestion-des-prix)
6. [Gestion des recharges (Topup)](#gestion-des-recharges-topup)
7. [Gestion des eSIM](#gestion-des-esim)
8. [Gestion KYC](#gestion-kyc)
9. [Gestion des soldes d'utilisation](#gestion-des-soldes-dutilisation)
10. [Erreurs](#erreurs)

## Prérequis d'authentification

L'API Orange Travel B2B utilise OAuth 2.0 pour l'authentification. Toutes les requêtes nécessitent un jeton d'accès valide.

### Obtention du jeton d'accès

- **URL** : `https://api.orange.com/oauth/v3/token`
- **Méthode** : `POST`
- **Authentification** : Identifiants client (client_id et client_secret)
- **Scope requis** : `sekapi:manager:access:api`

### Utilisation du jeton d'accès

Le jeton d'accès doit être inclus dans l'en-tête `Authorization` de chaque requête à l'API :

```
Authorization: Bearer {access_token}
```

## URL de base

Toutes les requêtes doivent utiliser l'une des URL de base suivantes :

- **Environnement de test (sandbox)** : `https://api.orange.com/travel-b2b-sandbox/v1`
- **Environnement de production** : `https://api.orange.com/travel-b2b/v1`

## Entités gérées par l'API Travel B2B

L'API Travel B2B gère plusieurs entités principales liées aux services de télécommunications pour les voyageurs :

### Produits (Products)

Représentent les offres de télécommunications disponibles, telles que :
- Recharges (topup)
- Cartes eSIM
- Cartes SIM physiques

Chaque produit possède des caractéristiques spécifiques comme :
- Zone de couverture (pays)
- Type de produit
- Validité
- Quantité de données
- Temps d'appel
- SMS inclus

### Offres (Offers)

Représentent les produits mis à disposition par un distributeur avec :
- Prix de revente
- Frais de distribution
- Métadonnées personnalisées

### Fournisseurs (Suppliers)

Les opérateurs qui fournissent les services de télécommunications, comme :
- Orange France
- Orange Espagne
- Welcome Travelers
- Autres partenaires

### Transactions

Enregistrent les opérations commerciales :
- Recharges de crédit (topup)
- Activation d'eSIM
- Activation de SIM physique

### Endpoints de référence

- **Test de connexion** : `/live`
- **Liste des pays** : `/countries`
- **Liste des devises** : `/currencies`
- **Liste des fournisseurs** : `/distributors/suppliers`

## Personnalisation des offres

Les distributeurs peuvent personnaliser les offres pour leurs besoins spécifiques.

### Modification des paramètres d'une offre

- **URL** : `/distributors/offers/{offer_id}`
- **Méthode** : `PATCH`
- **Corps de la requête** :
  ```json
  {
    "name": "Nom personnalisé de l'offre",
    "distributor_fees": 2.5,
    "distributor_fees_type": "value",
    "metadata": "Informations personnalisées"
  }
  ```

### Liste des offres disponibles

- **URL** : `/distributors/offers`
- **Méthode** : `GET`
- **Paramètres de requête** :
  - `offset` (optionnel) : Position de départ pour la pagination
  - `limit` (optionnel) : Nombre maximum d'éléments à retourner

## Gestion des prix

L'API permet de gérer les devises et les taux de change pour adapter les prix des offres.

### Devises

- **URL** : `/currencies`
- **Méthode** : `GET`
- **Réponse** : Liste des devises avec leurs taux de change par rapport à l'euro et au dollar américain

### Informations sur le prix des offres

Chaque offre contient des informations sur son prix :
- `resell_value` : Valeur finale du produit pour le distributeur
- `distribution_fees` : Frais appliqués par le distributeur
- `distribution_fees_type` : Type de frais ("percent" ou "value")
- `reference_currency` : Devise de référence utilisée

## Gestion des recharges (Topup)

### Création d'une recharge

- **URL** : `/distributors/transactions`
- **Méthode** : `POST`
- **Corps de la requête** :

**Pour Orange France/Espagne (nécessite MSISDN)**:
```json
{
    "offer_id": "7b977bd5-c7dc-4681-bf33-c4bd2eadc266",
    "user_id": "635768534667763",
    "parameters": {
        "msisdn": "684587587"
    }
}
```

**Pour Welcome Travelers (nécessite simId)**:
```json
{
    "offer_id": "44f9d3b6-242e-47c6-b978-88d5e2e041ce",
    "parameters": {
        "simId": "1956392841179"
    }
}
```

### Vérification d'une recharge

- **URL** : `/distributors/transactions/{transaction_id}`
- **Méthode** : `GET`

### Solde d'utilisation d'une recharge

- **URL** : `/distributors/suppliers/{id}/usagebalances`
- **Méthode** : `GET`
- **Paramètres de requête** :
  - `transaction` (optionnel) : Identifiant de la transaction
  - `simId` (optionnel) : Identifiant de la SIM (pour Welcome Travelers)

## Gestion des eSIM

### Création d'une transaction eSIM

- **URL** : `/distributors/transactions`
- **Méthode** : `POST`
- **Corps de la requête** :
```json
{
    "offer_id": "07966928-d3a3-453e-9944-b7ff1081794d"
}
```

### Récupération des informations eSIM

Après la création d'une transaction eSIM, la réponse contient toutes les informations nécessaires, dont :
- `activation_code` : Code d'activation chiffré avec la clé publique RSA du distributeur
- `msisdn` : Numéro de téléphone associé
- `pin_code` : Code PIN
- `puk` : Code PUK

### Gestion des clés de chiffrement

- **URL** : `/distributors/keys`
- **Méthode** : `POST`
- **Corps de la requête** :
```json
{
    "key_type": "rsa256",
    "public_key_value": "-----BEGIN PUBLIC KEY-----\nMIIB..."
}
```

## Gestion KYC

Certains produits, notamment les eSIM, peuvent nécessiter une vérification d'identité (KYC - Know Your Customer).

### Informations KYC dans les produits

Les produits contiennent des informations sur les exigences KYC dans leurs métadonnées :
- `kyc_level` : Niveau de KYC requis pour ce produit
- `kyc_url` : URL pour la gestion KYC de ce produit

## Gestion des soldes d'utilisation

### Vérification du solde d'utilisation

- **URL** : `/distributors/suppliers/{supplier_id}/usagebalances`
- **Méthode** : `GET`
- **Paramètres de requête** :
  - `transaction` : Identifiant de la transaction (pour les eSIM obtenues par API)
  - `simId` : Identifiant de la SIM (pour Welcome Travelers)

### Vérification du statut de la SIM

- **URL** : `/distributors/suppliers/{supplier_id}/simstatus`
- **Méthode** : `GET`
- **Paramètres de requête** :
  - Identiques à ceux de la vérification du solde d'utilisation

### Solde global du distributeur

- **URL** : `/distributors/suppliers/{supplier_id}/globalbalances`
- **Méthode** : `GET`
- **Paramètres de requête** :
  - `startDate` : Date de début (format YYYY-MM-DD)
  - `endDate` : Date de fin (format YYYY-MM-DD)
  - `zoneLevel` : Niveau de détail de la zone ("region" ou "country")

## Erreurs

L'API peut renvoyer différentes erreurs HTTP standard avec des messages spécifiques :

- **400 Bad Request** : Requête mal formée ou paramètres invalides
- **401 Unauthorized** : Authentification manquante ou invalide
- **403 Forbidden** : Permissions insuffisantes
- **404 Not Found** : Ressource introuvable
- **429 Too Many Requests** : Trop de requêtes dans un intervalle donné
- **500 Internal Server Error** : Erreur interne du serveur

### Format des erreurs

```json
{
  "code": 0,
  "message": "Bad Request",
  "description": "Description détaillée de l'erreur"
}
```

### Erreurs spécifiques pour la création de transactions

- `missing offer_id parameter in body` : Le paramètre offer_id est manquant
- `invalid offer_id parameter` : L'identifiant de l'offre est invalide
- `bucket empty for offer {offer_id}` : Le bucket de l'offre est vide
- `missing parameters parameter in body` : Les paramètres sont manquants pour une transaction de recharge
- `bad parameter for transaction for offer {offer_id}` : Le MSISDN ou simId est invalide pour une transaction de recharge
