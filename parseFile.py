import time
from datetime import datetime

def txt(path, timeStamp):
    while True:
        try:
            with open(path,'r') as file:
                for line in file:
                    date_string = line.strip()[8:]  # Ignorer l'index de début, laisser le reste de la ligne
                    date_object = datetime.strptime(date_string, '%d/%m/%Y %H:%M:%S')
                    current_date=datetime.today().strftime('%d/%m/%Y %H:%M:%S')
                    if(date_object==current_date):
                        print("alert")
                    print(f"{date_object}\ncurrent date\n{datetime.today().strftime('%d/%m/%Y %H:%M:%S')} \n*******")


                    time.sleep(timeStamp)

        except FileNotFoundError:
            print("File not found")

ch = "./alert.csv"
txt(ch, 1)
