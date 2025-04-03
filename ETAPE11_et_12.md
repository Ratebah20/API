# Étape 11 : Gestion des Transactions (Transaction Management)

## Objectif de cette étape

Cette étape explique comment récupérer techniquement la liste complète des transactions réalisées par le distributeur ainsi que les détails spécifiques d'une transaction en particulier, en utilisant l'API Orange Travel B2B.

## Pourquoi gérer les transactions ?

La gestion des transactions permet :

- Un suivi précis et détaillé de toutes les ventes (SIM/eSIM).
- Une meilleure réactivité dans le traitement des réclamations ou demandes de support des clients.
- Une gestion efficace des opérations commerciales.

## Comment récupérer la liste des transactions ?

Utilisez la requête suivante avec la méthode GET :

```json
GET /distributors/transactions
```

### Filtres disponibles :

- Dates (`start_date` et `end_date`)
- Identifiant d'offre (`offer_id`)
- Identifiant utilisateur (`user_id`)
- Statut de transaction (`status`)

## Comment récupérer les détails d’une transaction spécifique ?

Utilisez la requête suivante :

```json
GET /distributors/transactions/{transaction_id}
```

- `{transaction_id}` : Identifiant unique d’une transaction spécifique.

## Exemple concret d’une réponse détaillée (eSIM)

```json
{
    "id": "transaction_id",
    "status": "ok",
    "product_type": "eSim",
    "creation_date": "2024-03-12T17:59:18Z",
    "offer_id": "id_offre",
    "distributor_id": "id_distributeur",
    "resell_value": 43.99,
    "parameters": {
        "msisdn": "0678578545",
        "activation_code": "code_activation_chiffré",
        "pin_code": "0000",
        "puk": "71289750"
    }
}
```

- Le code d'activation est chiffré avec votre clé publique RSA, vous devez le déchiffrer avant usage.

## Gestion rigoureuse des erreurs

- Vérifiez toujours les codes HTTP des réponses API (200 OK pour succès).
- Gérez précisément les erreurs courantes (ex : token JWT expiré, requête mal formée).

### Exemples d’erreurs courantes :

- **401 Unauthorized** (Token JWT expiré)
- **400 Bad Request** (Requête incorrecte ou mal formée)

## Bonnes pratiques

- Implémentez une gestion rigoureuse et automatisée des erreurs.
- Documentez clairement les erreurs possibles et leurs solutions.
- Automatisez autant que possible la récupération et le traitement des transactions pour assurer un suivi efficace.

Cette étape garantit une gestion efficace et sécurisée des transactions commerciales, indispensable à la performance opérationnelle du distributeur.