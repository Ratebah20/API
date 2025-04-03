# Étape 3 : Personnalisation des Offres

## Objectif de cette étape

Cette étape vise à permettre au distributeur d'adapter les offres fournies par Orange selon ses besoins commerciaux spécifiques, tout en conservant une transparence totale sur les prix et les marges appliquées.

## Pourquoi personnaliser les offres ?

La personnalisation permet au distributeur :

- De mieux adapter les offres aux attentes de ses clients finaux.
- D'améliorer son positionnement commercial grâce à des offres attractives et différenciantes.
- D’ajuster librement les prix finaux proposés aux clients en ajoutant des frais additionnels.

## Paramètres personnalisables d’une offre

### 1. Nom (`name`)

Le distributeur peut modifier le nom par défaut de l'offre afin de refléter sa propre marque ou stratégie commerciale.

**Exemple :**
- Nom initial : `Topup 10 € avec données`
- Nom personnalisé : `Offre Vacances 10 €`

### 2. Frais additionnels (`distributor_fees` et `distributor_fees_type`)

Ces frais permettent au distributeur de définir une marge commerciale additionnelle sur la valeur de revente initiale.

- Frais fixes : montant précis ajouté au prix initial.
- Frais en pourcentage : pourcentage appliqué au prix initial.

**Exemple concret :**
- Valeur initiale : 10 €
- Avec frais fixes de 2 € : prix final de 12 €
- Avec frais de 10 % : prix final de 11 €

### 3. Métadonnées personnalisées (`metadata`)

Informations supplémentaires que le distributeur peut associer librement aux offres pour des besoins internes ou marketing.

**Exemple :**
- `"metadata": "Promo été 2025 limitée"`

## Exemple technique de personnalisation

Voici un exemple simplifié de requête API (PATCH) pour modifier une offre existante :

```json
PATCH /distributors/offers/{offer_id}
{
    "name" : "Mon offre personnalisée",
    "distributor_fees" : 10,
    "distributor_fees_type" : "percent",
    "metadata" : "Infos complémentaires personnalisées"
}
```

La personnalisation des offres permet au distributeur de combiner la flexibilité commerciale avec un contrôle précis de sa stratégie tarifaire.

