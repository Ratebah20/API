/**
 * Simulator.js - Script pour le simulateur mobile Orange Travel B2B
 * Ce script gère les interactions du simulateur et les transitions entre les différents écrans
 */

console.log('Chargement du fichier simulator.js...');

// Définition de la fonction globale pour Alpine.js - DOIT être accessible comme variable globale
window.mobileSimulator = function() {
    console.log('mobileSimulator() initialisé');
    
    // Définition d'un objet simple pour déboguer
        return {
        currentFlow: 'purchase',  // 'purchase' ou 'management'
        currentStep: 'start',     // étape actuelle dans le flux
        previousSteps: [],        // historique des étapes pour permettre de revenir en arrière
        apiInfo: {},              // informations sur l'API correspondant à l'étape actuelle
        
        // Initialisation
        init() {
            // Définir les informations d'API pour chaque étape
            this.apiInfo = {
                'purchase': {
                    'start': {
                        endpoint: 'Aucun appel API à cette étape',
                        description: 'Initialisation de l\'application.'
                    },
                    'access_travel': {
                        endpoint: 'POST /oauth/v3/token',
                        description: 'Authentification et obtention du token d\'accès.'
                    },
                    'list_countries': {
                        endpoint: 'GET /distributors/offers',
                        description: 'Récupération des offres disponibles, filtrées par pays.'
                    },
                    'select_country': {
                        endpoint: 'Manipulation côté client',
                        description: 'Aucun appel API, filtrage des données déjà reçues.'
                    },
                    'select_offer': {
                        endpoint: 'GET /distributors/offers/{offer_id}',
                        description: 'Récupération des détails de l\'offre sélectionnée.'
                    },
                    'receive_esim': {
                        endpoint: 'POST /distributors/transactions',
                        description: 'Création d\'une transaction pour obtenir une eSIM.'
                    },
                    'decrypt_esim': {
                        endpoint: 'Utilisation de la clé privée',
                        description: 'Déchiffrement du code d\'activation à l\'aide de la clé privée du distributeur.'
                    },
                    'install_esim': {
                        endpoint: 'Redirection système',
                        description: 'Redirection vers les paramètres du téléphone pour installer le profil eSIM.'
                    },
                    'activate_esim': {
                        endpoint: 'Opération système',
                        description: 'Activation du profil eSIM installé sur l\'appareil.'
                    }
                },
                'management': {
                    'receive_profile': {
                        endpoint: 'Affichage des détails de l\'eSIM',
                        description: 'Informations sur le profil eSIM déjà installé.'
                    },
                    'my_esim': {
                        endpoint: 'Navigation interne',
                        description: 'Accès à la section de gestion des eSIM.'
                    },
                    'supplier_info': {
                        endpoint: 'GET /distributors/suppliers/{supplier_id}',
                        description: 'Récupération des informations sur le fournisseur de l\'eSIM.'
                    },
                    'esim_type': {
                        endpoint: 'Affichage des propriétés',
                        description: 'Affichage des caractéristiques spécifiques de l\'eSIM.'
                    },
                    'msisdn_info': {
                        endpoint: 'GET /distributors/suppliers/{supplier_id}/sims/{sim_id}',
                        description: 'Récupération du numéro MSISDN associé à l\'eSIM, si disponible.'
                    },
                    'usage_info': {
                        endpoint: 'GET /distributors/suppliers/{supplier_id}/usagebalances',
                        description: 'Consultation du solde de données et de la date d\'expiration.'
                    }
                }
            };
            
            // Écouter les changements d'étape pour mettre à jour les informations API
            this.$watch('currentStep', (value) => {
                this.updateApiInfo();
            });
            
            this.$watch('currentFlow', (value) => {
                this.updateApiInfo();
            });
        },
        
        // Mettre à jour les informations d'API en fonction de l'étape actuelle
        updateApiInfo() {
            const apiInfoElement = document.getElementById('api-info');
            if (apiInfoElement && this.apiInfo[this.currentFlow] && this.apiInfo[this.currentFlow][this.currentStep]) {
                const info = this.apiInfo[this.currentFlow][this.currentStep];
                document.getElementById('api-endpoint').textContent = info.endpoint;
                document.getElementById('api-description').textContent = info.description;
            }
        },
        
        // Naviguer vers une étape spécifique
        goToStep(step) {
            console.log('goToStep appelé avec step=', step);
            this.previousSteps.push(this.currentStep);
            this.currentStep = step;
            console.log('Nouvel état - currentStep:', this.currentStep, 'previousSteps:', this.previousSteps);
        },
        
        // Revenir à l'étape précédente
        goBack() {
            console.log('goBack appelé');
            if (this.previousSteps.length > 0) {
                this.currentStep = this.previousSteps.pop();
                console.log("Retour à l'étape:", this.currentStep);
            } else {
                console.log("Impossible de revenir en arrière: pas d'étapes précédentes");
            }
        },
        
        // Changer de flux et réinitialiser les étapes
        switchFlow(flow, initialStep) {
            console.log('switchFlow appelé avec flow=', flow, 'initialStep=', initialStep);
            this.currentFlow = flow;
            this.currentStep = initialStep;
            this.previousSteps = [];
            console.log('Flux changé, nouvel état - currentFlow:', this.currentFlow, 'currentStep:', this.currentStep);
        },
        
        // Obtenir la séquence des étapes pour le flux actuel
        getFlowSteps() {
            if (this.currentFlow === 'purchase') {
                return ['start', 'access_travel', 'list_countries', 'select_country', 'select_offer', 'receive_esim', 'decrypt_esim', 'install_esim', 'activate_esim'];
            } else {
                return ['receive_profile', 'my_esim', 'supplier_info', 'esim_type', 'msisdn_info', 'usage_info'];
            }
        },
        
        // Obtenir l'étape suivante dans le flux
        getNextStep() {
            const steps = this.getFlowSteps();
            const currentIndex = steps.indexOf(this.currentStep);
            if (currentIndex < steps.length - 1) {
                return steps[currentIndex + 1];
            }
            return null;
        },
        
        // Aller à l'étape suivante
        goToNextStep() {
            console.log("goToNextStep appelé");
            const nextStep = this.getNextStep();
            if (nextStep) {
                this.goToStep(nextStep);
                console.log("Passage à l'étape suivante:", nextStep);
            } else if (this.currentFlow === 'purchase') {
                // Si on est à la fin du flux d'achat, passer au flux de gestion
                this.switchFlow('management', 'receive_profile');
                console.log("Fin du flux d'achat, passage au flux de gestion");
            }
        }
    };
};

// Débogage - Vérification de l'existence de la fonction
console.log("Fin du chargement de simulator.js, fonction mobileSimulator disponible:", typeof window.mobileSimulator);

