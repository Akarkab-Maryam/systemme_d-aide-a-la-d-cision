import matplotlib.pyplot as plt

# Chemin du fichier
fichier_chemin = r"C:\Users\maryam\Downloads\enregistrements.txt"  # Assurez-vous que le fichier est à ce chemin

# Variables pour compter les paiements
paiements_reussis = 0
paiements_echoues = 0
paiements_attente = 0

try:
    # Lecture du fichier
    with open(fichier_chemin, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            # Vérifier les mots-clés indiquant le résultat des paiements
            if "réussi" in ligne.lower():
                paiements_reussis += 1
            elif "échoué" in ligne.lower():
                paiements_echoues += 1
            elif "en attente" in ligne.lower():
                paiements_attente += 1
except UnicodeDecodeError:
    print("Encodage UTF-8 invalide. Tentative avec latin-1...")
    with open(fichier_chemin, 'r', encoding='latin-1') as fichier:
        for ligne in fichier:
            if "réussi" in ligne.lower():
                paiements_reussis += 1
            elif "échoué" in ligne.lower():
                paiements_echoues += 1
            elif "en attente" in ligne.lower():
                paiements_attente += 1

# Affichage des résultats
print(f"Paiements réussis : {paiements_reussis}")
print(f"Paiements échoués : {paiements_echoues}")
print(f"Paiements en attente : {paiements_attente}")

# Création du graphique
categories = ['Réussites', 'Échecs', 'En attente']
valeurs = [paiements_reussis, paiements_echoues, paiements_attente]

plt.bar(categories, valeurs, color=['green', 'red', 'orange'])
plt.title("Statistiques des paiements")
plt.xlabel("Résultat")
plt.ylabel("Nombre de paiements")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
