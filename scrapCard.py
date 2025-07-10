from enum import Enum
from faker import Faker
import pickle
import jsonpickle
from random import *
import requests
from bs4 import BeautifulSoup

import csv

from Card import *

urlSetOne = "https://api.ccgtrader.co.uk/_/items/card?fields%5B0%5D=id&fields%5B1%5D=name&fields%5B2%5D=number&fields%5B3%5D=subtitle&fields%5B4%5D=rarity.id&fields%5B5%5D=image_url&fields%5B6%5D=image.data.asset_url&fields%5B7%5D=number&fields%5B8%5D=reference&fields%5B9%5D=type&fields%5B10%5D=url_title&filter%5Bset%5D%5Beq%5D=5070&sort=number%2Ctype%2Cname&limit=4999"
urlSetTwo = "https://api.ccgtrader.co.uk/_/items/card?fields%5B0%5D=id&fields%5B1%5D=name&fields%5B2%5D=number&fields%5B3%5D=subtitle&fields%5B4%5D=rarity.id&fields%5B5%5D=image_url&fields%5B6%5D=image.data.asset_url&fields%5B7%5D=number&fields%5B8%5D=reference&fields%5B9%5D=type&fields%5B10%5D=url_title&filter%5Bset%5D%5Beq%5D=5071&sort=number%2Ctype%2Cname&limit=4999"
urlSetThree = "https://api.ccgtrader.co.uk/_/items/card?fields%5B0%5D=id&fields%5B1%5D=name&fields%5B2%5D=number&fields%5B3%5D=subtitle&fields%5B4%5D=rarity.id&fields%5B5%5D=image_url&fields%5B6%5D=image.data.asset_url&fields%5B7%5D=number&fields%5B8%5D=reference&fields%5B9%5D=type&fields%5B10%5D=url_title&filter%5Bset%5D%5Beq%5D=5072&sort=number%2Ctype%2Cname&limit=4999"

filePathOne = ".\data\dataSetOne"
filePathTwo = ".\data\dataSetTwo"
filePathThree = ".\data\dataSetThree"

def dictToCard(dict):
    name = dict["name"]
    type = dict["type"]
    id = dict["reference"]
    idRarity = dict["rarity"]["id"]
    if (idRarity == 10):
        rarity = "common"
    elif(idRarity == 20):
        rarity = "uncommon"
    elif(idRarity == 30):
        rarity = "rare"
    elif(idRarity == 48):
        rarity = "ultra_rare"
    else:
        rarity = "NO_RARITY"

    return Card(id, name, rarity, type)

def consumeApiToCardList(url):
    response = requests.get(url)
    data = response.json()
    dataAsDict = data["data"]
    l = len(dataAsDict)
    cardList = list()
    for k in range(l):
        cardList.append(dictToCard(dataAsDict[k]))
    return cardList

def cardListToJSON(cardList):
    return jsonpickle.dumps(cardList, indent = 4)

def cardListToCSV(cardList):
    tabForCsv = list()
    for k in range (len(cardList)):
        tabForCsv.append(cardList[k].toList())
    return tabForCsv

def saveJSON(filePath, jsonName):
    f = open(filePath+".json", "w")
    f.write(jsonName)
    f.close()

def saveCSV(filePath, CSVName):
    f = open(filePath + ".csv", "w")
    csv.writer(f).writerows(CSVName)
    f.close()

def main():


    cardListSetOne = consumeApiToCardList(urlSetOne)
    cardListSetTwo = consumeApiToCardList(urlSetTwo)
    cardListSetThree = consumeApiToCardList(urlSetThree)

    cardListSetOneAsJSON = cardListToJSON(cardListSetOne)
    cardListSetTwoAsJSON = cardListToJSON(cardListSetTwo)
    cardListSetThreeAsJSON = cardListToJSON(cardListSetThree)

    cardListSetOneAsCSV = cardListToCSV(cardListSetOne)
    cardListSetTwoAsCSV = cardListToCSV(cardListSetTwo)
    cardListSetThreeAsCSV = cardListToCSV(cardListSetThree)

    saveJSON(filePathOne, cardListSetOneAsJSON)
    saveCSV(filePathOne, cardListSetOneAsCSV)

    saveJSON(filePathTwo, cardListSetTwoAsJSON)
    saveCSV(filePathTwo, cardListSetTwoAsCSV)

    saveJSON(filePathThree, cardListSetThreeAsJSON)
    saveCSV(filePathThree, cardListSetThreeAsCSV)

    print("fini ^^")

if __name__ == "__main__":
    main()