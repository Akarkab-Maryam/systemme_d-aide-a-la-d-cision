Objectif de projet : 
	Extraire des données depuis plusieurs sources (fichiers JSON, bases de données locales).
	Transformer les données
	Charger dans un entrepôt de données hébergé dans le cloud (par exemple, Google BigQuery ou Amazon Redshift)


	Description générale :
 Ce mini-projet vise à concevoir un Système d'Aide à la Décision (DSS) pour analyser les achats en ligne 

en utilisant un entrepôt de données (Data Warehouse) hébergé dans le cloud. L'objectif principal est 

d'extraire des données provenant de plusieurs sources, de les transformer, et de les charger dans un 

entrepôt cloud, puis de créer des rapports interactifs pour visualiser et analyser les performances des 

ventes, les comportements des clients, et les tendances du marché


2 -les sources de donnés : 

 Dans le cadre du développement d'un système d'aide à la décision, plusieurs fichiers de données ont été   

 générés pour simuler des scénarios réels. Les données des produits sont stockées dans un fichier produits.csv,
 
contenant des informations telles que l'identifiant du produit, son nom, sa catégorie, et son prix. Ces données

 ont été créées à l'aide du script GénérateCSV.py. De même, les informations relatives aux clients, comprenant

 l'identifiant du client, son nom, son pays, et la date d'inscription, sont centralisées dans clients.csv grâce à 

 un  script similaire. Pour les commandes, les données structurées sont regroupées dans 
FileJsonCommande.json, 

générées par generatJsonFile.py. Ces fichiers offrent une base essentielle pour effectuer des opérations ETL, 


alimenter un entrepôt de données, et réaliser des analyses avancées via des outils de Business Intelligence



