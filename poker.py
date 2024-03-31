import random

cartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
naipes = ["Espadas","Paus","Ouros","Copas"]
escolhapc = ["S","N"]

def maojogador():
    carta1j = random.choice(cartas)
    carta2j = random.choice(cartas)
    naipe1j = random.choice(naipes)
    naipe2j = random.choice(naipes)
    
    print("Jogador", nome, "você tem", carta1j,"de",naipe1j, "e", carta2j, "de", naipe2j)


def maopc():
    carta1pc = random.choice(cartas)
    carta2pc = random.choice(cartas)
    naipe1pc = random.choice(naipes)
    naipe2pc = random.choice(naipes)

def mesa():
    cartamesa = random.choice(cartas)
