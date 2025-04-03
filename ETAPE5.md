# Étape 5 : Gestion des Recharges à la Demande (Topup Management)

## Objectif de cette étape

Cette étape explique en détail comment réaliser techniquement une transaction de recharge (topup) à la demande via l'API Orange Travel B2B. Le but est d'automatiser totalement ce processus pour simplifier la gestion des ventes et des recharges.

## Pourquoi gérer les topups via l'API ?

L'utilisation de l'API pour gérer les recharges permet :

- Un traitement automatisé, rapide et sécurisé des recharges.
- Une gestion simplifiée du stock et des transactions.
- Une réponse rapide et claire au client final (succès ou échec immédiat).

## Déroulement technique du processus de recharge

### 1. Création d'une transaction

Le distributeur doit envoyer une requête API pour créer une nouvelle transaction de recharge.

- **Exemple de requête minimale :**

```json
POST /distributors/transactions
{
    "offer_id": "id_offre",
    "parameters": {
        "msisdn": "numéro_mobile"
    }
}
```

### 2. Vérification du stock (Bucket)

L'API vérifie automatiquement si le stock disponible chez le distributeur est suffisant :

- Si le stock est épuisé, la transaction est immédiatement rejetée.

### 3. Résultat de la transaction

Selon le résultat, deux réponses possibles :

- **Succès :**
  - Déduction automatique d'une unité du stock.
  - Confirmation positive retournée au distributeur.

- **Échec :**
  - Le stock reste inchangé.
  - Réponse négative retournée avec la raison de l’échec.

## Cas particulier de Welcome Travelers

- Pour les recharges Welcome Travelers, la requête utilise `simId` au lieu du `msisdn`.

**Exemple :**

```json
POST /distributors/transactions
{
    "offer_id": "id_offre_welcome",
    "parameters":{
        "simId": "identifiant_sim"
    }
}
```

## Bonnes pratiques

- Implémentez une gestion précise des réponses de l’API pour informer immédiatement les clients finaux.
- Suivez régulièrement votre stock (bucket) pour éviter des échecs inutiles.

Cette étape garantit une gestion optimale des recharges mobiles, essentielle pour une expérience client fluide et réactive.

