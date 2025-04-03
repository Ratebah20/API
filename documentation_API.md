Documentation technique API Orange Travel B2B Sandbox

Cette documentation explique comment réaliser étape par étape une intégration complète avec l'API Orange Travel B2B Sandbox en vue d'effectuer une simulation technique complète.

Étape 1 : Base URL et Vérifications initiales

Utilisez systématiquement la Base URL suivante pour toutes les requêtes :

https://api.orange.com/travel-b2b-sandbox/v1/

Vérification en cas d'erreur :

Vérifiez la Base URL en cas d'erreur 404 NOT FOUND.

Étape 2 : Entités principales

Types d'API disponibles

Récupération des offres.

Création des transactions.

Consultation des transactions effectuées.

Produit

Un produit est fourni par Orange, associé à un fournisseur.

Offre

Associe un produit à un distributeur, avec possibilité de frais additionnels.

Étape 3 : Personnalisation des offres

Le distributeur peut personnaliser les paramètres suivants d'une offre :

Nom (name)

Frais supplémentaires (distributor_fees et distributor_fees_type)

Métadonnées supplémentaires (metadata)

Exemple de requête PATCH :

PATCH /distributors/offers/{offer_id}
{
    "name" : "Nom personnalisé",
    "distributor_fees" : 10,
    "distributor_fees_type" : "percent",
    "metadata" : "Information supplémentaire"
}

Étape 4 : Gestion des prix

Valeur affichée : Prix public indicatif.

Valeur de revente : Prix facturé au distributeur.

Le distributeur peut ajouter des frais additionnels.

Étape 5 : Gestion des recharges à la demande (Topup)

Requête minimale pour une transaction topup :

POST /distributors/transactions
{
    "offer_id": "id_offre",
    "parameters": { "msisdn": "numéro_mobile" }
}

Vérification du stock disponible (bucket).

Réponse claire (succès ou échec).

Étape 6 : Gestion sécurisée des eSIM

Génération des clés RSA :

openssl genrsa -out distributor_private.pem 4096
openssl rsa -in distributor_private.pem -pubout -out distributor_public.pem

Transmettre la clé publique à Orange.

Conserver précieusement la clé privée.

Ajouter ou mettre à jour la clé publique :

POST /distributors/keys
{
  "public_key": "clé publique RSA"
}

Étape 7 : Transaction eSIM

Requête minimale pour une transaction eSIM :

POST /distributors/transactions
{
    "offer_id": "id_offre_esim"
}

L'activation code reçu est chiffré avec la clé publique RSA fournie par le distributeur. Décoder et déchiffrer cet activation code avant usage.

Étape 8 : Vérification d'identité KYC

Obligatoire sous 30 jours après achat.

URLs spécifiques :

Orange France : travel.orange.com/fr/orange-holidays

Welcome Travelers : travel.orange.com/fr/welcome-travelers

Étape 9 : Statut de la SIM/eSIM

Vérifier le statut d'une SIM ou eSIM :

GET /distributors/suppliers/{supplier_id}/simstatus?transaction={trx_id}

Réponse avec statut détaillé (activé, suspendu, expiré...).

Étape 10 : Gestion des consommations

Récupérer les consommations restantes (Welcome Travelers et Orange France uniquement) :

GET /distributors/suppliers/{supplier_id}/usagebalances?transaction={trx_id}

Réponse détaillée sur les consommations restantes (data, appels, SMS).

Étape 11 : Gestion des transactions

Liste des transactions :

Récupération avec filtres possibles (dates, statut, offre, utilisateur).

GET /distributors/transactions

Détails d'une transaction spécifique :

GET /distributors/transactions/{transaction_id}

Étape 12 : Gestion des erreurs

Traiter les réponses HTTP :

401 Unauthorized : gérer la génération des tokens JWT.

400 Bad Request : vérifier la requête (format, headers, paramètres).

Respectez ces étapes pour assurer une intégration robuste et efficace avec l'API Orange Travel B2B Sandbox.