# Étape 2 : Compréhension des Entités Principales

## Objectif de cette étape

L'objectif de cette étape est de comprendre précisément les différentes entités manipulées par l'API Orange Travel B2B afin de réaliser efficacement les opérations techniques par la suite.

## Les entités principales

### 1. Produit

Le produit représente l'article disponible à la vente pour le client final. Il peut s'agir :

- D'une **recharge mobile (topup)** : pour ajouter du crédit, des données mobiles ou des minutes d'appel.
- D'une **eSIM** : une SIM dématérialisée activable directement depuis l’appareil du client final.

Chaque produit est fourni par Orange et associé à des informations prédéfinies telles que la zone de couverture, le fournisseur (Orange France, Orange Espagne, Welcome Travelers), et les caractéristiques techniques (validité, volume de données, etc.).

### 2. Offre

L'offre est une liaison commerciale entre un produit spécifique et le distributeur. Elle définit notamment :

- Le prix de revente fixé par Orange au distributeur (resell value).
- Les frais additionnels que le distributeur peut appliquer à ses clients.
- Les éventuelles métadonnées supplémentaires et personnalisables selon les besoins du distributeur.
- La quantité autorisée en stock (bucket) disponible pour le distributeur.

### 3. Transaction

La transaction représente une opération d'achat concrète effectuée par un client final via le distributeur. Elle est essentielle car elle :

- Permet d’enregistrer chaque opération de vente effectuée.
- Contient toutes les informations nécessaires pour l’exécution de la recharge ou la génération de l’eSIM.
- Facilite le suivi détaillé et précis des ventes réalisées par le distributeur.

## Fonctionnement global des entités

Le processus général implique que le distributeur consulte d’abord les offres disponibles, puis génère des transactions spécifiques lorsqu'un client effectue un achat. Chaque transaction est suivie et détaillée afin de garantir une traçabilité et une gestion simplifiée des opérations commerciales.

Cette compréhension claire des entités est essentielle pour aborder efficacement les étapes techniques suivantes.

