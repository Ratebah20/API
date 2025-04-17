import os
import json
import subprocess
from flask_babel import Babel
from babel.messages.pofile import read_po, write_po
from babel.messages.mofile import write_mo
from babel.messages.catalog import Message

# Dictionnaire des traductions pour le guide d'intégration
translations = {
    # Titre et introduction
    "Guide d'intégration en 12 étapes": {
        "en": "12-Step Integration Guide"
    },
    "Ce guide interactif vous présente les 12 étapes nécessaires pour intégrer l'API Orange Travel B2B dans votre système. Chaque étape contient des explications détaillées et des exemples concrets.": {
        "en": "This interactive guide presents the 12 steps necessary to integrate the Orange Travel B2B API into your system. Each step contains detailed explanations and concrete examples."
    },
    
    # Boutons de navigation
    "Étapes 1-4 : Bases et configuration": {
        "en": "Steps 1-4: Basics and Configuration"
    },
    "Étapes 5-8 : Transactions et eSIM": {
        "en": "Steps 5-8: Transactions and eSIM"
    },
    "Étapes 9-12 : Suivi et gestion": {
        "en": "Steps 9-12: Monitoring and Management"
    },
    
    # Titres des sections
    "Bases et configuration": {
        "en": "Basics and Configuration"
    },
    "Transactions et eSIM": {
        "en": "Transactions and eSIM"
    },
    "Suivi et gestion": {
        "en": "Monitoring and Management"
    },
    
    # Section des ressources complémentaires
    "Ressources complémentaires": {
        "en": "Additional Resources"
    },
    "Testeur d'API": {
        "en": "API Tester"
    },
    "Essayez les endpoints directement depuis votre navigateur": {
        "en": "Try endpoints directly from your browser"
    },
    "Simulateur d'écrans mobiles": {
        "en": "Mobile Screen Simulator"
    },
    "Visualisez l'expérience utilisateur sur mobile": {
        "en": "Visualize the user experience on mobile"
    },
    
    # Étapes 1-4
    "Étape 1 : Base URL et vérifications initiales": {
        "en": "Step 1: Base URL and Initial Verifications"
    },
    "Utilisez systématiquement la Base URL suivante pour toutes les requêtes à l'API Orange Travel B2B Sandbox": {
        "en": "Always use the following Base URL for all requests to the Orange Travel B2B Sandbox API"
    },
    "Accédez au portail": {
        "en": "Access the portal"
    },
    "Créez un compte et validez votre email": {
        "en": "Create an account and validate your email"
    },
    "Souscrivez à l'offre Travel B2B API": {
        "en": "Subscribe to the Travel B2B API offer"
    },
    "Récupérez vos clés d'API dans la section 'Mes applications'": {
        "en": "Retrieve your API keys in the 'My Applications' section"
    },
    
    "Étape 2 : Compréhension des entités principales": {
        "en": "Step 2: Understanding the Main Entities"
    },
    "Pour intégrer efficacement l'API Orange Travel B2B, il est essentiel de comprendre les trois entités principales qui la composent.": {
        "en": "To effectively integrate the Orange Travel B2B API, it is essential to understand the three main entities that comprise it."
    },
    "Produit": {
        "en": "Product"
    },
    "L'article disponible à la vente pour le client final.": {
        "en": "The item available for sale to the end customer."
    },
    "Recharge mobile (topup) : crédit, données, minutes": {
        "en": "Mobile top-up (topup): credit, data, minutes"
    },
    "eSIM : SIM dématérialisée activable directement": {
        "en": "eSIM: digital SIM that can be activated directly"
    },
    "Fourni par Orange avec des informations prédéfinies": {
        "en": "Provided by Orange with predefined information"
    },
    "Associé à une zone de couverture, un fournisseur et des caractéristiques techniques": {
        "en": "Associated with a coverage area, a supplier, and technical characteristics"
    },
    "Offre": {
        "en": "Offer"
    },
    "La liaison commerciale entre un produit et le distributeur.": {
        "en": "The commercial link between a product and the distributor."
    },
    "Prix de revente fixé par Orange au distributeur": {
        "en": "Resale price set by Orange to the distributor"
    },
    "Frais additionnels personnalisables": {
        "en": "Customizable additional fees"
    },
    "Métadonnées supplémentaires personnalisables": {
        "en": "Customizable additional metadata"
    },
    "Stock disponible (bucket) pour le distributeur": {
        "en": "Available stock (bucket) for the distributor"
    },
    "Transaction": {
        "en": "Transaction"
    },
    "Une opération d'achat concrète effectuée par un client.": {
        "en": "A concrete purchase operation carried out by a customer."
    },
    "Enregistre chaque opération de vente": {
        "en": "Records each sales operation"
    },
    "Contient les informations pour l'exécution": {
        "en": "Contains information for execution"
    },
    "Facilite le suivi des ventes réalisées": {
        "en": "Facilitates tracking of completed sales"
    },
    "Permet la traçabilité des opérations": {
        "en": "Enables traceability of operations"
    },
    "Fonctionnement global": {
        "en": "Global Operation"
    },
    "Le processus général implique que le distributeur consulte d'abord les offres disponibles, puis génère des transactions spécifiques lorsqu'un client effectue un achat. Chaque transaction est suivie et détaillée pour garantir une traçabilité et une gestion simplifiée.": {
        "en": "The general process involves the distributor first consulting the available offers, then generating specific transactions when a customer makes a purchase. Each transaction is tracked and detailed to ensure traceability and simplified management."
    },
    "Principaux endpoints liés aux entités": {
        "en": "Main Endpoints Related to Entities"
    },
    "Récupérer les offres disponibles": {
        "en": "Retrieve available offers"
    },
    "Détails d'une offre spécifique": {
        "en": "Details of a specific offer"
    },
    "Créer une transaction": {
        "en": "Create a transaction"
    },
    "Lister les transactions": {
        "en": "List transactions"
    },
    "Détails d'une transaction": {
        "en": "Details of a transaction"
    },
    "Les recharges à la demande (topups) permettent d'ajouter du crédit, des données mobiles ou des minutes d'appel à un numéro de téléphone existant. Voici comment gérer les transactions de type topup.": {
        "en": "On-demand recharges (topups) allow adding credit, mobile data, or call minutes to an existing phone number. Here's how to manage topup transactions."
    },
    "Utilisez le flux client_credentials": {
        "en": "Use the client_credentials flow"
    },
    "Envoyez une requête POST à https://api.orange.com/oauth/v3/token": {
        "en": "Send a POST request to https://api.orange.com/oauth/v3/token"
    },
    "Incluez vos client_id et client_secret": {
        "en": "Include your client_id and client_secret"
    },
    "Stockez le token retourné (valide 1 heure)": {
        "en": "Store the returned token (valid for 1 hour)"
    },
    "Exemple de code": {
        "en": "Code example"
    },
    
    "Étape 3 : Personnalisation des offres": {
        "en": "Step 3: Customization of Offers"
    },
    "La personnalisation des offres permet au distributeur d'adapter les offres fournies par Orange selon ses besoins commerciaux spécifiques, tout en conservant une transparence totale sur les prix et les marges appliquées.": {
        "en": "Offer customization allows the distributor to adapt the offers provided by Orange according to their specific business needs, while maintaining full transparency on prices and applied margins."
    },
    "Pourquoi personnaliser les offres ?": {
        "en": "Why customize offers?"
    },
    "Mieux adapter les offres aux attentes des clients finaux": {
        "en": "Better adapt offers to end-customer expectations"
    },
    "Améliorer son positionnement commercial avec des offres différenciantes": {
        "en": "Improve commercial positioning with differentiated offers"
    },
    "Ajuster librement les prix finaux en ajoutant des frais additionnels": {
        "en": "Freely adjust final prices by adding additional fees"
    },
    "Paramètres personnalisables": {
        "en": "Customizable Parameters"
    },
    "Nom": {
        "en": "Name"
    },
    "Modifiez le nom par défaut de l'offre pour refléter votre marque ou stratégie commerciale.": {
        "en": "Modify the default name of the offer to reflect your brand or commercial strategy."
    },
    "Exemple :": {
        "en": "Example:"
    },
    "Nom initial: Topup 10 € avec données": {
        "en": "Initial name: Topup 10 € with data"
    },
    "Nom personnalisé: Offre vacances 10 €": {
        "en": "Customized name: Holiday Offer 10 €"
    },
    "Frais additionnels": {
        "en": "Additional Fees"
    },
    "Définissez une marge commerciale additionnelle sur la valeur de revente initiale.": {
        "en": "Define an additional commercial margin on the initial resale value."
    },
    "Types de frais": {
        "en": "Fee types"
    },
    "Frais fixes": {
        "en": "Fixed fee"
    },
    "montant précis ajouté au prix initial": {
        "en": "precise amount added to the initial price"
    },
    "Frais en pourcentage": {
        "en": "Percentage fee"
    },
    "pourcentage appliqué au prix initial": {
        "en": "percentage applied to the initial price"
    },
    "Exemple concret": {
        "en": "Concrete example"
    },
    "Valeur initiale": {
        "en": "Initial value"
    },
    "Avec frais fixe de 2 €": {
        "en": "With fixed fee of 2 €"
    },
    "prix final de 12 €": {
        "en": "final price of 12 €"
    },
    "Avec frais de 10 pour cent": {
        "en": "With 10 percent fee"
    },
    "prix final de 11 €": {
        "en": "final price of 11 €"
    },
    "Métadonnées personnalisées": {
        "en": "Custom Metadata"
    },
    "Informations supplémentaires associées librement aux offres pour des besoins internes ou marketing.": {
        "en": "Additional information freely associated with offers for internal or marketing needs."
    },
    "Exemple technique de personnalisation": {
        "en": "Technical Example of Customization"
    },
    "GET /countries - Liste des pays couverts": {
        "en": "GET /countries - List of covered countries"
    },
    "GET /currencies - Devises supportées": {
        "en": "GET /currencies - Supported currencies"
    },
    "Endpoints principaux": {
        "en": "Main endpoints"
    },
    "GET /offers - Liste des offres disponibles": {
        "en": "GET /offers - List of available offers"
    },
    "POST /transactions - Créer une transaction": {
        "en": "POST /transactions - Create a transaction"
    },
    "GET /transactions/{id} - Détails d'une transaction": {
        "en": "GET /transactions/{id} - Transaction details"
    },
    
    "Étape 4 : Gestion des prix": {
        "en": "Step 4: Price Management"
    },
    "La gestion des prix est un aspect crucial de l'intégration avec l'API Orange Travel B2B. Cette étape explique les différents types de prix et comment ils sont calculés.": {
        "en": "Price management is a crucial aspect of integration with the Orange Travel B2B API. This step explains the different types of prices and how they are calculated."
    },
    "Valeur affichée": {
        "en": "Display Value"
    },
    "Prix public indicatif qui peut être affiché au client final. Ce prix est une référence, mais le distributeur a la liberté de définir son propre prix de vente.": {
        "en": "Indicative public price that can be displayed to the end customer. This price is a reference, but the distributor has the freedom to define its own selling price."
    },
    "Valeur de revente (resell_value)": {
        "en": "Resale Value (resell_value)"
    },
    "Prix facturé au distributeur par Orange. C'est la base sur laquelle le distributeur peut ajouter ses propres frais pour déterminer le prix final.": {
        "en": "Price charged to the distributor by Orange. This is the basis on which the distributor can add its own fees to determine the final price."
    },
    "Calcul du prix final": {
        "en": "Calculating the Final Price"
    },
    "Exemple de calcul": {
        "en": "Calculation Example"
    },
    "Valeur de revente (définie par Orange)": {
        "en": "Resale value (defined by Orange)"
    },
    "Ajout de frais fixe de 2 €": {
        "en": "Addition of fixed fee of 2 €"
    },
    "Ou ajout de frais en pourcentage de 15 pour cent": {
        "en": "Or addition of percentage fee of 15 percent"
    },
    "Le prix final est celui qui sera facturé au client": {
        "en": "The final price is the one that will be charged to the customer"
    },
    "Exemple de réponse de l'API pour une offre avec les prix": {
        "en": "Example API response for an offer with prices"
    },
    "Points importants à retenir": {
        "en": "Important Points to Remember"
    },
    "La valeur de revente (resell_value) est fixée par Orange": {
        "en": "The resale value (resell_value) is set by Orange"
    },
    "Les frais additionnels sont à la discrétion du distributeur": {
        "en": "Additional fees are at the distributor's discretion"
    },
    "L'API fournit toujours les informations de prix dans la devise de référence (EUR)": {
        "en": "The API always provides price information in the reference currency (EUR)"
    },
    "Des taux de change sont disponibles pour afficher les prix en devises locales": {
        "en": "Exchange rates are available to display prices in local currencies"
    },
    "Pourquoi utiliser RSA ?": {
        "en": "Why use RSA?"
    },
    "Les codes d'activation d'eSIM sont des données sensibles": {
        "en": "eSIM activation codes are sensitive data"
    },
    "Le chiffrement RSA assure leur protection": {
        "en": "RSA encryption ensures their protection"
    },
    "Étapes de configuration": {
        "en": "Configuration steps"
    },
    "Générez une paire de clés RSA (2048 bits minimum)": {
        "en": "Generate an RSA key pair (2048 bits minimum)"
    },
    "Envoyez votre clé publique via POST /keys": {
        "en": "Send your public key via POST /keys"
    },
    "Conservez votre clé privée en sécurité": {
        "en": "Keep your private key secure"
    },
    
    # Étapes 5-8
    "Étape 5 : Gestion des recharges à la demande (Topup)": {
        "en": "Step 5: On-Demand Recharge Management (Topup)"
    },
    "Impémentez la gestion des recharges mobiles à la demande pour vos clients.": {
        "en": "Implement on-demand mobile recharge management for your customers."
    },
    "Appel API": {
        "en": "API Call"
    },
    "GET /offers avec pagination (page, perPage)": {
        "en": "GET /offers with pagination (page, perPage)"
    },
    "Filtrage possible par type (topup, esim, sim)": {
        "en": "Possible filtering by type (topup, esim, sim)"
    },
    "Traitement des résultats": {
        "en": "Processing results"
    },
    "Affichez les offres par catégorie": {
        "en": "Display offers by category"
    },
    "Stockez les IDs d'offres pour les transactions": {
        "en": "Store offer IDs for transactions"
    },
    "Mettez en cache les résultats (TTL recommandé: 1h)": {
        "en": "Cache results (recommended TTL: 1h)"
    },
    
    "Étape 6 : Créer une transaction": {
        "en": "Step 6: Create a Transaction"
    },
    "Implémentez le processus d'achat pour permettre à vos clients d'acquérir des offres.": {
        "en": "Implement the purchase process to allow your customers to acquire offers."
    },
    "Préparer les données": {
        "en": "Prepare the data"
    },
    "ID de l'offre (obligatoire)": {
        "en": "Offer ID (required)"
    },
    "ID utilisateur (recommandé pour le suivi)": {
        "en": "User ID (recommended for tracking)"
    },
    "Paramètres spécifiques selon le type d'offre": {
        "en": "Specific parameters depending on the offer type"
    },
    "Envoyer la requête": {
        "en": "Send the request"
    },
    "POST /transactions avec le token OAuth": {
        "en": "POST /transactions with the OAuth token"
    },
    "Format JSON pour le corps de la requête": {
        "en": "JSON format for the request body"
    },
    "Gérer la réponse": {
        "en": "Handle the response"
    },
    "Stockez l'ID de transaction retourné": {
        "en": "Store the returned transaction ID"
    },
    "Vérifiez le statut initial (généralement 'created')": {
        "en": "Check the initial status (usually 'created')"
    },
    
    "Étape 7 : Gérer les codes d'activation eSIM": {
        "en": "Step 7: Manage eSIM Activation Codes"
    },
    "Déchiffrez et présentez les codes d'activation eSIM à vos utilisateurs.": {
        "en": "Decrypt and present eSIM activation codes to your users."
    },
    "Récupérer les codes chiffrés": {
        "en": "Retrieve encrypted codes"
    },
    "GET /transactions/{id} après création réussie": {
        "en": "GET /transactions/{id} after successful creation"
    },
    "Les codes sont dans le champ 'encrypted_activation_code'": {
        "en": "Codes are in the 'encrypted_activation_code' field"
    },
    "Déchiffrement côté client": {
        "en": "Client-side decryption"
    },
    "Utilisez votre clé privée RSA pour déchiffrer": {
        "en": "Use your private RSA key to decrypt"
    },
    "Le résultat est un objet JSON avec les codes": {
        "en": "The result is a JSON object with the codes"
    },
    "Présentation à l'utilisateur": {
        "en": "Presentation to the user"
    },
    "Code QR pour installation facile": {
        "en": "QR code for easy installation"
    },
    "Instructions manuelles (code d'activation + confirmation)": {
        "en": "Manual instructions (activation code + confirmation)"
    },
    
    "Étape 8 : Implémenter le webhook de notification": {
        "en": "Step 8: Implement the Notification Webhook"
    },
    "Configurez un endpoint pour recevoir les mises à jour de statut des transactions.": {
        "en": "Configure an endpoint to receive transaction status updates."
    },
    "Créer l'endpoint webhook": {
        "en": "Create the webhook endpoint"
    },
    "Endpoint accessible publiquement (HTTPS obligatoire)": {
        "en": "Publicly accessible endpoint (HTTPS required)"
    },
    "Méthode POST acceptant du JSON": {
        "en": "POST method accepting JSON"
    },
    "Enregistrer l'URL": {
        "en": "Register the URL"
    },
    "Contactez le support Orange pour enregistrer votre URL": {
        "en": "Contact Orange support to register your URL"
    },
    "Traiter les notifications": {
        "en": "Process notifications"
    },
    "Vérifiez la signature dans l'en-tête X-Signature": {
        "en": "Check the signature in the X-Signature header"
    },
    "Mettez à jour le statut des transactions dans votre système": {
        "en": "Update transaction status in your system"
    },
    "Répondez avec un code 200 pour confirmer la réception": {
        "en": "Respond with a 200 code to confirm receipt"
    },
    
    # Étapes 9-12
    "Étape 9 : Vérifier le statut des transactions": {
        "en": "Step 9: Check Transaction Status"
    },
    "Implémentez un mécanisme pour suivre et afficher l'état des transactions.": {
        "en": "Implement a mechanism to track and display transaction status."
    },
    "Méthode pull (active)": {
        "en": "Pull method (active)"
    },
    "GET /transactions/{id} périodiquement": {
        "en": "GET /transactions/{id} periodically"
    },
    "Intervalle recommandé: 30s initialement, puis espacé": {
        "en": "Recommended interval: 30s initially, then spaced out"
    },
    "Statuts possibles": {
        "en": "Possible statuses"
    },
    "created: Transaction créée": {
        "en": "created: Transaction created"
    },
    "pending: En cours de traitement": {
        "en": "pending: Processing"
    },
    "ok: Réussie": {
        "en": "ok: Successful"
    },
    "ko: Échouée": {
        "en": "ko: Failed"
    },
    "expired: Expirée": {
        "en": "expired: Expired"
    },
    "Interface utilisateur": {
        "en": "User interface"
    },
    "Affichez le statut actuel de manière claire": {
        "en": "Display the current status clearly"
    },
    "Prévoyez des messages d'erreur explicites": {
        "en": "Provide explicit error messages"
    },
    
    "Étape 10 : Consulter les consommations": {
        "en": "Step 10: Check Usage"
    },
    "Permettez à vos utilisateurs de suivre leur consommation de données, minutes et SMS.": {
        "en": "Allow your users to track their data, minutes, and SMS usage."
    },
    "Récupérer les informations": {
        "en": "Retrieve information"
    },
    "GET /suppliers/usagebalances avec l'ID de transaction": {
        "en": "GET /suppliers/usagebalances with transaction ID"
    },
    "Alternative: utiliser l'ICCID si disponible": {
        "en": "Alternative: use ICCID if available"
    },
    "Données retournées": {
        "en": "Returned data"
    },
    "Données restantes (Mo/Go)": {
        "en": "Remaining data (MB/GB)"
    },
    "Minutes d'appel disponibles": {
        "en": "Available call minutes"
    },
    "SMS restants": {
        "en": "Remaining SMS"
    },
    "Date d'expiration": {
        "en": "Expiration date"
    },
    "Affichage utilisateur": {
        "en": "User display"
    },
    "Graphiques de consommation": {
        "en": "Usage graphs"
    },
    "Alertes de seuil (80%, 90%, 100%)": {
        "en": "Threshold alerts (80%, 90%, 100%)"
    },
    
    "Étape 11 : Implémenter les recharges": {
        "en": "Step 11: Implement Top-ups"
    },
    "Ajoutez la possibilité pour vos clients de recharger leurs forfaits existants.": {
        "en": "Add the ability for your customers to top up their existing plans."
    },
    "Types de recharge": {
        "en": "Top-up types"
    },
    "Recharge de données": {
        "en": "Data top-up"
    },
    "Extension de validité": {
        "en": "Validity extension"
    },
    "Crédit supplémentaire": {
        "en": "Additional credit"
    },
    "Processus de recharge": {
        "en": "Top-up process"
    },
    "Identifiez l'offre de recharge appropriée": {
        "en": "Identify the appropriate top-up offer"
    },
    "Créez une transaction avec l'ID de la SIM/eSIM": {
        "en": "Create a transaction with the SIM/eSIM ID"
    },
    "POST /transactions avec paramètre 'simId'": {
        "en": "POST /transactions with 'simId' parameter"
    },
    "Confirmez l'application de la recharge": {
        "en": "Confirm the application of the top-up"
    },
    
    "Étape 12 : Mettre en place le reporting": {
        "en": "Step 12: Set Up Reporting"
    },
    "Implémentez des outils de reporting pour suivre les ventes et l'utilisation.": {
        "en": "Implement reporting tools to track sales and usage."
    },
    "Collecte de données": {
        "en": "Data collection"
    },
    "GET /transactions avec filtres de date": {
        "en": "GET /transactions with date filters"
    },
    "GET /transactions_count pour les statistiques": {
        "en": "GET /transactions_count for statistics"
    },
    "GET /suppliers/globalbalances pour la consommation": {
        "en": "GET /suppliers/globalbalances for consumption"
    },
    "Rapports recommandés": {
        "en": "Recommended reports"
    },
    "Ventes quotidiennes/hebdomadaires/mensuelles": {
        "en": "Daily/weekly/monthly sales"
    },
    "Répartition par type d'offre": {
        "en": "Distribution by offer type"
    },
    "Taux de conversion et d'abandon": {
        "en": "Conversion and abandonment rates"
    },
    "Consommation moyenne par utilisateur": {
        "en": "Average consumption per user"
    },
    "Visualisation": {
        "en": "Visualization"
    },
    "Tableaux de bord interactifs": {
        "en": "Interactive dashboards"
    },
    "Exportation au format CSV/Excel": {
        "en": "Export in CSV/Excel format"
    },
    "Alertes sur seuils critiques": {
        "en": "Alerts on critical thresholds"
    },
    
    # Contenu manquant du guide
    "Test de connexion": {
        "en": "Connection Test"
    },
    "Vous pouvez facilement vérifier que votre connexion à l'API fonctionne avec l'endpoint": {
        "en": "You can easily verify that your API connection works with the endpoint"
    },
    "Cet endpoint vous permettra également de connaître la version de l'API.": {
        "en": "This endpoint will also let you know the API version."
    },
    "Requête": {
        "en": "Request"
    },
    "Réponse attendue": {
        "en": "Expected response"
    },
    "Documentation API": {
        "en": "API Documentation"
    },
    "Selon la documentation OpenAPI, cet endpoint est décrit comme": {
        "en": "According to the OpenAPI documentation, this endpoint is described as"
    },
    "dans le tag": {
        "en": "in the tag"
    },
    "Résolution d'erreurs courantes": {
        "en": "Common Error Resolution"
    },
    "Si vous obtenez une erreur 404 NOT FOUND, vérifiez que vous utilisez bien la base URL complète et correcte mentionnée ci-dessus.": {
        "en": "If you get a 404 NOT FOUND error, verify that you are using the complete and correct base URL mentioned above."
    },
    "Utilisation du token": {
        "en": "Token Usage"
    },
    "Pour chaque appel API, ajoutez l'en-tête suivant :": {
        "en": "For each API call, add the following header:"
    },
    "Sécurité": {
        "en": "Security"
    },
    "Ne partagez jamais vos identifiants client_id et client_secret. Stockez-les de manière sécurisée et ne les incluez pas dans le code côté client.": {
        "en": "Never share your client_id and client_secret credentials. Store them securely and do not include them in client-side code."
    },
    "Récupère toutes les offres disponibles pour votre compte distributeur.": {
        "en": "Retrieves all offers available for your distributor account."
    },
    "Paramètres :": {
        "en": "Parameters:"
    },
    "Numéro de page": {
        "en": "Page number"
    },
    "Nombre d'éléments par page": {
        "en": "Number of items per page"
    },
    "Type d'offre (topup, esim, sim)": {
        "en": "Offer type (topup, esim, sim)"
    },
    "Crée une nouvelle transaction pour l'achat d'une offre.": {
        "en": "Creates a new transaction for purchasing an offer."
    },
    "Corps de la requête :": {
        "en": "Request body:"
    },
    "ID de l'offre (obligatoire)": {
        "en": "Offer ID (required)"
    },
    "ID utilisateur pour le suivi (recommandé)": {
        "en": "User ID for tracking (recommended)"
    },
    "Informations supplémentaires (optionnel)": {
        "en": "Additional information (optional)"
    },
    "Récupère les détails complets d'une transaction spécifique.": {
        "en": "Retrieves the complete details of a specific transaction."
    },
    "Réponse :": {
        "en": "Response:"
    },
    "Statut de la transaction (created, pending, ok, ko, expired)": {
        "en": "Transaction status (created, pending, ok, ko, expired)"
    },
    "Date de création": {
        "en": "Creation date"
    },
    "Code d'activation chiffré (pour eSIM)": {
        "en": "Encrypted activation code (for eSIM)"
    },
    "Documentation complète": {
        "en": "Complete Documentation"
    },
    "Consultez la documentation OpenAPI complète pour découvrir tous les endpoints disponibles et leurs paramètres détaillés.": {
        "en": "Consult the complete OpenAPI documentation to discover all available endpoints and their detailed parameters."
    },
    "Schema OpenAPI": {
        "en": "OpenAPI Schema"
    },
    "Mon offre personnalisée": {
        "en": "My customized offer"
    },
    "percent": {
        "en": "percent"
    },
    "Infos complémentaires personnalisées": {
        "en": "Custom additional information"
    },
    "Europe 10 Go": {
        "en": "Europe 10 GB"
    },
    "value": {
        "en": "value"
    },
    "33612345678": {
        "en": "33612345678"
    },
    "Selon la documentation, la personnalisation de l'offre utilise le schema": {
        "en": "According to the documentation, offer customization uses the schema"
    },
    "qui définit les champs modifiables.": {
        "en": "which defines the editable fields."
    },
    "Requête d'authentification": {
        "en": "Authentication Request"
    },
    
    # Étape 4 - Éléments manquants
    "Génération d'une paire de clés RSA (exemple avec OpenSSL)": {
        "en": "Generating an RSA key pair (example with OpenSSL)"
    },
    "openssl genrsa -out private_key.pem 2048": {
        "en": "openssl genrsa -out private_key.pem 2048"
    },
    "openssl rsa -in private_key.pem -pubout -out public_key.pem": {
        "en": "openssl rsa -in private_key.pem -pubout -out public_key.pem"
    },
    "# Envoi de la clé publique à l'API": {
        "en": "# Sending the public key to the API"
    },
    "POST /keys": {
        "en": "POST /keys"
    },
    "Content-Type: application/json": {
        "en": "Content-Type: application/json"
    },
    "{ \"public_key\": \"-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...\\n-----END PUBLIC KEY-----\" }": {
        "en": "{ \"public_key\": \"-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...\\n-----END PUBLIC KEY-----\" }"
    },
    "Processus de déchiffrement": {
        "en": "Decryption Process"
    },
    "Lorsque vous recevez un code d'activation chiffré, vous devrez le déchiffrer avec votre clé privée. Ce processus se fait entièrement côté client pour garantir la sécurité des données.": {
        "en": "When you receive an encrypted activation code, you will need to decrypt it with your private key. This process takes place entirely on the client side to ensure data security."
    },
    "Security": {
        "en": "Security"
    },
    "Ne partagez JAMAIS votre clé privée": {
        "en": "NEVER share your private key"
    },
    "Stockez-la dans un environnement sécurisé": {
        "en": "Store it in a secure environment"
    },
    "Prévoyez une procédure de rotation des clés": {
        "en": "Plan a key rotation procedure"
    },
    "Utilisez une longueur de clé d'au moins 2048 bits": {
        "en": "Use a key length of at least 2048 bits"
    },
    
    # Étapes 5-8 - Éléments manquants
    "Pour créer une transaction de recharge, vous devez fournir l'identifiant de l'offre et le numéro de téléphone du client final (MSISDN) dans la requête.": {
        "en": "To create a top-up transaction, you must provide the offer ID and the end customer's phone number (MSISDN) in the request."
    },
    "Points importants": {
        "en": "Important points"
    },
    "Vérifiez toujours le stock disponible (bucket) avant de créer une transaction": {
        "en": "Always check available stock (bucket) before creating a transaction"
    },
    "Assurez-vous que le numéro MSISDN est au format international (ex: 33612345678 pour la France)": {
        "en": "Make sure the MSISDN number is in international format (e.g.: 33612345678 for France)"
    },
    "Le statut de la transaction indiquera si la recharge a été effectuée avec succès": {
        "en": "The transaction status will indicate if the top-up was successful"
    },
    "Réponse de l'API": {
        "en": "API Response"
    },
    "La réponse contient toutes les informations sur la transaction créée, y compris son statut et les détails de la recharge effectuée.": {
        "en": "The response contains all information about the created transaction, including its status and details of the completed top-up."
    },
    "Exemple de réponse": {
        "en": "Response example"
    },
    
    "Étape 6 : Gestion sécurisée des eSIM": {
        "en": "Step 6: Secure eSIM Management"
    },
    "Les codes d'activation des eSIM sont des données sensibles qui doivent être protégées. L'API Orange Travel B2B utilise le chiffrement RSA pour sécuriser ces codes, et seul le distributeur peut les déchiffrer avec sa clé privée.": {
        "en": "eSIM activation codes are sensitive data that must be protected. The Orange Travel B2B API uses RSA encryption to secure these codes, and only the distributor can decrypt them with their private key."
    },
    "Génération des clés RSA": {
        "en": "RSA Key Generation"
    },
    "Première étape : générer une paire de clés RSA (clé privée et clé publique).": {
        "en": "First step: generate an RSA key pair (private key and public key)."
    },
    "# Génération d'une paire de clés RSA de 4096 bits": {
        "en": "# Generation of a 4096-bit RSA key pair"
    },
    "Important": {
        "en": "Important"
    },
    "La clé privée ne doit JAMAIS être partagée ou exposée. Conservez-la dans un emplacement sécurisé. Seule la clé publique est transmise à Orange via l'API.": {
        "en": "The private key should NEVER be shared or exposed. Keep it in a secure location. Only the public key is transmitted to Orange via the API."
    },
    "Enregistrement de la clé publique": {
        "en": "Registering the Public Key"
    },
    "Transmettez votre clé publique à l'API Orange Travel B2B pour qu'elle soit utilisée pour le chiffrement des codes d'activation eSIM.": {
        "en": "Transmit your public key to the Orange Travel B2B API to be used for encrypting eSIM activation codes."
    },
    "Remarque": {
        "en": "Note"
    },
    "Vous pouvez utiliser le paramètre": {
        "en": "You can use the parameter"
    },
    "avec la valeur": {
        "en": "with the value"
    },
    "si votre clé publique est encodée en base64.": {
        "en": "if your public key is base64 encoded."
    },
    
    "Étape 7 : Transaction eSIM": {
        "en": "Step 7: eSIM Transaction"
    },
    "Une fois que vous avez configuré votre clé publique, vous pouvez créer des transactions eSIM. Contrairement aux transactions de topup, les transactions eSIM ne nécessitent pas de paramètre MSISDN.": {
        "en": "Once you have configured your public key, you can create eSIM transactions. Unlike topup transactions, eSIM transactions do not require an MSISDN parameter."
    },
    "Création d'une transaction eSIM": {
        "en": "Creating an eSIM Transaction"
    },
    "La requête pour une transaction eSIM est plus simple que pour une recharge, car seul l'identifiant de l'offre est requis.": {
        "en": "The request for an eSIM transaction is simpler than for a top-up, as only the offer ID is required."
    },
    "Réponse avec code d'activation chiffré": {
        "en": "Response with Encrypted Activation Code"
    },
    "La réponse contient toutes les informations sur la transaction eSIM, y compris le code d'activation chiffré avec votre clé publique RSA.": {
        "en": "The response contains all information about the eSIM transaction, including the activation code encrypted with your RSA public key."
    },
    "Déchiffrement du code d'activation": {
        "en": "Decryption of the Activation Code"
    },
    "Vous devez déchiffrer le code d'activation en utilisant votre clé privée.": {
        "en": "You must decrypt the activation code using your private key."
    },
    "# Déchiffrement avec la clé privée": {
        "en": "# Decryption with the private key"
    },
    "Le code d'activation déchiffré doit être transmis au client final de manière sécurisée. Il permettra d'installer l'eSIM sur son appareil. Le code ressemble généralement à \"LPA:1$smdp.provider.com$ACTIVATION-CODE\".": {
        "en": "The decrypted activation code must be transmitted to the end customer securely. It will allow them to install the eSIM on their device. The code typically looks like \"LPA:1$smdp.provider.com$ACTIVATION-CODE\"."
    },
    
    "Étape 8 : Vérification d'identité KYC": {
        "en": "Step 8: KYC Identity Verification"
    },
    "KYC (Know Your Customer) est un processus obligatoire pour certains produits eSIM et SIM. Ce processus permet de vérifier l'identité du client final et est généralement requis dans les 30 jours suivant l'achat.": {
        "en": "KYC (Know Your Customer) is a mandatory process for certain eSIM and SIM products. This process verifies the identity of the end customer and is generally required within 30 days of purchase."
    },
    "Processus KYC": {
        "en": "KYC Process"
    },
    "Selon le fournisseur, le processus KYC peut varier. Les clients doivent être informés de la nécessité de compléter la vérification d'identité pour continuer à utiliser le service.": {
        "en": "Depending on the provider, the KYC process may vary. Customers must be informed of the need to complete identity verification to continue using the service."
    },
    "Orange France": {
        "en": "Orange France"
    },
    "URL de vérification KYC :": {
        "en": "KYC verification URL:"
    },
    "Welcome Travelers": {
        "en": "Welcome Travelers"
    },
    "Informations requises pour le KYC": {
        "en": "Information Required for KYC"
    },
    "Pièce d'identité valide (passeport, carte d'identité)": {
        "en": "Valid ID (passport, identity card)"
    },
    "Informations personnelles (nom, prénom, date de naissance)": {
        "en": "Personal information (last name, first name, date of birth)"
    },
    "Numéro de transaction ou autre identifiant fournit lors de l'achat": {
        "en": "Transaction number or other identifier provided at the time of purchase"
    },
    "Dans certains cas, une photo du visage (selfie) pour la vérification biométrique": {
        "en": "In some cases, a face photo (selfie) for biometric verification"
    },
    "Si le KYC n'est pas complété dans les délais requis (généralement 30 jours), la ligne peut être suspendue ou désactivée. Il est donc crucial d'informer vos clients de cette exigence lors de l'achat.": {
        "en": "If the KYC is not completed within the required timeframe (generally 30 days), the line may be suspended or deactivated. It is therefore crucial to inform your customers of this requirement at the time of purchase."
    },
    
    # Étapes 9-12 - Éléments manquants
    "Étape 9 : Statut de la SIM/eSIM": {
        "en": "Step 9: SIM/eSIM Status"
    },
    "Pour assurer un suivi efficace des SIM et eSIM, l'API Orange Travel B2B propose un endpoint dédié permettant de récupérer le statut actuel d'une carte SIM ou eSIM.": {
        "en": "To ensure efficient tracking of SIMs and eSIMs, the Orange Travel B2B API offers a dedicated endpoint for retrieving the current status of a SIM card or eSIM."
    },
    "SIM physiques et eSIM": {
        "en": "Physical SIMs and eSIMs"
    },
    "L'API Orange Travel B2B prend en charge deux types de cartes :": {
        "en": "The Orange Travel B2B API supports two types of cards:"
    },
    "Cartes SIM physiques": {
        "en": "Physical SIM cards"
    },
    "Cartes traditionnelles qui doivent être insérées physiquement dans l'appareil": {
        "en": "Traditional cards that must be physically inserted into the device"
    },
    "eSIM": {
        "en": "eSIM"
    },
    "Cartes SIM électroniques intégrées directement dans l'appareil et activées à distance": {
        "en": "Electronic SIM cards integrated directly into the device and activated remotely"
    },
    "Certains états et opérations comme": {
        "en": "Some states and operations like"
    },
    "ou": {
        "en": "or"
    },
    "ne s'appliquent qu'aux eSIM": {
        "en": "only apply to eSIMs"
    },
    "tandis que d'autres comme": {
        "en": "while others like"
    },
    "s'appliquent aux deux types. Dans les exemples d'API ci-dessous, nous préciserons les différences d'utilisation quand elles existent.": {
        "en": "apply to both types. In the API examples below, we will specify the differences in usage when they exist."
    },
    "Vérification du statut": {
        "en": "Status Verification"
    },
    "Pour vérifier le statut, vous devez spécifier l'ID du fournisseur et l'ID de la transaction associée.": {
        "en": "To check the status, you must specify the supplier ID and the associated transaction ID."
    },
    "Pour les SIM physiques ou les eSIM récupérées par lot, vous pouvez utiliser le paramètre": {
        "en": "For physical SIMs or eSIMs retrieved in batches, you can use the parameter"
    },
    "au lieu de": {
        "en": "instead of"
    },
    "La réponse contient le statut de la SIM/eSIM ainsi que des informations complémentaires comme les dates d'activation et d'expiration.": {
        "en": "The response contains the status of the SIM/eSIM as well as complementary information such as activation and expiration dates."
    },
    "Valeurs possibles du statut": {
        "en": "Possible Status Values"
    },
    "free": {
        "en": "free"
    },
    "La SIM/eSIM n'est associée à aucun forfait": {
        "en": "The SIM/eSIM is not associated with any plan"
    },
    "tous types": {
        "en": "all types"
    },
    "available": {
        "en": "available"
    },
    "La carte est active et peut être utilisée normalement": {
        "en": "The card is active and can be used normally"
    },
    "not installed": {
        "en": "not installed"
    },
    "L'eSIM n'a pas encore été installée sur un appareil": {
        "en": "The eSIM has not yet been installed on a device"
    },
    "eSIM uniquement": {
        "en": "eSIM only"
    },
    "uninstalled": {
        "en": "uninstalled"
    },
    "L'eSIM a été désinstallée de l'appareil initial": {
        "en": "The eSIM has been uninstalled from the initial device"
    },
    "suspended fraud": {
        "en": "suspended fraud"
    },
    "Suspendue pour suspicion de fraude": {
        "en": "Suspended for suspicion of fraud"
    },
    "suspended kyc default": {
        "en": "suspended kyc default"
    },
    "Suspendue car le KYC n'a pas été complété": {
        "en": "Suspended because KYC has not been completed"
    },
    "suspended by operator": {
        "en": "suspended by operator"
    },
    "Désactivée par le fournisseur": {
        "en": "Deactivated by the provider"
    },
    "suspended following a theft or loss": {
        "en": "suspended following a theft or loss"
    },
    "Désactivée suite à un vol ou une perte": {
        "en": "Deactivated following a theft or loss"
    },
    "expired": {
        "en": "expired"
    },
    "La période de validité est terminée": {
        "en": "The validity period has ended"
    },
    "revoked by operator": {
        "en": "revoked by operator"
    },
    "Révoquée par l'opérateur": {
        "en": "Revoked by the operator"
    },
    "sim swap": {
        "en": "sim swap"
    },
    "La SIM a été changée pour un nouvel appareil": {
        "en": "The SIM has been changed for a new device"
    },
    "SIM physique uniquement": {
        "en": "Physical SIM only"
    },
    "Conseil": {
        "en": "Tip"
    },
    "Effectuez des vérifications régulières de statut pour les cartes actives afin de détecter rapidement tout problème et d'informer vos clients en conséquence.": {
        "en": "Perform regular status checks for active cards to quickly detect any issues and inform your customers accordingly."
    },
    
    "Étape 10 : Comptage et statistiques des transactions": {
        "en": "Step 10: Transaction Counting and Statistics"
    },
    "Pour faciliter la génération de rapports et statistiques, l'API Orange Travel B2B propose un endpoint dédié au comptage des transactions selon divers critères de filtrage.": {
        "en": "To facilitate report generation and statistics, the Orange Travel B2B API offers an endpoint dedicated to counting transactions according to various filtering criteria."
    },
    "Comptage des transactions": {
        "en": "Transaction Counting"
    },
    "Cet endpoint permet d'obtenir rapidement le nombre total de transactions correspondant à des critères spécifiques sans avoir à récupérer et compter les transactions individuelles.": {
        "en": "This endpoint allows you to quickly get the total number of transactions corresponding to specific criteria without having to retrieve and count individual transactions."
    },
    "Paramètres de filtrage disponibles": {
        "en": "Available Filtering Parameters"
    },
    "startDate et endDate": {
        "en": "startDate and endDate"
    },
    "Période de comptage (format ISO)": {
        "en": "Counting period (ISO format)"
    },
    "status": {
        "en": "status"
    },
    "Filtrer par statut de transaction": {
        "en": "Filter by transaction status"
    },
    "offer": {
        "en": "offer"
    },
    "Filtrer par ID d'offre": {
        "en": "Filter by offer ID"
    },
    "supplier": {
        "en": "supplier"
    },
    "Filtrer par ID de fournisseur": {
        "en": "Filter by supplier ID"
    },
    "user": {
        "en": "user"
    },
    "Filtrer par ID d'utilisateur": {
        "en": "Filter by user ID"
    },
    "La réponse contient simplement le nombre total de transactions correspondant aux critères spécifiés.": {
        "en": "The response simply contains the total number of transactions matching the specified criteria."
    },
    "Conseil d'utilisation": {
        "en": "Usage Tip"
    },
    "Cet endpoint est particulièrement utile pour les tableaux de bord administratifs et les rapports périodiques. Vous pouvez l'utiliser pour afficher des statistiques par période, par type d'offre ou par statut sans avoir à charger toutes les données des transactions.": {
        "en": "This endpoint is particularly useful for administrative dashboards and periodic reports. You can use it to display statistics by period, by offer type, or by status without having to load all the transaction data."
    },
    
    "Étape 11 : Gestion des consommations": {
        "en": "Step 11: Usage Management"
    },
    "Pour permettre aux utilisateurs de suivre leur consommation de données, d'appels et de SMS, l'API Orange Travel B2B propose un endpoint dédié à la récupération des consommations restantes.": {
        "en": "To allow users to track their data, call, and SMS usage, the Orange Travel B2B API offers a dedicated endpoint for retrieving remaining usage."
    },
    "Disponibilité": {
        "en": "Availability"
    },
    "Cette fonctionnalité n'est disponible que pour les fournisseurs Welcome Travelers et Orange France. Les autres fournisseurs ne supportent pas cette fonctionnalité pour le moment.": {
        "en": "This feature is only available for Welcome Travelers and Orange France providers. Other providers do not support this feature at the moment."
    },
    "Récupération des consommations restantes": {
        "en": "Retrieving Remaining Usage"
    },
    "Pour récupérer les consommations, utilisez l'endpoint suivant en spécifiant l'ID du fournisseur et l'ID de la transaction.": {
        "en": "To retrieve usage, use the following endpoint by specifying the supplier ID and the transaction ID."
    },
    "De même que pour le statut, vous pouvez utiliser le paramètre": {
        "en": "As with status, you can use the parameter"
    },
    "pour les SIM physiques ou les eSIM récupérées par lot :": {
        "en": "for physical SIMs or eSIMs retrieved in batches:"
    },
    "La réponse contient des informations détaillées sur les consommations restantes, organisées par 'buckets' (enveloppes de consommation).": {
        "en": "The response contains detailed information about remaining usage, organized by 'buckets' (consumption packages)."
    },
    
    "La réponse contient des informations détaillées sur les consommations restantes, organisées par \"buckets\" (enveloppes de consommation).": {
        "en": "The response contains detailed information about remaining usage, organized by 'buckets' (consumption packages)."
    },
    "Conseil d'implémentation": {
        "en": "Implementation Tip"
    },
    "Intégrez cette fonctionnalité dans votre application pour permettre à vos clients de surveiller facilement leur consommation et d'éviter les mauvaises surprises. Vous pouvez également mettre en place des alertes lorsque les consommations atteignent certains seuils.": {
        "en": "Integrate this feature into your application to allow your customers to easily monitor their usage and avoid unpleasant surprises. You can also set up alerts when usage reaches certain thresholds."
    },
    "Fonctionnalité avancée": {
        "en": "Advanced Feature"
    },
    "En plus des consommations individuelles, vous pouvez également accéder aux": {
        "en": "In addition to individual usage, you can also access"
    },
    "statistiques globales de consommation": {
        "en": "global usage statistics"
    },
    "par région ou par pays. Cette fonctionnalité permet d'analyser les tendances et d'optimiser vos offres.": {
        "en": "by region or by country. This feature allows you to analyze trends and optimize your offers."
    },
    
    "Étape 11 : Gestion des transactions": {
        "en": "Step 11: Transaction Management"
    },
    "La gestion efficace des transactions est essentielle pour suivre les activités, générer des rapports et résoudre d'éventuels problèmes. L'API Orange Travel B2B propose plusieurs endpoints pour faciliter cette gestion.": {
        "en": "Efficient transaction management is essential for tracking activities, generating reports, and resolving potential issues. The Orange Travel B2B API offers several endpoints to facilitate this management."
    },
    "Liste des transactions": {
        "en": "Transaction List"
    },
    "Pour récupérer la liste des transactions, utilisez l'endpoint suivant. Vous pouvez utiliser divers filtres pour affiner les résultats.": {
        "en": "To retrieve the list of transactions, use the following endpoint. You can use various filters to refine the results."
    },
    "offset": {
        "en": "offset"
    },
    "Décalage pour la pagination": {
        "en": "Offset for pagination"
    },
    "limit": {
        "en": "limit"
    },
    "Nombre maximal de transactions à retourner": {
        "en": "Maximum number of transactions to return"
    },
    "startDate": {
        "en": "startDate"
    },
    "Date de début (format YYYY-MM-DD)": {
        "en": "Start date (YYYY-MM-DD format)"
    },
    "endDate": {
        "en": "endDate"
    },
    "Date de fin (format YYYY-MM-DD)": {
        "en": "End date (YYYY-MM-DD format)"
    },
    "Filtre par statut (created, pending, ok, ko, expired)": {
        "en": "Filter by status (created, pending, ok, ko, expired)"
    },
    "Filtre par identifiant d'offre": {
        "en": "Filter by offer ID"
    },
    "Filtre par identifiant de fournisseur": {
        "en": "Filter by supplier ID"
    },
    "Filtre par identifiant utilisateur": {
        "en": "Filter by user ID"
    },
    "Exemple de requête avec filtres :": {
        "en": "Example request with filters:"
    },
    "Détails d'une transaction spécifique": {
        "en": "Details of a Specific Transaction"
    },
    "Pour récupérer les détails complets d'une transaction spécifique, utilisez l'identifiant de la transaction.": {
        "en": "To retrieve the complete details of a specific transaction, use the transaction ID."
    },
    "Si vous avez besoin de connaître le nombre total de transactions sans récupérer les données complètes, utilisez l'endpoint dédié au comptage.": {
        "en": "If you need to know the total number of transactions without retrieving the complete data, use the dedicated counting endpoint."
    },
    "Bonnes pratiques": {
        "en": "Best Practices"
    },
    "Pour optimiser les performances, utilisez toujours des filtres appropriés et limitez le nombre de résultats si vous n'avez pas besoin de récupérer toutes les transactions. Pour les rapports, considérez l'utilisation du comptage et de la pagination.": {
        "en": "To optimize performance, always use appropriate filters and limit the number of results if you don't need to retrieve all transactions. For reports, consider using counting and pagination."
    },
    
    "Étape 12 : Gestion des erreurs": {
        "en": "Step 12: Error Management"
    },
    "Une gestion efficace des erreurs est essentielle pour assurer la robustesse de votre intégration avec l'API Orange Travel B2B. Cette dernière étape vous présente les différents types d'erreurs et comment les traiter.": {
        "en": "Effective error management is essential to ensure the robustness of your integration with the Orange Travel B2B API. This final step presents the different types of errors and how to handle them."
    },
    "Format des réponses d'erreur": {
        "en": "Error Response Format"
    },
    "Toutes les erreurs sont retournées avec un code HTTP approprié et un corps JSON contenant des informations détaillées.": {
        "en": "All errors are returned with an appropriate HTTP code and a JSON body containing detailed information."
    },
    "Principaux codes d'erreur HTTP": {
        "en": "Main HTTP Error Codes"
    },
    "401 Unauthorized": {
        "en": "401 Unauthorized"
    },
    "Problème d'authentification ou token expiré": {
        "en": "Authentication problem or expired token"
    },
    "Solution : Régénérer un token valide": {
        "en": "Solution: Regenerate a valid token"
    },
    "400 Bad Request": {
        "en": "400 Bad Request"
    },
    "Requête mal formée ou paramètres invalides": {
        "en": "Malformed request or invalid parameters"
    },
    "Solution : Vérifier les paramètres de la requête": {
        "en": "Solution: Check request parameters"
    },
    "404 Not Found": {
        "en": "404 Not Found"
    },
    "Ressource non trouvée (URL incorrecte ou ID invalide)": {
        "en": "Resource not found (incorrect URL or invalid ID)"
    },
    "Solution : Vérifier l'URL et les identifiants utilisés": {
        "en": "Solution: Check the URL and identifiers used"
    },
    "429 Too Many Requests": {
        "en": "429 Too Many Requests"
    },
    "Dépassement de la limite de requêtes": {
        "en": "Request limit exceeded"
    },
    "Solution : Implémenter un backoff exponentiel": {
        "en": "Solution: Implement exponential backoff"
    },
    "500 Internal Server Error": {
        "en": "500 Internal Server Error"
    },
    "Erreur interne du serveur": {
        "en": "Internal server error"
    },
    "Solution : Contacter le support d'Orange": {
        "en": "Solution: Contact Orange support"
    },
    "503 Service Unavailable": {
        "en": "503 Service Unavailable"
    },
    "Service temporairement indisponible": {
        "en": "Service temporarily unavailable"
    },
    "Solution : Réessayer plus tard avec un backoff": {
        "en": "Solution: Try again later with a backoff"
    },
    "Stratégies de gestion des erreurs": {
        "en": "Error Management Strategies"
    },
    "Validation préalable": {
        "en": "Prior validation"
    },
    "Validez vos données avant d'envoyer des requêtes": {
        "en": "Validate your data before sending requests"
    },
    "Gestion des 401": {
        "en": "Handling 401s"
    },
    "Implémentez un mécanisme de rafraîchissement automatique des tokens": {
        "en": "Implement an automatic token refresh mechanism"
    },
    "Retries avec backoff": {
        "en": "Retries with backoff"
    },
    "Pour les erreurs 429 et 503, implémentez un système de réessais avec délai croissant": {
        "en": "For 429 and 503 errors, implement a retry system with increasing delay"
    },
    "Logging": {
        "en": "Logging"
    },
    "Enregistrez toutes les erreurs pour faciliter le diagnostic": {
        "en": "Log all errors to facilitate diagnosis"
    },
    "Monitoring": {
        "en": "Monitoring"
    },
    "Mettez en place des alertes pour détecter les problèmes récurrents": {
        "en": "Set up alerts to detect recurring problems"
    },
    "Code d'exemple pour la gestion des erreurs": {
        "en": "Example code for error handling"
    },
    "La requête a été faite et le serveur a répondu avec un code d'état hors de la plage 2xx": {
        "en": "The request was made and the server responded with a status code outside the 2xx range"
    },
    "Problème d'authentification": {
        "en": "Authentication problem"
    },
    "Réessayer la requête avec le nouveau token": {
        "en": "Retry the request with the new token"
    },
    "Erreur de validation": {
        "en": "Validation error"
    },
    "Erreur de validation:": {
        "en": "Validation error:"
    },
    "Informer l'utilisateur du problème spécifique": {
        "en": "Inform the user of the specific problem"
    },
    "Trop de requêtes": {
        "en": "Too many requests"
    },
    "Réessayer la requête après le délai": {
        "en": "Retry the request after the delay"
    },
    "Autres erreurs": {
        "en": "Other errors"
    },
    "Erreur": {
        "en": "Error"
    },
    "Informer l'utilisateur qu'une erreur s'est produite": {
        "en": "Inform the user that an error has occurred"
    },
    "La requête a été faite mais aucune réponse n'a été reçue": {
        "en": "The request was made but no response was received"
    },
    "Pas de réponse du serveur": {
        "en": "No response from server"
    },
    "Vérifier la connectivité réseau": {
        "en": "Check network connectivity"
    },
    "Une erreur s'est produite lors de la configuration de la requête": {
        "en": "An error occurred during request configuration"
    },
    "Erreur de configuration:": {
        "en": "Configuration error:"
    },
    
    # Statistiques globales de consommation
    "Statistiques globales de consommation": {
        "en": "Global Usage Statistics"
    },
    "Pour analyser les tendances de consommation et optimiser vos offres, l'API Orange Travel B2B propose un endpoint permettant d'obtenir des statistiques globales de consommation par région ou par pays.": {
        "en": "To analyze consumption trends and optimize your offers, the Orange Travel B2B API provides an endpoint for obtaining global consumption statistics by region or country."
    },
    "Endpoint pour les statistiques globales": {
        "en": "Endpoint for Global Statistics"
    },
    "Contrairement à l'endpoint": {
        "en": "Unlike the endpoint"
    },
    "qui fournit des informations pour une carte SIM spécifique, cet endpoint permet d'obtenir des statistiques agrégées pour l'ensemble des cartes SIM/eSIM d'un fournisseur sur une période donnée.": {
        "en": "which provides information for a specific SIM card, this endpoint allows you to obtain aggregated statistics for all SIM/eSIM cards from a supplier over a given period."
    },
    "Paramètres disponibles": {
        "en": "Available Parameters"
    },
    "Identifiant du fournisseur": {
        "en": "Supplier identifier"
    },
    "Début de la période d'analyse (format ISO)": {
        "en": "Start of analysis period (ISO format)"
    },
    "Fin de la période d'analyse (format ISO)": {
        "en": "End of analysis period (ISO format)"
    },
    "Niveau d'agrégation (\"region\" ou \"country\")": {
        "en": "Aggregation level (\"region\" or \"country\")"
    },
    "Limitation": {
        "en": "Limitation"
    },
    "La période d'analyse ne peut pas dépasser 6 mois. Pour des statistiques sur une plus longue période, effectuez plusieurs appels avec des périodes successives.": {
        "en": "The analysis period cannot exceed 6 months. For statistics over a longer period, make multiple calls with successive periods."
    },
    "La réponse contient des statistiques détaillées par zone géographique, avec pour chaque zone la consommation de données, de voix et de SMS.": {
        "en": "The response contains detailed statistics by geographical area, with data, voice, and SMS consumption for each zone."
    },
    "Applications pratiques": {
        "en": "Practical Applications"
    },
    "Ces statistiques peuvent être utilisées pour :": {
        "en": "These statistics can be used to:"
    },
    "Analyser les tendances de consommation par zone géographique": {
        "en": "Analyze consumption trends by geographic area"
    },
    "Optimiser vos offres en fonction des habitudes d'utilisation": {
        "en": "Optimize your offers based on usage habits"
    },
    "Créer des rapports visuels pour vos clients": {
        "en": "Create visual reports for your customers"
    },
    "Anticiper les besoins en capacité et planifier vos achats": {
        "en": "Anticipate capacity needs and plan your purchases"
    },
    "Testez cet endpoint": {
        "en": "Test this endpoint"
    },
    "Vous pouvez tester cet endpoint directement dans notre": {
        "en": "You can test this endpoint directly in our"
    },
    "testeur d'API": {
        "en": "API tester"
    },
    "Sélectionnez l'endpoint": {
        "en": "Select the endpoint"
    },
    "et renseignez les paramètres requis.": {
        "en": "and fill in the required parameters."
    },
    
    # Autres
    "Voir plus": {
        "en": "See more"
    },
    "Copier": {
        "en": "Copy"
    },
    "Copié !": {
        "en": "Copied!"
    }
}

def update_existing_translation_file(filepath, new_translations, language):
    """Met à jour un fichier de traduction existant avec de nouvelles traductions."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            catalog = read_po(f)
        
        # Ajouter ou mettre à jour les messages
        for message_id, translations_dict in new_translations.items():
            if language in translations_dict:
                translation = translations_dict[language]
                if message_id in catalog:
                    # Mettre à jour un message existant
                    catalog[message_id].string = translation
                else:
                    # Ajouter un nouveau message
                    from babel.messages.catalog import Message
                    catalog[message_id] = Message(message_id, string=translation)
        
        # Enregistrer le catalogue mis à jour
        with open(filepath, 'wb') as f:
            write_po(f, catalog)
        
        return True
    except Exception as e:
        print(f"Erreur lors de la mise à jour du fichier de traduction {filepath}: {e}")
        return False

def compile_translations():
    """Compile les fichiers .po en fichiers .mo."""
    try:
        for lang in ['fr', 'en']:
            po_file_path = f"translations/{lang}/LC_MESSAGES/messages.po"
            mo_file_path = f"translations/{lang}/LC_MESSAGES/messages.mo"
            
            # Vérifier que le fichier .po existe
            if not os.path.exists(po_file_path):
                print(f"Fichier {po_file_path} introuvable.")
                continue
            
            print(f"Compilation du fichier {po_file_path}...")
            
            # Lire le fichier .po
            with open(po_file_path, 'r', encoding='utf-8') as f:
                catalog = read_po(f)
            
            # Écrire le fichier .mo
            with open(mo_file_path, 'wb') as f:
                write_mo(f, catalog)
            
            print(f"Fichier {mo_file_path} créé avec succès.")
        
        print("Compilation des traductions terminée.")
        return True
    except Exception as e:
        print(f"Erreur lors de la compilation des traductions: {e}")
        return False

def main():
    # Mettre à jour les fichiers de traduction pour le guide d'intégration
    print("Mise à jour des fichiers de traduction pour le guide d'intégration...")
    
    # Mettre à jour le fichier de traduction anglais
    en_po_file = "translations/en/LC_MESSAGES/messages.po"
    if os.path.exists(en_po_file):
        update_existing_translation_file(en_po_file, translations, 'en')
    
    # Mettre à jour le fichier de traduction français (identité)
    fr_po_file = "translations/fr/LC_MESSAGES/messages.po"
    if os.path.exists(fr_po_file):
        # Pour le français, nous utilisons les clés comme traductions (identité)
        fr_translations = {k: {"fr": k} for k in translations.keys()}
        update_existing_translation_file(fr_po_file, fr_translations, 'fr')
    
    # Compiler les traductions
    compile_translations()
    
    print("Traductions mises à jour et compilées.")
    print("Redémarrez votre serveur Flask pour appliquer les changements.")

if __name__ == "__main__":
    main()
