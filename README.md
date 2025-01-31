# Objectif du projet

- **Extraire** des données depuis plusieurs sources (fichiers JSON, bases de données locales).  
- **Transformer**  :TRonsformer et nettoyer les données
- **Charger** dans un entrepôt de données hébergé dans le cloud (par exemple, Google BigQuery ou Amazon Redshift)
-  **Créations des dashbord  avec powerBI**
  

---

## Description générale

Ce mini-projet vise à concevoir un **Système d'Aide à la Décision (DSS)** pour analyser les achats en ligne en utilisant un entrepôt de données (**Data Warehouse**) hébergé dans le cloud.  

### Objectifs principaux :
1. Extraire des données provenant de plusieurs sources.  
2. Transformer les données.  
3. Charger les données dans un entrepôt cloud.  
4. Créer des **rapports interactifs** pour visualiser et analyser :  
   - Les performances des ventes,  
   - Les comportements des clients,  
   - Les tendances du marché.  

---

## Sources de données

Dans le cadre du développement du système d'aide à la décision, plusieurs fichiers de données ont été générés pour simuler des scénarios réels :  

- **Produits :**  
  Les données des produits sont stockées dans un fichier `produits.csv`, contenant :  
  - Identifiant du produit  
  - Nom  
  - Catégorie  
  - Prix  

  Ces données ont été créées à l'aide du script `GénérateCSV.py`.  

- **Clients :**  
  Les informations relatives aux clients sont centralisées dans `clients.csv`, contenant :  
  - Identifiant du client  
  - Nom  
  - Pays  
  - Date d'inscription  

  Généré à l'aide du script `GénérateCSV.py`.  

- **Commandes :**  
  Les données structurées des commandes sont regroupées dans `FileJsonCommande.json`, générées par le script `generatJsonFile.py`.  

Ces fichiers offrent une base essentielle pour effectuer des opérations **ETL**, alimenter un entrepôt de données et réaliser des analyses avancées via des outils de **Business Intelligence**.
