# Guide du Simulateur Mobile Orange Travel B2B

## Vue d'ensemble

Le simulateur mobile Orange Travel B2B est un outil interactif conçu pour visualiser et tester l'expérience utilisateur des services eSIM sur un appareil mobile. Il offre deux flux principaux :

1. **Flux d'achat et d'activation d'eSIM** - Simule l'expérience complète d'achat d'un eSIM jusqu'à son activation
2. **Flux de gestion d'eSIM** - Simule l'interface de gestion des eSIM et les interactions avec les fournisseurs de réseau

## Architecture technique

### Technologies utilisées

- **Frontend** : HTML, CSS (Tailwind CSS), JavaScript avec Alpine.js v3
- **Backend** : Flask (Python)
- **Structure du projet** : Organisation modulaire avec séparation des composants

### Structure des fichiers

```
API_travel2/API/
├── app/
│   ├── templates/
│   │   ├── simulator.html       # Page principale du simulateur
│   │   ├── base.html            # Template de base
│   ├── routes/
│   │   ├── main.py              # Routes pour le simulateur
│   ├── __init__.py              # Configuration Flask
├── static/
│   ├── css/                     # Styles CSS
│   ├── js/
│   │   ├── simulator.js         # Code JavaScript (déprécié)
│   ├── img/                     # Images utilisées dans le simulateur
```

## Implémentation technique

### État actuel

Le simulateur utilise Alpine.js v3 avec la méthode `Alpine.data()` pour gérer l'état et les interactions de l'interface. La navigation entre les différents écrans est entièrement contrôlée par JavaScript.

### Flux de données

1. L'utilisateur interagit avec les boutons du simulateur
2. Alpine.js gère les changements d'état (currentFlow, currentStep)
3. Les écrans appropriés sont affichés/masqués en fonction de l'état
4. Les transitions entre les écrans simulent les appels API réels

### Méthodes principales

- `switchFlow(flow, initialStep)` : Change entre les flux d'achat et de gestion
- `goToStep(step)` : Navigue vers une étape spécifique dans le flux actuel
- `goBack()` : Retourne à l'étape précédente
- `goToNextStep()` : Passe à l'étape suivante dans la séquence

## Flux d'utilisation

### Flux d'achat et d'activation d'eSIM

1. **Écran de démarrage** : Introduction au service
2. **Accès eSIM Travel** : Choix du service eSIM
3. **Sélection du pays** : Choix du pays de destination
4. **Sélection de l'offre** : Choix du forfait eSIM
5. **Réception de l'eSIM** : Réception du profil eSIM
6. **Déchiffrement de l'eSIM** : Simulation du déchiffrement
7. **Installation de l'eSIM** : Processus d'installation
8. **Activation de l'eSIM** : Activation finale
9. **Transition** : Passage au flux de gestion

### Flux de gestion d'eSIM

1. **Réception du profil** : Informations initiales du profil
2. **Mon eSIM** : Vue d'ensemble de l'eSIM
3. **Informations fournisseur** : Détails sur le fournisseur
4. **Type d'eSIM** : Informations sur le type d'eSIM
5. **Information MSISDN** : Détails sur le numéro associé
6. **Solde d'utilisation** : État du crédit et de la consommation

## Résolution des problèmes techniques

Nous avons résolu plusieurs défis techniques lors du développement :

1. **Problème d'initialisation d'Alpine.js** : Résolu en utilisant la méthode officielle `Alpine.data()` au lieu d'une fonction globale.
2. **Erreurs de syntaxe JavaScript** : Corrigées en standardisant l'utilisation des guillemets et en améliorant la structure du code.
3. **Problèmes de chargement du fichier JavaScript** : Résolu en intégrant le code directement dans le fichier HTML.

## Prochaines étapes

1. **Enrichissement des simulations d'API** : Ajouter des réponses API plus détaillées
2. **Amélioration de l'UI/UX** : Ajouter des animations de transition
3. **Tests complets** : Tester tous les scénarios d'utilisation
4. **Documentation des API** : Lier chaque étape aux endpoints API correspondants
5. **Mode développeur** : Ajouter un mode affichant les détails des requêtes API simulées
