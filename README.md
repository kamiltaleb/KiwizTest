# SUMMER-BREAK
Ce projet est une application web permettant de gérer des transactions et de générer un rapport sur les revenus et les dépenses. Il utilise Flask pour la partie serveur, Pandas pour le traitement des données, et Flasgger pour la documentation Swagger.


## Prérequis

1. Python 
2. Pip 


## Instructions pour la configuration de l'environnement

1. Creer un environnement virtuel avec python -m virtualenv (nom ex:kiwiz) 
2. Activer l'environnement avec kiwiz\Scripts\activate
3. Installer les dépendances nécessaires : `pip install -r requirements.txt`.


## Exécuter le code

- Pour démarrer l'application : `python run.py`.
- Pour lancer les tests : `python -m unittest discover tests`.
- Pour consulter la documentation swagger, lancez http://127.0.0.1:5000/apidocs/

### Hypothèses
- Les colonnes sont dans l'ordre suivant : Date, Type, Montant, Mémo.


## Limitations de la solution

- La gestion des erreurs peut être améliorée, notamment pour les fichiers CSV mal formatés.
- La solution n'inclut pas de persistance de données, donc les données sont perdues à chaque redémarrage de l'application.
- Le format de la date n'est pas validé.


## Évolutions futures

- Ajouter une persistance des données via une base de données.
- Améliorer l'interface avec des fonctionnalités supplémentaires.
- Ajouter des tests plus complets et une validation plus robuste.



