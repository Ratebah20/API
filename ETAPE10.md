# Étape 10 : Gestion des Consommations (Usage Balance Management)

## Objectif de cette étape

Cette étape explique comment récupérer techniquement les informations détaillées sur les consommations restantes (data, voix, SMS) associées à une SIM ou eSIM vendue via l'API Orange Travel B2B. Cela permet un suivi précis des consommations des clients finaux.

## Pourquoi gérer les consommations ?

La gestion des consommations permet :

- D'offrir un suivi précis et transparent aux clients.
- De diagnostiquer rapidement des problèmes éventuels signalés par les clients.
- De mieux gérer les forfaits et recharges proposés.

## Comment récupérer les consommations restantes ?

Utilisez les requêtes suivantes avec la méthode GET selon le fournisseur concerné :

### Welcome Travelers

Par transaction :

```json
GET /distributors/suppliers/{wt_supplier_id}/usagebalances?transaction={trx_id}
```

Ou directement par simId :

```json
GET /distributors/suppliers/{wt_supplier_id}/usagebalances?simId={simId}
```

### Orange France

Par transaction uniquement :

```json
GET /distributors/suppliers/{ofr_supplier_id}/usagebalances?transaction={trx_id}
```

## Exemple concret de réponse

```json
{
    "first_activation_date": null,
    "number_expiration_date": "2025-05-10T00:00:00Z",
    "buckets": [
        {
            "expiration_date": "2024-11-05T00:00:00Z",
            "data_remaining": 13.2,
            "data_unit": "Gb",
            "airtime_remaining": 0,
            "airtime_unit": "seconds",
            "sms_remaining": 0,
            "name": "Carte Holiday Tourist LS"
        },
        {
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

## Bonnes pratiques

- Proposez un accès clair à ces informations via une interface client intuitive.
- Utilisez ces données pour anticiper les besoins de recharge ou d’extension de forfait des clients.
- Réalisez régulièrement des vérifications pour prévenir d'éventuels problèmes ou réclamations.

Cette étape garantit une gestion proactive et transparente des forfaits et consommations mobiles, essentielle pour maintenir une excellente expérience utilisateur.

