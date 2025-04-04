# Analyse de l'API Orange Travel B2B

## Introduction

Ce document résume l'analyse de l'API Orange Travel B2B basée sur l'examen des fichiers `context.md`, `documentation_API.md` et `odm-distributor-api.json`. L'objectif est de fournir une compréhension claire de la structure, des fonctionnalités et des exigences techniques de l'API pour faciliter son intégration.

## Contexte du projet

L'API Orange Travel B2B permet aux entreprises partenaires (distributeurs) de gérer de manière automatisée la distribution de recharges mobiles (topups) et d'eSIMs à leurs clients finaux. Cette API offre une solution complète pour :

- Consulter les offres disponibles (recharges et eSIMs)
- Personnaliser ces offres selon les besoins commerciaux spécifiques
- Réaliser des transactions automatisées pour les clients finaux
- Suivre les transactions et les consommations en temps réel
- Gérer de façon sécurisée les données sensibles liées aux eSIMs (codes d'activation)

## Structure technique de l'API

### Informations de base
- **Titre**: Travel B2B API
- **Version**: 1.7.X
- **Environnements**:
  - Sandbox: `https://api.orange.com/travel-b2b-sandbox/v1`
  - Production: `https://api.orange.com/travel-b2b/v1`

### Authentification
- Méthode: OAuth 2.0 avec flow de type "Client Credentials"
- URL du token: `https://api.orange.com/oauth/v3/token`
- Scope requis: `sekapi:manager:access:api`

### Principales entités

1. **Distributeurs** (votre rôle dans l'API)
   - Gestion des offres personnalisées
   - Création et suivi des transactions
   - Gestion des clés de sécurité (RSA)

2. **Fournisseurs (Suppliers)**
   - Liste des fournisseurs disponibles
   - Statut des SIM/eSIM
   - Consommation et soldes

3. **Produits et Offres**
   - Différents types: topup, eSim, simCard
   - Personnalisation possible (prix, frais, métadonnées)
   - Gestion des stocks (bucket)

4. **Transactions**
   - Création (topup ou eSIM)
   - Suivi des statuts
   - Filtrage et recherche

## Points d'accès principaux

### Gestion des offres
- `GET /distributors/offers` - Liste des offres
- `GET /distributors/offers/{id}` - Détails d'une offre
- `PATCH /distributors/offers/{id}` - Personnalisation d'une offre

### Gestion des transactions
- `POST /distributors/transactions` - Création de transaction
- `GET /distributors/transactions` - Liste des transactions
- `GET /distributors/transactions/{id}` - Détails d'une transaction
- `GET /distributors/transactions/count` - Comptage des transactions

### Sécurité eSIM
- `POST /distributors/keys` - Configuration de la clé publique RSA
- `GET /distributors/keys` - Récupération de la clé publique actuelle

### Suivi des consommations
- `GET /distributors/suppliers/{id}/usagebalances` - Solde de consommation
- `GET /distributors/suppliers/{id}/simstatus` - État de la SIM/eSIM
- `GET /distributors/suppliers/{id}/globalbalances` - Solde global du distributeur

## Schémas de données importants

1. **TransactionCreation** - Structure pour créer une transaction
   - Champ obligatoire: `offer_id`
   - Paramètres spécifiques selon le type (TopupParameters ou SimParameters)

2. **DistributorTransaction** - Structure complète d'une transaction
   - Inclut les informations de statut, dates, valeurs, etc.

3. **OfferLight** - Structure d'une offre
   - Contient des informations sur le produit associé, le prix, etc.

4. **DistributorKey** - Structure pour la gestion des clés RSA
   - Utilisé pour le chiffrement des données sensibles (codes d'activation eSIM)

## Étapes d'intégration

D'après la documentation, l'intégration complète avec l'API Orange Travel B2B Sandbox se déroule en 12 étapes :

1. **Base URL et vérifications initiales**
2. **Entités principales** - Compréhension des types d'API et des entités
3. **Personnalisation des offres** - Modification des paramètres d'une offre
4. **Gestion des prix** - Compréhension des différentes valeurs de prix
5. **Gestion des recharges à la demande (Topup)** - Création de transactions de recharge
6. **Gestion sécurisée des eSIM** - Génération et gestion des clés RSA
7. **Transaction eSIM** - Création de transactions eSIM
8. **Vérification d'identité KYC** - Processus obligatoire sous 30 jours
9. **Statut de la SIM/eSIM** - Vérification de l'état des cartes SIM
10. **Gestion des consommations** - Suivi des consommations restantes
11. **Gestion des transactions** - Liste et détails des transactions
12. **Gestion des erreurs** - Traitement des codes d'erreur HTTP

## Sécurité et gestion des eSIMs

Un aspect important de l'API concerne la gestion sécurisée des eSIMs via chiffrement RSA :

1. **Génération des clés RSA** :
   ```
   openssl genrsa -out distributor_private.pem 4096
   openssl rsa -in distributor_private.pem -pubout -out distributor_public.pem
   ```

2. **Transmission de la clé publique à Orange** :
   ```
   POST /distributors/keys
   {
     "public_key": "clé publique RSA"
   }
   ```

3. **Déchiffrement des codes d'activation** :
   Les codes d'activation reçus lors des transactions eSIM sont chiffrés avec la clé publique RSA fournie par le distributeur. Ils doivent être déchiffrés avec la clé privée avant usage.

## Conclusion

L'API Orange Travel B2B offre une solution complète pour la distribution de recharges mobiles et d'eSIMs. Elle est conçue selon les principes REST, avec une sécurité OAuth2, et permet de gérer l'ensemble du flux de distribution, de la consultation des offres jusqu'au suivi des consommations.

L'intégration technique nécessite une attention particulière à la gestion des clés RSA pour les eSIMs, ainsi qu'à la compréhension des différentes entités et de leurs relations.
