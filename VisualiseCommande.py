# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:03:45 2025

@author: maryam
"""

import json

# Chemin du fichier JSON
chemin_fichier = r'C:\Users\maryam\Downloads\FileJsonCommande.json'

# Lecture du fichier JSON
with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
    donnees = json.load(fichier)

# Affichage dans la console
print(json.dumps(donnees, indent=4, ensure_ascii=False))

# Affichage dans le Variable Explorer de Spyder
# Assurez-vous que le panneau "Variable Explorer" est ouvert dans Spyder
