import time
from datetime import datetime
import multiprocessing

def addLineToFile(filename):
    while True:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = f"[Error],{current_date}\n"
        with open(filename, "a") as file:
            file.write(ligne)
        print("Ligne ajoutée dans le fichier.")
        time.sleep(10)

def verifier_augmentation_lignes(filename, intervalle):
    nb_lignes_debut = compter_lignes(filename)
    while True:
        time.sleep(intervalle)
        nb_lignes_fin = compter_lignes(filename)
        if nb_lignes_fin > nb_lignes_debut:
            print("Alerte: Le nombre de lignes a augmenté dans l'intervalle de temps spécifié.")
        nb_lignes_debut = nb_lignes_fin

def compter_lignes(filename):
    with open(filename, "r") as file:
        nb_lignes = sum(1 for line in file)
    return nb_lignes

if __name__ == "__main__":
    nom_fichier = "erreurs.csv"
    
    processus_ajout = multiprocessing.Process(target=addLineToFile, args=(nom_fichier,))
    processus_verification = multiprocessing.Process(target=verifier_augmentation_lignes, args=(nom_fichier, 10))

    processus_ajout.start()
    processus_verification.start()

    processus_ajout.join()
    processus_verification.join()
