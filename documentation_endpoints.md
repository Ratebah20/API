# Documentation des Endpoints de l'API Orange Travel B2B

Cette documentation détaille tous les endpoints disponibles dans l'API Orange Travel B2B, leurs paramètres, les méthodes HTTP supportées et des exemples d'utilisation.

## Base URL

Toutes les requêtes doivent utiliser la base URL suivante :

```
https://api.orange.com/travel-b2b-sandbox/v1
```

## Authentification

Toutes les requêtes nécessitent un token d'authentification OAuth 2.0. Le token doit être inclus dans l'en-tête `Authorization` :

```
Authorization: Bearer {access_token}
```

## Endpoints de Base

### Test de Connexion

Vérifie la disponibilité de l'API et ses informations de version.

- **URL** : `/live`
- **Méthode** : `GET`
- **Paramètres** : Aucun
- **Réponse** :
  ```json
  {
    "isAlive": true,
    "version": "1.7.X"
  }
  ```

### Liste des Pays

Récupère la liste des pays avec leurs codes ISO, noms et préfixes téléphoniques.

- **URL** : `/countries`
- **Méthode** : `GET`
- **Paramètres** :
  - `offset` (optionnel) : Position de départ pour la pagination
  - `limit` (optionnel) : Nombre maximum d'éléments à retourner
- **Réponse** : Liste des pays

### Liste des Devises

Récupère les devises disponibles avec taux de conversion.

- **URL** : `/currencies`
- **Méthode** : `GET`
- **Paramètres** :
  - `offset` (optionnel) : Position de départ pour la pagination
  - `limit` (optionnel) : Nombre maximum d'éléments à retourner
- **Réponse** : Liste des devises avec leurs taux de conversion

## Transactions

Les transactions représentent les opérations commerciales effectuées via l'API, comme les recharges de crédit téléphonique ou l'activation d'eSIM.

### Créer une Transaction

Crée une nouvelle transaction (recharge, activation eSIM, etc.).

- **URL** : `/distributors/transactions`
- **Méthode** : `POST`
- **Corps de la Requête** :
  - `offer_id` (obligatoire) : Identifiant UUID de l'offre
  - `user_id` (optionnel) : Identifiant utilisateur côté distributeur
  - `parameters` (dépend du type d'offre) : Paramètres spécifiques au type de transaction

#### Exemples de Requêtes

**1. Recharge Orange France/Espagne (topup)**

```json
{
    "offer_id": "7b977bd5-c7dc-4681-bf33-c4bd2eadc266",
    "user_id": "635768534667763",
    "parameters": {
        "msisdn": "684587587"
    }
}
```

**2. Recharge Welcome Travelers**

```json
{
    "offer_id": "44f9d3b6-242e-47c6-b978-88d5e2e041ce",
    "parameters": {
        "simId": "1956392841179"
    }
}
```

**3. Activation eSIM**

```json
{
    "offer_id": "07966928-d3a3-453e-9944-b7ff1081794d"
}
```

- **Réponse** : Détails de la transaction créée, incluant un identifiant unique

**Exemple de réponse pour une activation eSIM**

```json
{
    "id": "386c9673-33f8-4364-bb78-e7b18371be5a",
    "billing_mode": "prepaid",
    "status": "ok",
    "product_type": "eSim",
    "creation_date": "2024-07-16T12:52:11Z",
    "expiration_date": null,
    "change_date": "2024-07-16T12:52:11Z",
    "offer_id": "07966928-d3a3-453e-9944-b7ff1081794d",
    "distributor_id": "8822b635-f710-47f1-a24c-5b9e58a84e7e",
    "resell_value": 27.5,
    "reference_currency": "EUR",
    "distributor_fees": 0.0,
    "distributor_fees_type": "value",
    "offer_bucket": 0,
    "user_id": "",
    "metadata": null,
    "product_id": "004088d8-20f3-4913-9b89-4bee25e0be79",
    "product_name": "eSim for preprod",
    "supplier_name": "Orange France",
    "distributor_name": "FakeDistributor",
    "parameters": {
        "supplier_ref": "3561292346865",
        "expiration_date": "None",
        "prefix": "33",
        "msisdn": "0678578522",
        "activation_code": "Me3ddE4i-S3krivxZZIjcm1tbwgRhh2ySwTg74Lbf...5_qPSjKBX-AE4=",
        "iccid": "",
        "nsce": "02322145207458",
        "pin_code": "0000",
        "puk": "71289750",
        "matching_id": "",
        "smdp_url": ""
    }
}
```

**Note** : Pour les transactions eSIM, le code d'activation (`activation_code`) est chiffré avec la clé publique RSA du distributeur et encodé en base64. Il doit être décodé puis déchiffré avec la clé privée correspondante.

### Récupérer une Transaction

Récupère les détails d'une transaction spécifique.

- **URL** : `/distributors/transactions/{transaction_id}`
- **Méthode** : `GET`
- **Paramètres de Chemin** :
  - `transaction_id` (obligatoire) : Identifiant unique de la transaction
- **Réponse** : Détails complets de la transaction

### Lister les Transactions

Récupère la liste des transactions avec possibilité de filtrage.

- **URL** : `/distributors/transactions`
- **Méthode** : `GET`
- **Paramètres de Requête** :
  - `offset` (optionnel) : Position de départ pour la pagination
  - `limit` (optionnel) : Nombre maximum d'éléments à retourner
  - `status` (optionnel) : Filtre par statut (ex: "ok", "error")
  - `product_type` (optionnel) : Filtre par type de produit (ex: "topup", "eSim")
  - `start_date` (optionnel) : Date de début pour filtrer (format ISO)
  - `end_date` (optionnel) : Date de fin pour filtrer (format ISO)
- **Réponse** : Liste des transactions correspondant aux critères

### Compter les Transactions

Compte le nombre de transactions correspondant aux critères de filtrage.

- **URL** : `/distributors/transactions/count`
- **Méthode** : `GET`
- **Paramètres de Requête** : Mêmes options de filtrage que pour la liste des transactions
- **Réponse** : Nombre total de transactions correspondant aux critères

## Gestion des Offres

### Liste des Offres

Récupère toutes les offres disponibles pour le distributeur.

- **URL** : `/distributors/offers`
- **Méthode** : `GET`
- **Paramètres** :
  - `offset` (optionnel) : Position de départ pour la pagination
  - `limit` (optionnel) : Nombre maximum d'éléments à retourner
- **Réponse** : Liste des offres disponibles

### Détails d'une Offre

Récupère les détails d'une offre spécifique.

- **URL** : `/distributors/offers/{offer_id}`
- **Méthode** : `GET`
- **Paramètres de chemin** :
  - `offer_id` (obligatoire) : Identifiant UUID de l'offre
- **Réponse** : Détails complets de l'offre

### Personnaliser une Offre

Permet de modifier certains paramètres d'une offre.

- **URL** : `/distributors/offers/{offer_id}`
- **Méthode** : `PATCH`
- **Paramètres de chemin** :
  - `offer_id` (obligatoire) : Identifiant UUID de l'offre
- **Corps de la requête** :
  ```json
  {
    "name": "Nom personnalisé",
    "distributor_fees": 10,
    "distributor_fees_type": "percent",
    "metadata": "Information supplémentaire"
  }
  ```
- **Réponse** : Offre mise à jour

## Gestion des Transactions

### Liste des Transactions

Récupère l'historique des transactions filtré par date/statut.

- **URL** : `/distributors/transactions`
- **Méthode** : `GET`
- **Paramètres** :
  - `startDate` (optionnel) : Date de début (format YYYY-MM-DD)
  - `endDate` (optionnel) : Date de fin (format YYYY-MM-DD)
  - `status` (optionnel) : Statut des transactions
  - `offer` (optionnel) : Filtre par identifiant d'offre
  - `supplier` (optionnel) : Filtre par identifiant de fournisseur
  - `limit` (optionnel) : Nombre maximum d'éléments à retourner
  - `offset` (optionnel) : Position de départ pour la pagination
  - `user` (optionnel) : Identifiant utilisateur
- **Réponse** : Liste des transactions

### Créer une Transaction

Crée une nouvelle transaction pour une offre.

- **URL** : `/distributors/transactions`
- **Méthode** : `POST`
- **Corps de la requête** :
  ```json
  {
    "offer_id": "id_offre",
    "voucher_id": "id_voucher",
    "user_id": "id_utilisateur",
    "parameters": {
      "msisdn": "numéro_mobile"
    }
  }
  ```
- **Réponse** : Détails de la transaction créée

### Détails d'une Transaction

Récupère les détails d'une transaction spécifique.

- **URL** : `/distributors/transactions/{transaction_id}`
- **Méthode** : `GET`
- **Paramètres de chemin** :
  - `transaction_id` (obligatoire) : Identifiant UUID de la transaction
- **Réponse** : Détails complets de la transaction

### Nombre de Transactions

Compte le nombre de transactions selon filtre.

- **URL** : `/distributors/transactions/count`
- **Méthode** : `GET`
- **Paramètres** :
  - `startDate` (optionnel) : Date de début (format YYYY-MM-DD)
  - `endDate` (optionnel) : Date de fin (format YYYY-MM-DD)
  - `status` (optionnel) : Statut des transactions
  - `offer` (optionnel) : Filtre par identifiant d'offre
  - `supplier` (optionnel) : Filtre par identifiant de fournisseur
  - `user` (optionnel) : Identifiant utilisateur
- **Réponse** : Nombre de transactions correspondant aux critères

## Gestion des Fournisseurs et eSIM

### Liste des Fournisseurs

Récupère la liste des fournisseurs disponibles.

- **URL** : `/distributors/suppliers`
- **Méthode** : `GET`
- **Paramètres** : Aucun
- **Réponse** : Liste des fournisseurs

### Statut d'une SIM/eSIM

Vérifie le statut d'une carte SIM/eSIM.

- **URL** : `/distributors/suppliers/{supplier_id}/simstatus`
- **Méthode** : `GET`
- **Paramètres de chemin** :
  - `supplier_id` (obligatoire) : Identifiant UUID du fournisseur
- **Paramètres de requête** :
  - `transaction` (optionnel) : Identifiant de transaction (pour eSIM via API)
  - `simId` (optionnel) : Identifiant de la SIM (pour SIM physique ou eSIM via bulk)
- **Réponse** : Statut détaillé de la SIM/eSIM

### Consommations d'une SIM

Récupère les données de consommation.

- **URL** : `/distributors/suppliers/{supplier_id}/usagebalances`
- **Méthode** : `GET`
- **Paramètres de chemin** :
  - `supplier_id` (obligatoire) : Identifiant UUID du fournisseur
- **Paramètres de requête** :
  - `transaction` (optionnel) : Identifiant de transaction (pour eSIM via API)
  - `simId` (optionnel) : Identifiant de la SIM (pour SIM physique ou eSIM via bulk)
- **Réponse** : Données détaillées de consommation (data, appels, SMS)

### Statistiques Globales

Récupère les statistiques globales.

- **URL** : `/distributors/suppliers/{supplier_id}/globalbalances`
- **Méthode** : `GET`
- **Paramètres de chemin** :
  - `supplier_id` (obligatoire) : Identifiant UUID du fournisseur
- **Paramètres de requête** :
  - `startDate` (obligatoire) : Date de début (format YYYY-MM-DD)
  - `endDate` (obligatoire) : Date de fin (format YYYY-MM-DD)
  - `zoneLevel` (obligatoire) : Niveau de détail de zone ("region" ou "country")
- **Réponse** : Statistiques globales pour la période spécifiée

## Gestion des Clés RSA

### Récupérer Clé Publique

Récupère la clé publique RSA actuelle.

- **URL** : `/distributors/keys`
- **Méthode** : `GET`
- **Paramètres de requête** :
  - `encoding` (optionnel) : Format d'encodage de la clé ("base64")
- **Réponse** : Clé publique RSA actuelle

### Configurer Clé Publique

Définit une nouvelle clé publique RSA.

- **URL** : `/distributors/keys`
- **Méthode** : `POST`
- **Corps de la requête** :
  ```json
  {
    "key_type": "rsa256",
    "public_key_value": "clé publique RSA"
  }
  ```
- **Réponse** : Confirmation de la mise à jour de la clé

## Codes de Statut HTTP

- `200 OK` : Requête réussie
- `201 Created` : Ressource créée avec succès
- `400 Bad Request` : Requête invalide (paramètres manquants ou incorrects)
- `401 Unauthorized` : Authentification requise ou invalide
- `404 Not Found` : Ressource non trouvée
- `500 Internal Server Error` : Erreur serveur

## Exemples d'Utilisation

### Exemple 1: Récupérer la liste des offres

```python
import requests

url = "https://api.orange.com/travel-b2b-sandbox/v1/distributors/offers"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json"
}
params = {
    "limit": 10,
    "offset": 0
}

response = requests.get(url, headers=headers, params=params)
offers = response.json()
```

### Exemple 2: Créer une transaction pour une recharge

```python
import requests
import json

url = "https://api.orange.com/travel-b2b-sandbox/v1/distributors/transactions"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}
data = {
    "offer_id": "12345678-1234-1234-1234-123456789012",
    "parameters": {
        "msisdn": "33612345678"
    }
}

response = requests.post(url, headers=headers, json=data)
transaction = response.json()
```

### Exemple 3: Vérifier le statut d'une eSIM

```python
import requests

supplier_id = "12345678-1234-1234-1234-123456789012"
transaction_id = "87654321-4321-4321-4321-210987654321"

url = f"https://api.orange.com/travel-b2b-sandbox/v1/distributors/suppliers/{supplier_id}/simstatus"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json"
}
params = {
    "transaction": transaction_id
}

response = requests.get(url, headers=headers, params=params)
sim_status = response.json()
```

## Bonnes Pratiques

1. **Gestion des erreurs** : Toujours vérifier le code de statut HTTP et gérer les erreurs appropriées.
2. **Authentification** : Renouveler le token d'accès avant qu'il n'expire.
3. **Pagination** : Utiliser les paramètres `limit` et `offset` pour gérer les grandes quantités de données.
4. **Sécurité** : Stocker les clés privées RSA de manière sécurisée et ne jamais les exposer.
5. **Validation** : Valider les données d'entrée avant de les envoyer à l'API.
