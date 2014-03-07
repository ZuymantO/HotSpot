HotSpot
=======

Projet de Fouille Master 2 Paris Diderot 2013/2014



Install
=======

Ce programme nécessite quelques modules de bases pour son fonctionnement

Une base de donnée mongodb, avec le server mongod en fonctionnement
(penser à créer le dossier /data/db)

Les librairies suivantes sont supposées présentes sur la machine exécutant le programme

string
pymongo (http://docs.mongodb.org/manual/core/indexes/)
math
numpy
sklearn (instalable avec pip en recherchant scikit-learn, ne pas confondre avec scikit-learns)
la classe de Niniane Wang pour les calculs de Tf-idf (tfidf.py)

Interface Utilisateur
=====
Sur base d'article, choisir les articles qu'on apprécie, puis au fil du temps le programme vous recommande des articles similaires
Les articles choisi comme interessants fond alors objet de base de recommandation pour d'autres articles.
