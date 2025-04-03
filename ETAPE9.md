# Étape 9 : Gestion du Statut des SIM/eSIM (SIM Status Management)

## Objectif de cette étape

Cette étape explique comment récupérer techniquement le statut actuel d'une SIM ou eSIM vendue à un client final via l'API Orange Travel B2B. Cela est essentiel pour un support client réactif et efficace.

## Pourquoi gérer le statut des SIM/eSIM ?

La récupération du statut permet :

- Une réponse rapide et précise en cas de réclamation ou problème signalé par le client.
- D’assurer une gestion proactive des lignes mobiles, notamment pour éviter des désactivations imprévues.

## Comment récupérer le statut des SIM/eSIM ?

Utilisez la requête suivante avec la méthode GET :

```json
GET /distributors/suppliers/{supplier_id}/simstatus?transaction={trx_id}
```

- `{supplier_id}` : Identifiant spécifique au fournisseur (Orange France, Welcome Travelers).
- `{trx_id}` : Identifiant unique de la transaction concernée.

## Exemples de statuts possibles

| Statut                              | Description claire                                                |
|-------------------------------------|--------------------------------------------------------------------|
| free                                | La SIM/eSIM n’est pas attachée à un forfait                    |
| not installed                       | Jamais installée sur un appareil                               |
| available                           | Active et utilisable normalement                               |
| suspended fraud                     | Ligne suspendue suite à suspicion de fraude                    |
| suspended kyc default               | Ligne désactivée faute de vérification KYC                     |
| suspended by operator               | Désactivation directe par l'opérateur                          |
| suspended following a theft or loss | Désactivation suite à une perte ou vol signalé                 |
| expired                             | Ligne expirée définitivement                                   |
| uninstalled                         | eSIM désinstallée de l'appareil initial                        |
| revoked by operator                 | Ligne définitivement révoquée par l'opérateur                  |
| sim swap                            | Échange de la SIM, activation d'une nouvelle SIM à la place    |

## Exemple concret de réponse

```json
{
    "status": "available",
    "creation_date": "2024-07-15T14:00:00Z",
    "activation_date": "2024-09-13T14:00:00Z",
    "last_topup_date": null,
    "expiration_date": "2024-11-14T13:00:00Z"
}
```

## Bonnes pratiques

- Intégrez systématiquement cette vérification dans vos procédures de support client.
- Informez rapidement les clients finaux de l’état exact de leur SIM/eSIM.

Cette étape garantit un suivi précis et efficace de chaque ligne mobile distribuée.

