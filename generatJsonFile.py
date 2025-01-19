# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:40:28 2025

@author: Destock-afric
"""

import json
import random
from datetime import datetime, timedelta

# Listes d'exemples de données très étendues pour générer aléatoirement
produits = [
    f"P{i:03d}" for i in range(1, 101)  # Génère P001, P002, ..., P100
]

clients = [
    f"C{i:03d}" for i in range(1, 101)  # Génère C001, C002, ..., C100
]

statuts = [
    f"statut{i}" for i in range(1, 101)  # Génère statut1, statut2, ..., statut100
]

# Fonction pour générer une date aléatoire dans les 30 derniers jours
def generate_random_date():
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Générer un grand nombre de commandes (par exemple 5000 commandes)
commandes = []
for i in range(5000):  # Augmenté à 5000 commandes
    commande = {
        "id_commande": f"{random.randint(10000, 99999)}",  # ID commande aléatoire
        "id_client": random.choice(clients),  # Choisir un client aléatoire
        "id_produit": random.choice(produits),  # Choisir un produit aléatoire
        "quantite": random.randint(1, 10),  # Quantité aléatoire entre 1 et 10
        "date": generate_random_date(),  # Date aléatoire des 30 derniers jours
        "statut": random.choice(statuts)  # Statut aléatoire
    }
    commandes.append(commande)

# Spécifier le chemin du fichier JSON où les données seront enregistrées
file_path = r'C:\Users\Destock-afric\Desktop\EGua\FileJsonCommande.json' 

# Ouvrir le fichier en mode écriture et y enregistrer les données
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(commandes, json_file, ensure_ascii=False, indent=4)

print(f"Le fichier JSON des commandes a été généré avec {len(commandes)} commandes.")
