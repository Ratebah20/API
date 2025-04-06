# Documentation Technique du Testeur d'API Orange Travel B2B

## Aperçu
Le testeur d'API est un outil intégré permettant aux développeurs d'interagir directement avec l'API Orange Travel B2B. Il offre une interface utilisateur interactive pour tester tous les endpoints disponibles, paramétrer les requêtes et visualiser les réponses.

## Fonctionnalités

- **Sélection d'endpoints** : Interface conviviale pour choisir parmi tous les endpoints disponibles (100% de couverture)
- **Paramétrage dynamique** : Champs générés automatiquement selon l'endpoint sélectionné
- **Authentification intégrée** : Utilisation du token d'accès stocké en session
- **Visualisation des réponses** : Affichage formaté des réponses JSON avec code de statut
- **Journalisation détaillée** : Console logs pour le débogage
- **Validation des entrées** : Vérification des champs obligatoires avant envoi
- **Format de corps adaptable** : Support du format snake_case requis par l'API

## Endpoints disponibles

Le testeur d'API couvre l'ensemble des endpoints disponibles dans l'API Orange Travel B2B :

### Informations de base
- **Test de connexion** (`/live`) : Vérifie la disponibilité de l'API et ses informations de version
- **Liste des pays** (`/countries`) : Récupère la liste des pays avec leurs codes ISO, noms et préfixes téléphoniques
- **Liste des devises** (`/currencies`) : Récupère les devises disponibles avec taux de conversion

### Gestion des offres
- **Liste des offres** (`/distributors/offers`) : Récupère toutes les offres disponibles pour le distributeur
- **Détails d'une offre** (`/distributors/offers/{id}`) : Récupère les détails d'une offre spécifique
- **Personnaliser une offre** (`/distributors/offers/{id}` méthode PATCH) : Permet de modifier certains paramètres d'une offre

### Gestion des transactions
- **Liste des transactions** (`/distributors/transactions`) : Récupère l'historique des transactions filtré par date/statut
- **Créer une transaction** (`/distributors/transactions` méthode POST) : Crée une nouvelle transaction pour une offre
- **Détails d'une transaction** (`/distributors/transactions/{id}`) : Récupère les détails d'une transaction spécifique
- **Nombre de transactions** (`/distributors/transactions/count`) : Compte le nombre de transactions selon filtre

### Gestion des fournisseurs et eSIM
- **Liste des fournisseurs** (`/distributors/suppliers`) : Récupère la liste des fournisseurs disponibles
- **Statut d'une SIM/eSIM** (`/distributors/suppliers/{id}/simstatus`) : Vérifie le statut d'une carte SIM/eSIM
- **Consommations d'une SIM** (`/distributors/suppliers/{id}/usagebalances`) : Récupère les données de consommation
- **Statistiques globales** (`/distributors/suppliers/{id}/globalbalances`) : Récupère les statistiques globales

### Gestion des clés RSA
- **Récupérer clé publique** (`/distributors/keys` méthode GET) : Récupère la clé publique RSA actuelle
- **Configurer clé publique** (`/distributors/keys` méthode POST) : Définit une nouvelle clé publique RSA

## Architecture technique

### Côté Frontend

1. **Alpine.js** : Gestion de l'état et de l'interactivité de l'interface
   - État principal : variable `endpoint` dans le composant Alpine.js
   - Interaction avec les boutons via les directives `@click`

2. **JavaScript** : 
   - `getSelectedEndpoint()` : Détecte l'endpoint sélectionné dans l'interface
   - `getEndpointConfig()` : Construit la configuration pour une requête API
   - `executeApiTest()` : Exécute la requête vers le backend

3. **Structure HTML** :
   - Panneau de sélection d'endpoints (gauche)
   - Formulaire de paramètres (centre)
   - Affichage des résultats (droite)

### Côté Backend

1. **Flask Blueprint** : Routage des requêtes
   - `api_tester_bp` : Blueprint dédié au testeur d'API
   - Route `/api/test` : Point d'entrée centralisé pour tous les tests d'endpoints

2. **Paramétrage et Configuration** :
   - Mapping des endpoints dans `config.py`
   - Utilisation des variables d'environnement pour les informations sensibles

3. **Gestion des requêtes** :
   - Construction dynamique des URLs avec remplacement des paramètres de chemin
   - Transmission des méthodes HTTP, headers, paramètres et corps de requête
   - Journalisation détaillée pour le débogage

4. **Sécurité** :
   - Vérification de l'authentification via le token d'accès en session
   - Validation des données entrantes côté client et serveur

## Guide d'utilisation

### Prérequis

1. **Authentification** : Avant d'utiliser le testeur, vous devez vous authentifier en cliquant sur le bouton "S'authentifier".
2. **Compréhension des endpoints** : Consultez la documentation de l'API Orange Travel B2B pour comprendre les paramètres attendus pour chaque endpoint.

### Utilisation pas à pas

1. **Sélectionner un endpoint** :
   - Choisissez l'endpoint à tester dans le panneau de gauche
   - Les endpoints sont organisés par catégories pour faciliter la navigation

2. **Configurer les paramètres** :
   - Remplissez les champs du formulaire adapté à l'endpoint sélectionné
   - Les champs obligatoires sont marqués d'un astérisque (*)

3. **Exécuter la requête** :
   - Cliquez sur le bouton "Exécuter la requête"
   - Les résultats s'affichent dans le panneau de droite
   - La console du navigateur contient des informations supplémentaires pour le débogage

### Exemples d'utilisation

#### Test de connexion

Plus simple endpoint pour vérifier que l'API est en ligne et accessible :
1. Sélectionnez "Test de connexion"
2. Cliquez sur "Exécuter la requête"
3. Vérifiez que le statut est 200 et que la version de l'API est indiquée

#### Création d'une transaction

Point sensible nécessitant plusieurs paramètres :
1. Sélectionnez "Créer une transaction"
2. Saisissez les informations requises :
   - ID de l'offre (format UUID)
   - Informations du client (ID, nom, prénom, email, date de naissance)
3. Cliquez sur "Exécuter la requête"
4. Notez l'ID de transaction généré pour l'utiliser dans d'autres endpoints

## Conseils et bonnes pratiques

1. **Tests progressifs** : Commencez par tester les endpoints simples avant d'utiliser les endpoints complexes
2. **Vérification des données** : Testez d'abord avec la liste des offres avant de tenter de créer une transaction
3. **Format des paramètres** : Assurez-vous de respecter les formats attendus (UUID, dates au format YYYY-MM-DD, etc.)
4. **Débogage** : Utilisez la console du navigateur pour voir les détails des requêtes et réponses
5. **Indices visuels** : Les boutons d'endpoints actifs sont surlignés en orange pour indiquer la sélection actuelle

## Intégration avec le guide d'intégration

Le testeur d'API complète le guide d'intégration en 12 étapes en offrant un moyen pratique de tester les concepts expliqués dans la documentation. Pour chaque étape du guide d'intégration, vous pouvez utiliser le testeur d'API correspondant pour voir les résultats réels.

### Côté Backend

1. **Routes** :
   - `/api-tester` : Affichage de l'interface du testeur
   - `/api/test` : Endpoint pour traiter les requêtes de test

2. **Traitement** :
   - Validation du token d'authentification
   - Construction dynamique des URLs via le mapping de configuration
   - Transmission de la requête à l'API externe
   - Retour de la réponse au frontend

## Configuration des endpoints

Les endpoints sont définis dans le fichier `config.py` sous la clé `ENDPOINTS` :

```python
ENDPOINTS = {
    # Endpoints de base
    "countries": "countries",
    "live": "live",
    "currencies": "currencies",
    
    # Offres
    "offers": "distributors/offers",
    
    # Transactions
    "transactions": "distributors/transactions",
    "transactions_count": "distributors/transactions/count",
    
    # Fournisseurs et services
    "suppliers": "distributors/suppliers",
    "suppliers/simstatus": "distributors/suppliers/{supplier_id}/simstatus",
    "suppliers/usagebalances": "distributors/suppliers/{supplier_id}/usagebalances",
    "suppliers/globalbalances": "distributors/suppliers/{supplier_id}/globalbalances",
    
    # Gestion des clés de sécurité
    "keys": "distributors/keys"
}
```

## Résolution de problèmes

### Détection de l'endpoint sélectionné
Le code implémente trois stratégies de détection (par ordre de priorité) :
1. Récupération directe depuis le conteneur principal Alpine.js
2. Détection du bouton actif (orange) et extraction de son endpoint
3. Parcours de tous les éléments Alpine.js

### Construction des URLs
Les URLs sont construites selon le format :
```python
url = f"{base_url}/{api_endpoint}"
```

Cette méthode garantit la compatibilité avec l'API Orange Travel B2B.

## Exemples d'utilisation

1. **Tester la liste des pays** :
   - Sélectionner "Liste des pays" dans le panneau de gauche
   - Cliquer sur "Exécuter la requête"
   - La réponse apparaît dans le panneau de droite

2. **Tester le statut d'une SIM** :
   - Sélectionner "Statut d'une SIM/eSIM" 
   - Renseigner l'ID du fournisseur et l'ID de transaction
   - Cliquer sur "Exécuter la requête"

## Extensions futures

- Historique des requêtes
- Export des requêtes en format cURL, Python, JavaScript, etc.
- Sauvegarde des paramètres fréquemment utilisés
- Gestion des favoris pour les endpoints les plus utilisés
