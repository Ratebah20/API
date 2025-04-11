# Guide d'implémentation du simulateur mobile Orange Travel B2B

Ce document détaille les étapes à suivre pour implémenter le simulateur de flux mobile pour l'API Orange Travel B2B, à destination des développeurs qui souhaitent comprendre comment intégrer l'API dans leurs applications mobiles.

## Objectif

Créer une simulation visuelle des flux d'utilisation de l'API Orange Travel B2B dans une application mobile, pour guider les développeurs dans leur intégration.

## 1. Création du template de base

1. **Partir du fichier `simulator.html` existant** et l'adapter pour représenter les deux flux décrits dans les diagrammes:
   - Flux d'achat et activation d'eSIM 
   - Flux de gestion de l'eSIM et réseau fournisseur

## 2. Structuration des écrans du simulateur

2. **Créer un conteneur pour chaque étape du flux** en utilisant Alpine.js pour gérer la navigation:
   ```html
   <div x-data="{ currentStep: 'start' }">
     <!-- Les différentes étapes seront affichées/masquées ici -->
   </div>
   ```

3. **Implémenter chaque écran du flux** avec les informations sur l'endpoint API correspondant:
   ```html
   <!-- Exemple pour l'écran de sélection d'offre -->
   <div x-show="currentStep === 'offer_selection'" class="mobile-screen">
     <div class="screen-header">Select an offer</div>
     <div class="api-info">
       <div class="endpoint">GET /distributors/offers</div>
       <div class="description">
         Cet endpoint renvoie la liste des offres disponibles.
       </div>
     </div>
     <button @click="currentStep = 'receive_esim'">Select offer</button>
   </div>
   ```

## 3. Annotations des points d'intégration API

4. **Annoter chaque écran avec les endpoints API correspondants** pour montrer clairement aux développeurs quelles API ils devront appeler à chaque étape:
   - Pour "Start Application" → Pas d'API spécifique
   - Pour "Accès Travel eSIM" → Authentification avec `/oauth/v3/token`
   - Pour "List Countries" → `GET /distributors/offers` avec filtrage par pays
   - Pour "Select a country" → Manipulation côté client
   - Pour "Select an offer" → `GET /distributors/offers/{offer_id}` pour les détails
   - Pour "Receive eSIM profile" → `POST /distributors/transactions`
   - Pour "Decrypt eSIM info" → Utilisation de la clé privée du distributeur
   - Pour "Install eSIM profile" → Redirection vers les paramètres du système
   - Pour "Activate eSIM profile" → Opération système
   - Pour "Receive eSIM profile" (flux 2) → Affichage des détails de l'eSIM
   - Pour "Go in MyeSIM" → Navigation interne
   - Pour "eSIM Supplier" → `GET /distributors/suppliers/{supplier_id}`
   - Pour "eSIM Type" → Affichage des propriétés 
   - Pour "eSIM MSISDN if exist" → `GET /distributors/suppliers/{supplier_id}/sims/{sim_id}`
   - Pour "eSIM Remaining metadata" → `GET /distributors/suppliers/{supplier_id}/usagebalances`

## 4. Implémentation des transitions visuelles

5. **Ajouter des flèches et transitions** entre les écrans pour représenter le flux des opérations:
   ```html
   <div class="flow-arrow">
     <svg><!-- Flèche SVG --></svg>
     <div class="arrow-label">Appel API</div>
   </div>
   ```

## 5. Ajout des informations explicatives

6. **Pour chaque étape, ajouter une zone d'information** qui explique:
   - Quel endpoint API est utilisé
   - Quels paramètres sont nécessaires
   - Quel format de réponse attendre
   - Quelles sont les erreurs possibles
   - Comment traiter la réponse

## 6. Mise en place de la navigation entre les flux

7. **Créer des boutons pour naviguer entre les différents flux**:
   ```html
   <div class="simulator-controls">
     <button @click="startFlow('esim_purchase')">Démarrer flux d'achat eSIM</button>
     <button @click="startFlow('esim_management')">Démarrer flux de gestion eSIM</button>
   </div>
   ```

## 7. Stylisation de l'interface mobile

8. **Styliser l'interface pour qu'elle ressemble à une application mobile**:
   ```css
   .mobile-device {
     width: 320px;
     height: 568px;
     border-radius: 30px;
     border: 10px solid #333;
     position: relative;
     overflow: hidden;
     box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
   }
   ```

## 8. Finalisation et tests

9. **Vérifier que la simulation est conforme aux diagrammes** fournis
10. **S'assurer que toutes les étapes des flux sont clairement représentées**
11. **Tester la navigation entre les différentes étapes**

## 9. Documentation des endpoints utilisés

12. **Créer une section de référence à côté du simulateur** qui liste tous les endpoints utilisés dans les flux et comment ils s'intègrent:
    ```html
    <div class="api-reference">
      <h3>Endpoints utilisés dans ce flux</h3>
      <ul>
        <li><code>GET /distributors/offers</code> - Liste des offres</li>
        <li><code>POST /distributors/transactions</code> - Création de transaction</li>
        <!-- etc. -->
      </ul>
    </div>
    ```

## Code d'exemple pour le flux d'achat et activation d'eSIM

```html
<!-- Premier flux: Achat et activation d'eSIM -->
<div x-show="currentFlow === 'purchase'" class="flow-container">
  <!-- Étape 1: Démarrer l'application -->
  <div x-show="currentStep === 'start'" class="mobile-screen">
    <div class="screen-title">Start Application</div>
    <button @click="currentStep = 'access_travel'" class="primary-button">
      Démarrer
    </button>
    <div class="api-note">
      Aucun appel API à cette étape. Initialisation de l'application.
    </div>
  </div>

  <!-- Étape 2: Accès Travel eSIM -->
  <div x-show="currentStep === 'access_travel'" class="mobile-screen">
    <div class="screen-title">Accès Travel eSIM</div>
    <div class="api-box">
      <div class="api-endpoint">POST /oauth/v3/token</div>
      <div class="api-description">
        Authentification et obtention du token d'accès
      </div>
    </div>
    <button @click="currentStep = 'list_countries'" class="primary-button">
      Continuer
    </button>
  </div>

  <!-- Étape 3: Liste des pays -->
  <div x-show="currentStep === 'list_countries'" class="mobile-screen">
    <div class="screen-title">Liste des pays</div>
    <div class="api-box">
      <div class="api-endpoint">GET /distributors/offers</div>
      <div class="api-description">
        Récupération des offres disponibles, filtrées par pays
      </div>
    </div>
    <div class="country-list">
      <div class="country-item" @click="currentStep = 'select_country'">France</div>
      <div class="country-item" @click="currentStep = 'select_country'">Espagne</div>
      <div class="country-item" @click="currentStep = 'select_country'">Italie</div>
    </div>
  </div>

  <!-- Autres étapes du flux... -->
</div>
```

## Code d'exemple pour le flux de gestion de l'eSIM

```html
<!-- Second flux: Gestion de l'eSIM -->
<div x-show="currentFlow === 'management'" class="flow-container">
  <!-- Étape 1: Réception du profil eSIM -->
  <div x-show="currentStep === 'receive_profile'" class="mobile-screen">
    <div class="screen-title">Receive eSIM profile</div>
    <div class="esim-details">
      <img src="/static/images/esim-qr.png" alt="eSIM QR Code" class="esim-qr">
      <div class="esim-info">
        <div>ICCID: 89332410000123456789</div>
        <div>Valide jusqu'au: 31/12/2025</div>
      </div>
    </div>
    <button @click="currentStep = 'my_esim'" class="primary-button">
      Voir mon eSIM
    </button>
  </div>

  <!-- Étape 2: Accès à MyeSIM -->
  <div x-show="currentStep === 'my_esim'" class="mobile-screen">
    <div class="screen-title">My eSIM</div>
    <div class="api-box">
      <div class="api-endpoint">GET /distributors/suppliers/{supplier_id}/sims/{sim_id}</div>
      <div class="api-description">
        Récupération des détails de l'eSIM
      </div>
    </div>
    <div class="esim-card">
      <div class="esim-card-header">Europe Travel</div>
      <div class="esim-card-body">
        <div>10GB de données</div>
        <div>30 jours de validité</div>
        <div>Statut: Actif</div>
      </div>
    </div>
    <button @click="currentStep = 'supplier_info'" class="primary-button">
      Voir détails du fournisseur
    </button>
  </div>

  <!-- Autres étapes du flux... -->
</div>
```

## Ressources nécessaires

- **Framework Alpine.js** : Pour gérer les interactions et transitions entre écrans
- **CSS Tailwind** : Pour styliser rapidement l'interface
- **Font Awesome** ou équivalent : Pour les icônes (flèches, boutons, etc.)
- **Maquettes d'écrans mobiles** : Utiliser des templates pour représenter fidèlement un écran mobile

## Notes importantes

- Ce simulateur ne fait pas d'appels réels à l'API, il s'agit uniquement d'une visualisation du flux à suivre
- Les informations sur les endpoints sont destinées à guider les développeurs dans leur intégration
- La simulation doit être très claire sur la distinction entre les opérations côté client et les appels API
- Chaque écran doit avoir une annotation expliquant la partie correspondante de l'API à utiliser
