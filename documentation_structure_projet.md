# Structure du Projet API Travel Orange B2B

## Objectif
Développer un site web interactif pour l'API Orange Travel B2B en centralisant la logique sur le backend Flask et en utilisant un frontend léger.

## Structure générale

```
API_travel/
├── API/                       # Dossier principal
│   ├── app/                   # Application Flask
│   │   ├── __init__.py        # Initialisation de l'application
│   │   ├── routes/            # Routes de l'API
│   │   ├── services/          # Services métier
│   │   ├── models/            # Modèles de données
│   │   ├── templates/         # Templates Flask
│   │   │   ├── partials/      # Composants HTML réutilisables
│   │   │   │   ├── guide_etapes_1_4.html    # Partie 1 du guide
│   │   │   │   ├── guide_etapes_5_8.html    # Partie 2 du guide
│   │   │   │   └── guide_etapes_9_12.html   # Partie 3 du guide
│   │   ├── static/            # Fichiers statiques (CSS, JS)
│   │   └── utils/             # Utilitaires
│   ├── tests/                 # Tests unitaires et d'intégration
│   └── config.py              # Configuration de l'application
```

## To-Do Liste de Développement

### 1. Configuration de l'environnement (Jour 1)
- [x] Réorganiser la structure des fichiers
- [x] Migrer le fichier auth.py existant dans la nouvelle structure
- [x] Configurer les dépendances dans requirements.txt
- [x] Mettre en place le système de configuration

### 2. Backend : Développement des routes (Jour 2-3)
- [x] Structurer l'application en modules (Blueprint Flask)
- [x] Endpoint : Authentification (basé sur auth.py existant)
- [x] Endpoint : Gestion des offres
  - [x] Liste des offres
  - [x] Détails d'une offre
  - [x] Personnalisation d'offre
- [x] Endpoint : Gestion des transactions
  - [x] Création de transaction
  - [x] Liste des transactions
  - [x] Détails d'une transaction
- [x] Endpoint : Gestion des eSIM
  - [x] Gestion des clés RSA
  - [x] Statut des SIM/eSIM
  - [x] Gestion des consommations

### 3. Services métier (Jour 4-5)
- [x] Service : Gestion des clés RSA
  - [x] Génération de paires de clés
  - [x] Stockage sécurisé des clés privées
  - [x] Transmission des clés publiques à l'API Orange
- [x] Service : Flux de démonstration des 12 étapes
  - [x] Étape 1-3 : Base et compréhension des entités
  - [x] Étape 4-5 : Gestion des prix et recharges
  - [x] Étape 6-7 : Gestion des eSIM
  - [x] Étape 8-12 : Vérification d'identité et suivi
- [ ] Service : Démonstration des flux
  - [ ] Simulation de flux complet d'achat
  - [ ] Simulation d'activation d'eSIM

### 4. Frontend : Templates et Interface (Jour 6-8)
- [x] Structure de base des templates
  - [x] Layout principal
  - [x] Navigation
  - [x] Composants réutilisables
- [x] Intégration de Alpine.js et Tailwind CSS
- [x] Interface utilisateur pour les sections principales
  - [x] Page d'accueil explicative
  - [x] Guide d'intégration en 12 étapes
      - [x] Partie 1: Bases et configuration (Étapes 1-4)
      - [x] Partie 2: Transactions et eSIM (Étapes 5-8)
      - [x] Partie 3: Suivi et gestion (Étapes 9-12)
  - [x] Testeur d'API interactif
      - [x] Sélection dynamique des endpoints (100% de couverture de l'API)
      - [x] Génération de formulaires adaptés pour chaque endpoint
      - [x] Exécution des requêtes API en temps réel avec méthodes GET, POST, PATCH
      - [x] Affichage formaté des résultats avec code de statut et messages d'erreur
      - [x] Validation des champs obligatoires avant soumission
      - [x] Format de données adapté (snake_case) pour compatibilité avec l'API
      - [x] Documentation complète et guide d'utilisation avec exemples
  - [x] Simulateur d'écrans mobiles

### 5. Visualisations et démonstrations (Jour 9-10)
- [ ] Mise en place des visualisations de données
  - [ ] Diagrammes des flux de processus
  - [ ] Graphiques explicatifs des entités
- [x] Création des simulations mobiles
  - [x] Maquettes d'écrans mobiles
  - [x] Transitions entre les écrans
  - [ ] Démonstration interactive du parcours utilisateur

### 6. Sécurité et optimisation (Jour 11)
- [x] Mise en place des bonnes pratiques de sécurité
  - [x] Protection contre les attaques CSRF
  - [x] Validation des entrées
  - [x] Gestion sécurisée des clés RSA
- [ ] Optimisation des performances
  - [ ] Mise en cache des réponses API
  - [ ] Minification des ressources statiques

### 7. Documentation et tests (Jour 12-13)
- [x] Documentation API
  - [ ] Documentation auto-générée (Swagger/OpenAPI)
  - [x] Guide d'utilisation pour les développeurs
- [ ] Tests
  - [ ] Tests unitaires des services
  - [ ] Tests d'intégration des endpoints
  - [ ] Tests fonctionnels de l'interface

### 8. Déploiement et finalisation (Jour 14)
- [ ] Préparation au déploiement
  - [ ] Configuration de production
  - [ ] Instructions de déploiement
- [ ] Derniers ajustements et corrections de bugs

## Technologies à utiliser

### Backend
- **Framework**: Flask (basé sur l'existant)
- **Documentation API**: Swagger/OpenAPI
- **Gestion des clés**: Cryptography (bibliothèque Python)

### Frontend
- **Templating**: Jinja2 (intégré à Flask)
- **CSS**: Tailwind CSS
- **JavaScript**: Alpine.js
- **Graphiques**: Chart.js ou D3.js pour les visualisations
- **Simulation mobile**: CSS personnalisé + animations

## Stratégie de développement

1. **Approche itérative**: Développer par fonctionnalité, en commençant par étendre le fichier auth.py existant
2. **Priorité au backend**: Concentrer les efforts sur une API robuste avant de développer l'interface
3. **Documentation continue**: Documenter chaque composant au fur et à mesure du développement
4. **Tests systématiques**: Tester chaque fonctionnalité avant de passer à la suivante

## Points d'attention particuliers

1. **Gestion des clés RSA**: Porter une attention particulière à la sécurité du stockage et de l'utilisation des clés
2. **Expérience utilisateur**: Concevoir une interface intuitive malgré la complexité technique
3. **Performances**: Optimiser les appels API pour éviter les temps de chargement trop longs
4. **Documentation**: Maintenir une documentation claire pour faciliter la compréhension de l'API Orange Travel B2B
