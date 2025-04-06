# Documentation Technique du Testeur d'API Orange Travel B2B

## Aperçu
Le testeur d'API est un outil intégré permettant aux développeurs d'interagir directement avec l'API Orange Travel B2B. Il offre une interface utilisateur interactive pour tester tous les endpoints disponibles, paramétrer les requêtes et visualiser les réponses.

## Fonctionnalités

- **Sélection d'endpoints** : Interface conviviale pour choisir parmi tous les endpoints disponibles
- **Paramétrage dynamique** : Champs générés automatiquement selon l'endpoint sélectionné
- **Authentification intégrée** : Utilisation du token d'accès stocké en session
- **Visualisation des réponses** : Affichage formaté des réponses JSON
- **Journalisation détaillée** : Console logs pour le débogage

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
