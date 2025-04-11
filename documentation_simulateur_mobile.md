# Documentation du Simulateur Mobile Orange Travel B2B

## Introduction

Le simulateur mobile est un composant interactif permettant de visualiser l'expérience utilisateur final lors de l'utilisation des services Orange Travel B2B. Cette interface simule les différentes étapes qu'un utilisateur suivrait sur son appareil mobile pour accéder aux services de connectivité internationale proposés par Orange Travel.

## Objectifs du Simulateur

1. Démontrer visuellement le parcours utilisateur
2. Illustrer les cas d'usage principaux de l'API Orange Travel B2B
3. Aider les développeurs à comprendre le flux complet d'une transaction
4. Servir de référence pour l'intégration dans des applications mobiles réelles

## Flux Principaux du Simulateur

Le simulateur mobile comprend deux flux principaux, correspondant aux principaux cas d'usage de l'API Orange Travel B2B:

### 1. Flux d'Achat et Activation d'une eSIM

Ce flux simule l'expérience utilisateur complète depuis le démarrage de l'application jusqu'à l'activation d'une eSIM.

#### Étapes du flux:

1. **Démarrer l'Application**
   - L'utilisateur lance l'application mobile
   - L'interface affiche un bouton "Start Application"

2. **Accès aux Services Travel eSIM**
   - L'utilisateur accède à la section "Accès Travel eSIM"
   - Présentation des services de connectivité internationale

3. **Liste des Pays**
   - L'application affiche la liste des pays où les services sont disponibles
   - Ces informations sont récupérées via l'API `/distributors/offers` qui renvoie les offres par pays

4. **Sélection d'un Pays**
   - L'utilisateur sélectionne un pays de destination
   - L'application filtre les offres disponibles pour ce pays

5. **Sélection d'une Offre**
   - Présentation des différentes offres disponibles (durée, volume de données, prix)
   - L'utilisateur sélectionne l'offre qui lui convient
   - Ces informations sont récupérées via l'API `/distributors/offers/{offer_id}`

6. **Réception du Profil eSIM**
   - Après validation de l'achat, l'utilisateur reçoit le profil eSIM
   - Cette étape utilise l'API `/distributors/transactions` pour créer une transaction

7. **Déchiffrement des Informations eSIM**
   - L'application déchiffre le code d'activation reçu via l'API
   - Ce processus utilise la clé privée du distributeur pour déchiffrer le `activation_code`

8. **Installation du Profil eSIM**
   - Instructions guidant l'utilisateur pour installer le profil sur son appareil
   - Redirection vers les paramètres du téléphone

9. **Activation du Profil eSIM**
   - L'utilisateur active le profil eSIM installé
   - Confirmation de l'activation réussie

### 2. Flux de Gestion de l'eSIM et Réseau Fournisseur

Ce flux illustre comment l'utilisateur peut gérer son eSIM et se connecter au réseau du fournisseur.

#### Étapes du flux:

1. **Accès à la Section MyeSIM**
   - L'utilisateur accède à ses eSIMs actives
   - Vue d'ensemble des eSIMs disponibles

2. **Connexion au Réseau du Fournisseur**
   - Redirection vers la section Travel
   - L'application se connecte au réseau du fournisseur

3. **Demande d'Informations Personnelles**
   - Si nécessaire, collecte d'informations KYC (Know Your Customer)
   - Ces informations sont traitées via les API de vérification d'identité

4. **Informations sur le Fournisseur eSIM**
   - Affichage des détails du fournisseur de l'eSIM
   - Informations de support et de contact

5. **Type d'eSIM**
   - Présentation du type d'eSIM (data uniquement, voix+data, etc.)
   - Caractéristiques spécifiques de l'offre

6. **Vérification MSISDN**
   - Si disponible, affichage du numéro de téléphone associé
   - Ce numéro est récupéré via l'API `/distributors/suppliers/{supplier_id}/sims/{sim_id}`

7. **Métadonnées Restantes**
   - Affichage des informations complémentaires de l'eSIM:
     - Volume de données restant
     - Date d'expiration
     - Pays de couverture
   - Ces informations sont récupérées via l'API `/distributors/suppliers/{supplier_id}/usagebalances`

8. **Affichage des Informations dans la Section Travel**
   - L'ensemble des informations pertinentes est affiché dans l'interface utilisateur
   - Présentation claire des informations pour l'utilisateur final



## Intégration avec l'API Orange Travel B2B

Le simulateur mobile illustre l'utilisation des principaux endpoints de l'API:

- **/distributors/offers**: Récupération des offres disponibles
- **/distributors/transactions**: Création et gestion des transactions
- **/distributors/suppliers/{supplier_id}/sims/{sim_id}**: Informations sur les SIM/eSIM
- **/distributors/suppliers/{supplier_id}/usagebalances**: Soldes et consommation
- **/distributors/keys**: Gestion des clés RSA pour le déchiffrement des codes d'activation

## Implémentation Technique du Simulateur

Le simulateur est développé en utilisant:
- **HTML/CSS**: Pour la structure et le style de l'interface mobile
- **Alpine.js**: Pour la gestion des interactions et des transitions entre écrans
- **Tailwind CSS**: Pour le design responsive et l'apparence visuelle
- **Flask/Jinja2**: Pour l'intégration avec le backend et la génération des templates

### Structure des Fichiers

```
app/
├── templates/
│   ├── simulator.html       # Template principal du simulateur
│   └── partials/            # Composants réutilisables
├── static/
│   ├── css/                 # Styles spécifiques au simulateur
│   ├── js/                  # Logic JavaScript pour les transitions
│   └── images/              # Images et icônes utilisées dans le simulateur
└── routes/
    └── simulator.py         # Routes Flask pour le simulateur
```

## Guide d'Utilisation du Simulateur

1. Accédez à la section "Simulateur Mobile" depuis le menu principal
2. Sélectionnez un des scénarios disponibles (Achat de recharge, Activation eSIM)
3. Parcourez les différentes étapes du flux en cliquant sur les boutons d'action
4. Observez les informations affichées et les transitions entre les écrans
5. Utilisez les boutons de navigation en bas de l'écran pour revenir à l'accueil ou explorer d'autres sections

## Prochaines Évolutions

Le simulateur sera enrichi avec les fonctionnalités suivantes:
- Intégration de davantage d'animations et de transitions entre les écrans
- Ajout de nouveaux scénarios illustrant d'autres cas d'usage
- Amélioration de l'interactivité avec des formulaires fonctionnels
- Création d'un mode "pas à pas" avec explications détaillées de chaque étape
- Possibilité de tester les API réelles en environnement de sandbox

## Conclusion

Le simulateur mobile Orange Travel B2B offre une visualisation concrète et interactive des flux utilisateurs liés à l'utilisation des eSIM et des services de connectivité internationale. Il permet aux développeurs et aux partenaires de mieux comprendre l'expérience utilisateur final et d'optimiser leur intégration avec l'API Orange Travel B2B.
