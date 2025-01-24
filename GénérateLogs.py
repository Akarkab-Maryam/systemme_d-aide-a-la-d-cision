# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:28:44 2025

@author: Destock-afric
"""

import random
import faker

# Initialisation de Faker pour générer des données aléatoires
fake = faker.Faker()

# Créer un fichier pour enregistrer les données
with open("enregistrements.txt", "w") as f:
    for _ in range(100):
        # Génération de données aléatoires pour l'enregistrement
        fichier_type = random.choice(["Fichier de paiement", "Fichier de logs", "Fichier e-commerce", "Statuts des paiements"])
        date_creation = fake.date_this_decade().strftime('%Y-%m-%d')
        taille_fichier = random.randint(100, 10000)  # Taille en Ko
        status_paiement = random.choice(["Réussi", "Échoué", "En attente"])

        # Format de l'enregistrement
        enregistrement = f"Autres fichiers : {fichier_type} | Date de création : {date_creation} | Taille : {taille_fichier} Ko | Statut du paiement : {status_paiement}\n"

        # Écrire l'enregistrement dans le fichier
        f.write(enregistrement)

print("100 enregistrements ont été générés avec succès dans 'enregistrements.txt'.")
