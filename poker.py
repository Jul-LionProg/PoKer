import random

cartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
naipes = ["Espadas","Paus","Ouros","Copas"]
escolhapc = ["S","N"]

def maojogador():
    carta1j = random.choice(cartas)
    carta2j = random.choice(cartas)
    naipe1j = random.choice(naipes)
    naipe2j = random.choice(naipes)
