import time
from datetime import datetime
import multiprocessing
import random
import requests

url = "http://localhost:3085/quantara/add/"


# Fonction temporaire qui envoie des données dans un fichier.
# Cette fonction sera remplacée par l'envoi de données à partir de fichiers journaux.
def ajouter_lignes_fichier(filename):
    while True:
        stamp = random.randint(10, 40)
        time.sleep(stamp)
        current_date1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = f"[Error],{current_date1}\n"
        with open(filename, "a") as file:
            file.write(ligne)
        print("Données ajoutées avec succès à ", current_date1)


## Fonction de vérification des nouvelles lignes :
def verifier_nouvelles_lignes(filename, interval, param):
    nb_lines_debut = compter_lignes(filename)

    while True:
        nb_lines_fin = compter_lignes(filename)
        try:
            if nb_lines_fin > nb_lines_debut:
                for i in range(interval):
                    current_date2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print("Nouvelle alerte à ", current_date2, ' ', i)

                    data = {"x": current_date2, "y": 1}

                    response = requests.post(url + param, json=data)
                    print("Réponse:", response.text)
                    time.sleep(1)
            else:
                data = {"x": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "y": 0}

                response = requests.post(url + param, json=data)
                print("Réponse:", response.text)
                time.sleep(1)

        except Exception as e:
            print("Erreur lors de l'envoi de la requête:", e)

        nb_lines_debut = nb_lines_fin


# Compter les lignes des fichiers
def compter_lignes(filename):
    with open(filename, "r") as file:
        nb_lines = sum(1 for lines in file)
    return nb_lines

if __name__ == "__main__":
    
    def Alert1():

            nom_fichier1 = "erreursAlert1.txt"

            processus_ajout1 = multiprocessing.Process(target=ajouter_lignes_fichier, args=(nom_fichier1,))
            processus_verification1 = multiprocessing.Process(target=verifier_nouvelles_lignes, args=(nom_fichier1, 10, "alert2"))

            processus_ajout1.start()
            processus_verification1.start()

            processus_ajout1.join()
            processus_verification1.join()
            print("alert1")



    def Alert2():
            nom_fichier2 = "erreursAlert2.txt"


            processus_ajout2 = multiprocessing.Process(target=ajouter_lignes_fichier, args=(nom_fichier2,))
            processus_verification2 = multiprocessing.Process(target=verifier_nouvelles_lignes, args=(nom_fichier2, 15, "alert2"))

            processus_ajout2.start()
            processus_verification2.start()

            processus_ajout2.join()
            processus_verification2.join()
            print("alert2")
        
