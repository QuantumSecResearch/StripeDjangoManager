StripeDjangoManager
StripeDjangoManager est une application web développée avec Django, intégrant des fonctionnalités de gestion des utilisateurs, des paiements en ligne, des abonnements récurrents et la gestion des fichiers statiques. L'application utilise Stripe pour les paiements, PostgreSQL pour la gestion de la base de données, et des outils comme Whitenoise et GitHub Actions pour la gestion des ressources statiques et l'automatisation des processus.

Fonctionnalités
Authentification des utilisateurs : Connexion via GitHub avec gestion des permissions et des groupes d'utilisateurs grâce à Django AllAuth.

Paiements en ligne : Intégration complète avec Stripe pour les paiements uniques et récurrents, avec gestion des abonnements et des produits.

Base de données PostgreSQL : Utilisation de Neon PostgreSQL pour la gestion et la synchronisation des données.

Automatisation des workflows : GitHub Actions pour la gestion des workflows, y compris la synchronisation des abonnements Stripe avec les données des utilisateurs.

Gestion des fichiers statiques : Utilisation de Whitenoise pour servir les fichiers statiques en production.

Interface moderne : Intégration de Tailwind CSS et Flowbite pour une interface utilisateur moderne et responsive.

Environnement de configuration : Gestion des variables d'environnement via Python Decouple pour simplifier la configuration et le déploiement.

Technologies Utilisées
Django : Framework Python pour la création de l'application web.

Stripe API : Gestion des paiements et abonnements.

PostgreSQL (Neon) : Base de données relationnelle pour la gestion des utilisateurs et des transactions.

GitHub Actions : Automatisation des workflows de développement et de production.

Whitenoise : Gestion des fichiers statiques en production.

Tailwind CSS & Flowbite : Frameworks CSS pour un design moderne et responsive.

Python Decouple : Gestion des variables d'environnement.

Déploiement
Cette application peut être déployée sur des plateformes cloud telles que Railway en suivant des étapes simples pour configurer les variables d'environnement et déployer l'application avec une intégration GitHub.

License
Ce projet est sous licence MIT.
