# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:46:08 2025

@author: Destock-afric
"""

import csv
import random
from faker import Faker

# Initialisation de Faker pour générer des noms de produits et catégories aléatoires
fake = Faker()

# Générer 100 enregistrements de produits avec des données aléatoires
produits = []
for i in range(1, 101):
    produit = {
        'ID': i,
        'Nom': fake.word().capitalize(),  # Générer un nom de produit aléatoire
        'Catégorie': random.choice(['Catégorie 1', 'Catégorie 2', 'Catégorie 3']),  # Catégorie aléatoire
        'Prix': round(random.uniform(10, 100), 2)  # Prix aléatoire entre 10 et 100
    }
    produits.append(produit)

# Spécifier le nom du fichier CSV
nom_fichier = 'produits.csv'

# Écrire les données dans le fichier CSV
with open(nom_fichier, mode='w', newline='', encoding='utf-8') as fichier_csv:
    champs = ['ID', 'Nom', 'Catégorie', 'Prix']
    writer = csv.DictWriter(fichier_csv, fieldnames=champs)
    
    # Écrire l'en-tête du CSV
    writer.writeheader()
    
    # Écrire les 100 enregistrements dans le fichier CSV
    for produit in produits:
        writer.writerow(produit)

print(f"Le fichier {nom_fichier} a été créé avec 100 enregistrements.")
