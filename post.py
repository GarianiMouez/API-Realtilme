import time
import requests
from datetime import datetime
import random

url = "http://localhost:3000/fact"

while True:
    try:
        # Créer les données avec x prenant la date et y prenant 1 ou 0 de manière aléatoire
        x = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        y = random.choice([0, 1])
        data = {"x": x, "y": y}
        
        # Effectuer la requête HTTP POST avec les données spécifiées
        response = requests.post(url, json=data)
        
        # Vérifier la réponse si nécessaire
        print("Réponse:", response.text)
        
    except Exception as e:
        print("Erreur lors de l'envoi de la requête:", e)
    
    # Attendre trois secondes avant la prochaine requête
    time.sleep(3)
