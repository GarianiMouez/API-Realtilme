import time
from datetime import datetime
import multiprocessing
import random
import requests

url = "http://localhost:3085/quantara/add/alert1"


# Temporary function that sends data into a file. 
# This function will be replaced by sending data from log files.
def addlinesToFile(filename):
    while True:
        stamp=random.randint(10,40)
        time.sleep(stamp)
        current_date1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = f"[Error],{current_date1}\n"
        with open(filename, "a") as file:
            file.write(ligne)
        print("data added succesfuly in ",current_date1)
        

##Check function for alert : 
def check_new_lines(filename, interval):
    nb_lines_debut = compter_lines(filename)
    alert_envoyee = False
    while True:
        nb_lines_fin = compter_lines(filename)
        try:
            if nb_lines_fin > nb_lines_debut:
                for i in range(interval):
                    current_date2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print("Nouvelle alerte à ", current_date2, ' ', i)

                    data = {"x": current_date2, "y": 1}

                    response = requests.post(url, json=data)
                    print("Réponse:", response.text)
                    time.sleep(1)
            else:
                    data = {"x": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "y": 0}

                    response = requests.post(url, json=data)
                    print("Réponse:", response.text)
                    time.sleep(1)
                  
        except Exception as e:
            print("Erreur lors de l'envoi de la requête:", e)

        nb_lines_debut = nb_lines_fin


# def check_new_lines(filename, interval):
#     nb_lines_debut = compter_lines(filename)
#     alertSended=True
#     while True:

#         nb_lines_fin = compter_lines(filename)
#         try:
#             if nb_lines_fin > nb_lines_debut:
#                 for i in range(interval):
#                   current_date2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                   print("New alert in ",current_date2,' ',i)
                
                
#                   data = {"x": current_date2, "y": 1}
                  
#                   response = requests.post(url, json=data)
#                   print("Réponse:", response.text)
#                   time.sleep(1)
           
               
#             else:
#                 data = {"x": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "y": 0}
                
#                 response = requests.post(url, json=data)
#                 print("Réponse:", response.text)
#                 time.sleep(1)


        
#         except Exception as e:
#             print("Erreur lors de l'envoi de la requête:", e)

#         nb_lines_debut = nb_lines_fin
 




#count flies lines
def compter_lines(filename):
    with open(filename, "r") as file:
        nb_lines = sum(1 for lines in file)
    return nb_lines

if __name__ == "__main__":
    nom_fichier = "erreursAlert2.txt"
    
    processus_ajout = multiprocessing.Process(target=addlinesToFile, args=(nom_fichier,))
    processus_verification = multiprocessing.Process(target=check_new_lines, args=(nom_fichier, 10))

    processus_ajout.start()
    processus_verification.start()

    processus_ajout.join()
    processus_verification.join()
