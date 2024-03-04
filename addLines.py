import time
from datetime import datetime

def addLineToFile(filename):
    while True:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        ligne = f"[Error],{current_date}\n"
        
        with open(filename, "a") as file:
            file.write(ligne)
        
        print("Ligne ajoutée dans le fichier.")
        
        time.sleep(10)

nom_fichier = "erreurs.csv"

addLineToFile(nom_fichier)