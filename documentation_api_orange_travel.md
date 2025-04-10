# Documentation API Orange Travel B2B

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

L'accès à cette API est sécurisé par le framework OAuth 2.0 avec le type d'autorisation "Client Credentials", ce qui signifie que vous devrez présenter un `access_token` OAuth 2.0 chaque fois que vous souhaitez interroger cette API.

Il est facile d'obtenir cet `access_token` : envoyez simplement une requête au point d'entrée de négociation de jeton approprié, avec un en-tête d'authentification Basic valorisé avec votre propre `client_id` et `client_secret`.

Pour cette API, le point d'entrée de négociation du jeton est :

```
https://api.orange.com/oauth/v3/token
```

Un guide technique est disponible pour apprendre à négocier et gérer ces `access_token`.

**Important**

- Veuillez porter une attention particulière à la gestion correcte des réponses d'erreur d'authentification dans votre application. Voir la section Erreurs.
- La durée de vie par défaut de l'`access_token` est de 60 minutes.
- L'en-tête `Accept: application/json` est maintenant requis, lorsqu'il est omis, vous recevrez une erreur 406.

## URL de base

L'URL de base est la première partie de l'URL d'invocation complète, juste avant les chemins de ressources. Chaque fois que vous effectuez des requêtes sur cette API, vous devrez ajouter l'URL de base suivante aux chemins de ressources définis pour cette API.

Si vous interrogez cette API et recevez une réponse d'erreur HTTP 404 NOT FOUND, veuillez d'abord vérifier que l'URL de base est correcte.

L'URL de base pour cette API est :

```
https://api.orange.com/travel-b2b-sandbox/v1/
```

## Entités gérées par l'API Travel B2B

Cette API permet à un distributeur de générer des transactions sur des produits fournis par Orange Travelers. Chaque produit disponible est intégré dans des offres avec des paramètres commerciaux spécifiques négociés entre le distributeur et Orange Travelers.

Il existe 3 types d'API :

1. API pour récupérer la liste des offres
2. API pour générer une transaction
3. API pour récupérer des informations sur une transaction ou une liste de transactions

L'API Travel B2B gère les entités suivantes :

### Produit (Product)

Un produit est un objet qui représente un article acheté par les clients finaux. Un produit est associé à un fournisseur qui fournit une plateforme pour compléter la transaction. Tous les paramètres du produit sont définis par Orange.

#### Propriétés d'un produit

| Propriété | Description |
|------------|-------------|
| Name | Nom du produit (défini par Orange) |
| Description | Description du produit |
| Tags | Étiquettes du produit pour faciliter la recherche ou le filtrage |
| Type | Type de produit : eSim ou topup |
| Status | Indique si le produit est disponible ou non |
| Coverage zone | Liste des pays où le produit est disponible |
| Supplier | Orange Espagne, Orange France, Welcome Travelers |
| Metadata | Informations supplémentaires sur le produit selon le type de produit |
| Bonus value | Bonus du produit fournisseur |
| Bonus activation date | Date d'activation du bonus du produit fournisseur |
| Bonus expiration date | Date d'expiration du bonus du produit fournisseur |

### Fournisseur (Supplier)

Un fournisseur propose des produits utilisés pour créer des offres. Chaque fournisseur dispose de son propre coffre-fort. Un fournisseur propose généralement des eSim ou des recharges. Pour l'instant, le système gère 4 fournisseurs : Orange France, Orange Espagne, Welcome Travelers et Orange Travel B2B.

### Offre (Offer)

Cette entité est une association entre un produit et un distributeur. Elle contient la valeur de revente fixée par Orange. Un distributeur peut ajouter des frais supplémentaires à la valeur de revente si nécessaire. Il peut également surcharger le nom et ajouter des métadonnées pour ses propres besoins. L'offre contient également un bucket qui indique le stock de produits autorisé au distributeur.

#### Propriétés d'une offre

| Propriété | Description |
|------------|-------------|
| Name template | Modèle de nom d'offre |
| Product | Produit associé à l'offre |
| Bucket | Nombre de produits restants dans le stock du distributeur |
| Distributor | Propriétaire de l'offre |
| Tags | Étiquettes d'offre pour faciliter la recherche ou le filtrage |
| Resell value | Montant facturé au distributeur par Orange Travelers pour le produit |
| Distributor Fees | Frais supplémentaires fixés par le distributeur |

### Transaction

Cette entité représente une transaction d'achat d'une offre. Elle contient toutes les informations nécessaires à Orange Travel pour pouvoir recharger le distributeur.

## Personnalisation des offres

Les offres sont initialement créées par Orange pour un distributeur. Le distributeur peut modifier certains paramètres pour les adapter à son contexte. Le distributeur peut personnaliser certaines propriétés de l'offre :

- **name** : le distributeur peut modifier le nom d'offre par défaut qui est le même que le nom du produit
- **fees** : le distributeur peut appliquer des frais sur le prix initial. La valeur de revente reste inchangée dans les transactions
- **metadata** : le distributeur peut attacher des métadonnées libres à l'offre

### Exemple de requête de personnalisation d'offre

```bash
curl --location --request PATCH 'https://api.orange.com/travel-b2b-sandbox/distributors/offers/12fee06a-273e-45c8-9e04-8841e74a749a' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer c3VwZXJfYW......dVN3Mm5FVXI4THBmNmNtN0s=' \
--data '{
    "name" : "My custom offer name",
    "distributor_fees" : 10,
    "distributor_fees_type" : "percent",
    "metadata" : "some additional information"
}'
```

### Exemple d'offre distributeur

```json
{
    "id": "12fee06a-273e-45c8-9e04-8841e74a749a",
    "name": "My custom offer name",
    "product": {
        "id": "e3585509-8f4e-4bca-a98f-20a323532690",
        "orange_travel_id": "OT456360478",
        "name": "Topup 10 € with data",
        "description": "<b>This top up includes: </b></br>5GB in Europe</br><..... card validity for 1 month.</b>",
        "type": "topup",
        "status": "available",
        "delivery" : ["api"],
        "reference_currency": "EUR",
        "bonus_value": 0.0,
        "bonus_activation_date": null,
        "bonus_expiration_date": null,
        "supplier_id": "7413e966-c97c-11ed-b80c-fa163e78aa28",
        "metadata": {
            "validity_duration": 14,
            "validity_unit": "days",
            "sms": 0,
            "sms_cost": null,
            "airtime_duration": 0,
            "airtime_unit": "hours",
            "airtime_cost": null,
            "data_amount": 5,
            "data_unit": "Gb"
        },
        "coverage_zone": []
    },
    "distributor_id": "e80797d1-e182-4079-a757-194d67998d2f",
    "bucket_update_date": null,
    "tags": "",
    "creation_date": "2024-07-16T12:52:11Z",
    "expiration_date": null,
    "bucket": 101,
    "resell_value": 7.92,
    "distributor_fees": 10.0,
    "distributor_fees_type": "percent",
    "metadata": "some additional information"
}
```

## Gestion des prix

Dans l'exemple ci-dessus, la valeur de référence du produit de recharge est de 10 €.

Orange Travelers facturera au distributeur 7,92 € pour ce produit (resell_value).

Pour toute information sur les prix et les conditions commerciales, veuillez contacter votre gestionnaire de compte Orange Travelers.

## Gestion des recharges (Topup)

Le diagramme de flux suivant illustre une utilisation de l'API Travel B2B. Pour ce cas d'utilisation, nous considérons que le distributeur a configuré sa plateforme de service avec les identifiants fournis par le portail Orange Developer.

<!-- Diagramme de flux pour la recharge -->
<!-- Note: L'image originale n'est pas accessible via GitHub. 

La requête POST /distributors/transactions nécessite au minimum la charge utile suivante :

```json
{
    "offer_id": "7b977bd5-c7dc-4681-bf33-c4bd2eadc266",
    "parameters" : {
        "msisdn" : "684587587"
    }
}
```

Cette charge utile est compatible avec les offres de recharge Orange France et Orange Espagne. Concernant le format msisdn, l'API prend en compte les 9 derniers chiffres.

Pour les recharges Welcome Travelers, le paramètre obligatoire est le simId. Pour ce fournisseur, le msisdn n'est pas fourni :

```json
{
    "offer_id": "44f9d3b6-242e-47c6-b978-88d5e2e041ce",
    "parameters":{
        "simId": "1956392841179"
    }
}
```

Pour faciliter la gestion des transactions côté distributeur, la charge utile de transaction peut contenir un paramètre libre user_id. Ce champ est fourni par le système d'information du distributeur.

```json
{
    "offer_id": "7b977bd5-c7dc-4681-bf33-c4bd2eadc266",
    "user_id" : "635768534667763",  
    "parameters" : {
        "msisdn" : "684587587"
    }
}
```

## Gestion des eSIM

### Gestion de la sécurité

Pour être autorisé à gérer les offres eSIM, le distributeur doit générer une paire de clés RSA et fournir la clé publique à Orange.

<!-- Diagramme de gestion des clés publiques du distributeur -->
<!-- Note: L'image originale n'est pas accessible via GitHub. Veuillez ajouter le diagramme localement si disponible. -->

#### Génération d'une paire de clés RSA :

```bash
openssl genrsa -out {private_key_file_name} 4096
openssl rsa -in {private_key_file_name} -pubout -out {public_key_file_name}
```

La clé publique est utilisée par Orange pour chiffrer les informations sensibles dans la réponse de transaction eSIM. Le code d'activation de l'eSIM est chiffré par Orange avec la clé publique du distributeur.

Voici la fonction de chiffrement utilisée par le serveur :

```python
def encryptRSA(activation_code, public_key):
    activation_code_bytes = activation_code.encode('utf-8')
    encrypted_text = public_key.encrypt(
        activation_code_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return str(base64.b64encode(encrypted_text).decode('utf-8'))
```

Seul le distributeur qui possède la clé privée associée peut la déchiffrer. Le distributeur doit conserver sa clé privée dans un endroit sécurisé.

Voici un exemple pour déchiffrer le code d'activation :

```python
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
...
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
    text_clear = texte_clear_bytes.decode('utf-8')
    return text_clear
```

### Ajout ou mise à jour de la clé publique du distributeur

L'API Travel B2B n'autorise qu'une seule clé par distributeur.

Avant d'appeler le endpoint POST /distributors/keys, aucune clé n'est définie sur le serveur Travel B2B pour un distributeur. Le distributeur n'est pas autorisé à effectuer des transactions eSIM, même si son bucket est correctement configuré.

Lors d'un premier appel à POST /distributors/keys, la clé est créée et le distributeur peut utiliser les offres eSIM.

Lors des appels suivants, la clé précédente est remplacée par la nouvelle. Il n'y a pas de retour en arrière possible. La mise à jour doit être effectuée si la clé privée du distributeur a été compromise.

Le distributeur est responsable de cette gestion de la sécurité.

### Transaction eSIM

Le diagramme de flux suivant illustre une utilisation de l'API Travel B2B. Pour ce cas d'utilisation, nous considérons que le distributeur a configuré sa plateforme de service avec les identifiants fournis par le portail Orange Developer.

<!-- Diagramme de consommation eSIM -->
<!-- Note: L'image originale n'est pas accessible via GitHub. Veuillez ajouter le diagramme localement si disponible. -->

Pour une transaction eSIM, la seule propriété obligatoire est l'offer_id :

```json
{
    "offer_id": "07966928-d3a3-453e-9944-b7ff1081794d"
}
```

La charge utile de la réponse de transaction contient toutes les informations concernant l'eSIM :

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

La propriété `activation_code` est chiffrée avec la clé publique du distributeur. La propriété `activation_code` est encodée en base64. Elle doit être décodée avant d'être déchiffrée. Elle doit être déchiffrée avec la clé privée par le distributeur.

Le code d'activation peut être transformé en image QRCode pour être installé sur l'appareil de l'utilisateur final.

## Gestion KYC

Dans tous les cas, pour les forfaits SIM ou eSIM prépayés, pour des raisons légales, l'utilisateur final doit enregistrer son document d'identité. Cette opération doit être effectuée dans les 30 jours suivant l'achat de la SIM ou eSIM. Au-delà de cette période, la ligne du client est désactivée. Pour enregistrer un document d'identité, le service Orange propose 2 formulaires :

- Pour les SIM ou eSIM Orange France : https://travel.orange.com/fr/orange-holidays
- Pour les SIM ou eSIM Welcome Travelers : https://travel.orange.com/fr/welcome-travelers

### Statut SIM

Pour votre support, l'API fournit une requête pour récupérer le statut actuel de la SIM. En cas de réclamation de votre client final, cela pourrait être utile.

La requête est :

```
GET /distributors/suppliers/{supplier_id}/simstatus?transaction={trx_id}
```

La requête renvoie les informations suivantes :

```json
{
    "status": "suspended fraud",
    "creation_date": "2024-07-15T14:00:00Z",
    "activation_date": "2024-09-13T14:00:00Z",
    "last_topup_date": null,
    "expiration_date": "2024-11-14T13:00:00Z"
}
```

#### Tableau des statuts

| Statut | Description |
|--------|-------------|
| free | La (e)SIM n'est attachée à aucun plan |
| not installed | La (e)SIM n'est pas installée |
| available | La (e)SIM est active |
| suspended fraud | Le fournisseur a détecté un comportement anormal et a suspendu la ligne |
| suspended kyc default | L'utilisateur final n'a pas fourni de document d'identité (passeport). Le fournisseur désactive sa ligne |
| suspended by operator | Le fournisseur désactive la ligne |
| suspended following a theft or loss | Le fournisseur désactive la ligne suite à un vol ou une perte |
| expired | La ligne est expirée et ne peut plus être utilisée |
| uninstalled | La (e)Sim est désinstallée de l'appareil initial |
| revoked by operator | Le fournisseur désactive la ligne |
| sim swap | Échange de SIM |

## Gestion des soldes d'utilisation

L'API fournit une requête pour récupérer le solde d'utilisation actuel. Cette fonctionnalité est actuellement uniquement disponible pour les numéros Welcome Travelers et Orange France.

La requête est :

```
GET /distributors/suppliers/{{wt_supplier_id}}/usagebalances?transaction={trx_id} => pour Welcome Travelers
GET /distributors/suppliers/{{ofr_supplier_id}}/usagebalances?transaction={trx_id} => pour Orange France 
```

La requête utilise le simId ou msisdn concerné par une transaction passée.

Pour Welcome Travelers, nous offrons la possibilité d'utiliser directement un simId :

```
GET /distributors/suppliers/{supplier_id}/usagebalances?simId={simId}
```

Dans les deux cas, cette requête renvoie les informations suivantes :

```json
{
    "first_activation_date": null,
    "number_expiration_date": "2025-05-10T00:00:00Z",
    "buckets": [
        {
            "activation_date": null,
            "expiration_date": "2024-11-05T00:00:00Z",
            "data_remaining": 13.2,
            "data_unit": "Gb",
            "airtime_remaining": 0,
            "airtime_unit": "seconds",
            "sms_remaining": 0,
            "name": "Carte Holiday Tourist LS"
        },
        {
            "activation_date": null,
            "expiration_date": "2024-11-05T00:00:00Z",
            "data_remaining": 0.0,
            "data_unit": "Gb",
            "airtime_remaining": 1800,
            "airtime_unit": "seconds",
            "sms_remaining": 0,
            "name": "Recharge Holiday Voix"
        }
    ]
}
```

### Récupération des identifiants de fournisseur

### Solde global du distributeur

Cet endpoint permet de récupérer les statistiques globales d'utilisation pour une période donnée (limitée à 6 mois). Il est particulièrement utile pour analyser la consommation de données à travers différentes zones géographiques.

```
GET /distributors/suppliers/{supplier_id}/globalbalances
```

#### Paramètres de requête

| Paramètre | Type | Description |
|------------|------|-------------|
| startDate | string | Date de début (format YYYY-MM-DD) |
| endDate | string | Date de fin (format YYYY-MM-DD) |
| zoneLevel | enum | Niveau de détail de la zone requis ("region" ou "country") |

#### Exemple de réponse

```json
{
  "start_date": "2024-01-01T00:00:00.000Z",
  "end_date": "2024-03-31T00:00:00.000Z",
  "zones": [
    {
      "name": "Europe",
      "code": "EU",
      "data_unit": "Mo",
      "data_amount": 1250
    },
    {
      "name": "North America",
      "code": "NA",
      "data_unit": "Mo",
      "data_amount": 782
    }
  ]
}
```

### Liste des fournisseurs

Pour récupérer l'identifiant du fournisseur, la requête suivante peut être utilisée :

```
GET /distributors/suppliers
```

Elle renvoie un tableau des fournisseurs actuellement pris en charge par l'API :

```json
[
    {
        "id": "7413e966-c97c-11ed-b80c-fa163e78aa28",
        "name": "Orange France",
        "connector_status": true
    },
    {
        "id": "92d376d4-0c18-4da8-9e6e-4dd173bc554e",
        "name": "Welcome Travelers",
        "connector_status": true
    },
    {
        "id": "e0c798dd-54a2-462d-8f87-79a44f7547a1",
        "name": "Orange Spain",
        "connector_status": false,
        "last_outage_date": "2025-03-06T19:07:34Z"
    },
    {
        "id": "e2c44763-fa73-11ef-bc0c-fa163ed2cb6e",
        "name": "Orange Travel B2B",
        "connector_status": true
    }
]
```

Les distributeurs peuvent appeler cette requête même pour les Sim ou eSim Welcome Travelers livrées en gros ou physiquement.

## Gestion des transactions

### Liste des transactions du distributeur

<!-- Diagramme de liste des transactions -->
![Diagramme de liste des transactions]

Un distributeur peut récupérer la liste de ses propres transactions. Il peut la récupérer au format JSON ou CSV. L'API prend des paramètres pour récupérer un sous-ensemble de transactions :

- Date de début et date de fin
- Identifiant de l'offre
- Identifiant de l'utilisateur (géré par le distributeur)
- Statut de la transaction

### Comptage des transactions

Un distributeur peut également récupérer le nombre total de transactions selon des critères de filtrage similaires. Cet endpoint est utile pour la pagination ou les rapports statistiques.

```
GET /distributors/transactions/count
```

#### Paramètres de requête

| Paramètre | Type | Description |
|------------|------|-------------|
| startDate | date-time | Date de début pour le filtrage |
| endDate | date-time | Date de fin pour le filtrage |
| status | string | Filtrage par statut de transaction |
| offer | string | Identifiant de l'offre à filtrer |
| supplier | string | Identifiant du fournisseur à filtrer |
| user | string | Identifiant externe provenant de la plateforme de service du distributeur |

#### Exemple de réponse

```json
{
  "count": 42
}
```

### Détail d'une transaction

Chaque transaction a des paramètres spécifiques selon le type de produit.

Pour un produit eSim, le endpoint POST /distributors/transactions/{transaction_id} renvoie les détails de la transaction dans la propriété parameters :

```json
{
    "id": "d3a82976-613d-44a4-8387-991035e25d1f",
    "billing_mode": "prepaid",
    "status": "ok",
    "product_type": "eSim",
    "creation_date": "Tue, 12 Mar 2024 17:59:18 GMT",
    "expiration_date": null,
    "change_date": "Tue, 12 Mar 2024 17:59:19 GMT",
    "offer_id": "03206821-70d6-43c7-8287-5a663919df1b",
    "distributor_id": "782d4ab7-22f2-42d5-9a76-e53b44fa7918",
    "resell_value": 43.99,
    "reference_currency": "EUR",
    "distributor_fees": 0.0,
    "distributor_fees_type": "value",
    "offer_bucket": 0,
    "user_id": "",
    "metadata": null,
    "product_id": "478dbe74-29a8-4da8-a749-a73d7f22232b",
    "product_name": "Orange Holiday Europe 30GO",
    "supplier_name": "Orange France",
    "distributor_name": "FakeDistributor",
    "parameters": {
        "supplier_ref": "3561292346865",
        "expiration_date": "None",
        "prefix": "33",
        "msisdn": "0678578545",
        "activation_code": "XodUlw4VwNPS-------o5xFIiypK7evuhp98ygM=",
        "iccid": "",
        "nsce": "02322145207458",
        "pin_code": "0000",
        "puk": "71289750",
        "matching_id": "",
        "smdp_url": ""
    }
}
```

Le code d'activation est toujours chiffré avec la clé publique du distributeur.

## Erreurs

**Important**

Ne pas coder une gestion appropriée des réponses d'erreur dans votre application peut affecter sa résilience. L'accès à l'API peut être révoqué si votre application génère trop d'erreurs non gérées.

Votre application doit analyser la réponse HTTP retournée pour vérifier si une erreur est retournée au lieu d'un 200 OK. Les API Orange utilisent des codes d'état HTTP appropriés pour indiquer toute erreur de traitement de requête, fournissant des informations détaillées sur le défaut sous-jacent. Cela vous aide à fournir un meilleur retour à vos utilisateurs et à mettre en œuvre un mécanisme de récupération de panne dans votre application.

Pour plus de détails sur les principaux codes d'erreur, le format de réponse, les conseils et le dépannage, consultez notre guide Handling API errors. Voici les erreurs client les plus courantes rencontrées.

### Erreurs 401

Si vous obtenez un code d'état 401 avec le code d'erreur 42 (comme ci-dessous), demandez alors un nouvel access_token.

```
HTTP/1.1 401 Unauthorized
Content-Type: application/json
{
  "code": 42,
  "message": "Expired credentials",
  "description": "The requested service needs credentials, and the ones provided were out-of-date."
}
```

**Important**
- Chaque access_token a une période de validité limitée (60 minutes par défaut). Cette période de validité peut changer au fil du temps pour se conformer aux règles de sécurité.
- Les demandes de jetons sont limitées à 50 requêtes par minute, lorsque la limite de débit est dépassée, vous recevrez une erreur 429. Par conséquent, NE demandez PAS un access_token chaque fois que vous invoquez l'API de service. NE codez PAS en dur une durée de validité dans votre application. Au lieu de cela, votre application doit analyser le code d'état retourné et le code d'erreur pour vérifier si elle a besoin de demander un nouvel access_token.
- Pour les autres erreurs 401 : vérifiez que vous fournissez le bon en-tête Autorization avec le bon Bearer.

### Erreurs 400

En cas de requête invalide vers l'API, vous recevrez un code d'erreur 400 avec des informations détaillées dans le message du corps, tel que :

```
HTTP/1.1 400 Bad Request
{
  "code": 25,
  "description": "Missing header",
  "message": "...."
}
```
