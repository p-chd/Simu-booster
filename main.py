from enum import Enum
from faker import Faker
import pickle
import jsonpickle
from random import *
import requests

import scrapCard
from Card import Card

fake = Faker()

class Rarity(Enum):
    COMMON=1
    UNCOMMON=2
    RARE=3
    ULTRA_RARE=4

#Creer une fausse liste de n cartes avec une rarite fixe
def createFalseCardList(n, rarity):
    cardList = list()
    for i in range(n):
        cardList.append(Card(i, fake.name(), rarity, 'type_temp'))
    return cardList

#Print une liste
def printList(l):
    for i in range(len(l)):
        print(l[i])

#Tire une carte aléatoire parmi celles dans la liste l
def drawRandomCard(l):
    return l[randint(0, len(l) - 1)]
    
#Tire n cartes parmi celles dans la liste l -- Doublon possible
def drawNRandomCards(l, n):
    returnedList = []
    for k in range(n):
        returnedList.append(drawRandomCard(l))
    return returnedList

#Creer un booster de 8 cartes à partir de 3 listes de cartes
def createBooster(common, uncommon, rare):
    cardList = list()
    for i in range(5):
        cardList.append(drawRandomCard(common))
    for i in range(2):
        cardList.append(drawRandomCard(uncommon))
    for i in range(1):
        cardList.append(drawRandomCard(rare))
    return cardList

#Creer un deck de n cartes à partir de 4 listes de cartes: common, uncommon, rare, ultra_rare
def createDeck(common, uncommon, rare, ultra_rare, n):
    deck = list()
    for i in range (n):
        r = random()
        if r <= 0.56:
            deck.append(drawRandomCard(common))
        elif r <= 0.82:
            deck.append(drawRandomCard(uncommon))
        elif r <= 0.93:
            deck.append(drawRandomCard(rare))
        else:
            deck.append(drawRandomCard(ultra_rare))
    return deck

#Creer une liste de cartes à partir du JSON reference
def importCardListFromJSON(JSONPath):
    f = open(JSONPath + ".json", "r")
    cardList = jsonpickle.decode(f.read())
    f.close()
    return cardList

#Creer une liste de carte uniquement à partir des cartes communes d'une autre liste de cartes
def retrieveByRarity(l, rarity):
    cardList = list()
    for k in l:
        if k.rarity == rarity:
            cardList.append(k)
    return cardList

#Count le nombre de cartes avec la rarete correspondante
def countRarity(cardList, rarity):
    counter = 0
    for k in cardList:
        if k.rarity == rarity:
            counter += 1
    return counter

#Fonction de test
def main():

    #On cree les trois listes
    commonsList = createFalseCardList(44, "Common")
    uncommonsList = createFalseCardList(50, "Uncommon")
    raresList = createFalseCardList(50, "rare")
    #printList(commonsList)

    #On tire 72 cartes aléatoire
    tirage = drawNRandomCards(commonsList, 72)
    printList(tirage)

    #On cree un booster
    booster = createBooster(commonsList, uncommonsList, raresList)
    print("BOOSTER:\n")
    printList(booster)

    #On fait un deck
    deck = createDeck(commonsList, uncommonsList, raresList, 128)
    printList(deck)
    print(f"Longueur du deck: {len(deck)}")

def main2():
    print("Importing...")
    cardListSetOne = importCardListFromJSON(".\data\dataSetOne")
    cardListSetTwo = importCardListFromJSON(".\data\dataSetTwo")
    cardListSetThree = importCardListFromJSON(".\data\dataSetThree")

    print("Import done\n")

    print("Concatenation...")
    cardListeAllSet = cardListSetOne + cardListSetTwo + cardListSetThree
    print("Concatenation done.\n")

    print("Retrieving by rarity...")
    commonCardList = (retrieveByRarity(cardListeAllSet, "common"))
    uncommonCardList = (retrieveByRarity(cardListeAllSet, "uncommon"))
    rareCardList = (retrieveByRarity(cardListeAllSet, "rare"))
    veryrareCardList = (retrieveByRarity(cardListeAllSet, "ultra_rare"))
    print("Retrieved.\n")

    print("Deck creation...")
    L = createDeck(commonCardList, uncommonCardList, rareCardList, veryrareCardList, 200)
    print("Deck created.\n")

    print("Couting by rarity from deck...")
    commonCount = countRarity(L, "common")
    uncommonCount = countRarity(L, "uncommon")
    rareCount = countRarity(L, "rare")
    ultraRareCount = countRarity(L, "ultra_rare")
    print("Count done.\n")

    print(f"Commons: {commonCount}\nUncommons: {uncommonCount}\nRares: {rareCount}\nUltra_rare: {ultraRareCount}\n")
    

if __name__ == "__main__":
    main2()
