import random
import time


type = 0
seconde = 0

def nombre_mystere():
    global type
    global seconde
    mystere = random.randint(1, 10)
    nombre = None
    nbtry = 0
    while nombre != mystere:
        nombre = int(input("Proposez un nombre ==> "))
        if nombre < mystere :
            print("C'est plus !")
            nbtry = nbtry + 1
        elif nombre > mystere :
            print("C'est moins !")
            nbtry = nbtry + 1


        else:
            type = type + 1
            print(f"Bravo vous avez gagné ! Le nombre de tentative est de : {nbtry} seconde {seconde}")
            print(type)
#Chrono          
def chrono():
    global type
    global seconde
    while type == 0:
        seconde = seconde + 1 
        time.sleep(1) 
       


nombre_mystere()




