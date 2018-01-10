import requests
from bs4 import BeautifulSoup as bs
import urllib3
import sys

def getPrice():
    s = requests.get('https://www.worldcoinindex.com/coin/bitcoin').text
    soup = bs(s,"html.parser")
    btcPrice = soup.find("td", {"class" : "coinprice"})
    btcString = btcPrice.getText()  
    return btcString


def convertPriceFloat(btcPriceRaw):
    price = ""
    for h in btcPriceRaw:
        if(h.isdigit()):
            price += h
    print(price)
    numLen = len(price)
    num = price[:-2]
    dec = price[-2:]
    price = num + '.' + dec
    btcDisplay = '$' + price
    btcPriceFloat = float(price)
    return btcPriceFloat, btcDisplay


def whichOne():
    while True:
        try:
            typeCon = int(input("Enter 1 to convert USD to BTC, 2 to convert BTC to USD, 3 to exit: "))
            break
        except ValueError:
             print('Please enter either 1 or 2...')
    return typeCon

def priceConvertUb(btcPriceFloat):
    btc = btcPriceFloat
    while True:
        try:
            userUsd = float(input("Enter a price in USD: "))
            convertedub = (userUsd*(1/btc))
            break
        except ValueError:
            print("Please enter a valid number...")
    return userUsd, convertedub

def priceConvertBu(btcPriceFloat):
    btc = btcPriceFloat
    while True:
        try:
            userBtc = float(input("Enter amount of Bitcoin: "))
            convertedbu = userBtc * btc
            break
        except ValueError:
            print("Please enter a valid number...")
    return userBtc, convertedbu



def reDone(btcFloat):
    choice = 0
    while True:
        try:
            theOne = int(input("Enter 1 to convert USD to BTC, 2 to convert BTC to USD: "))
            if theOne == 1:
                userAnsUb,ansUb = priceConvertUb(btcFloat)
                choice = 1
                return userAnsUb, ansUb, theOne, choice
                
            elif theOne == 2:
                choice = 2
                userAnsBu,ansBu = priceConvertBu(btcFloat)
                return userAnsBu, ansBu, theOne, choice
                
            elif theOne == 3:
                sys.exit()
                choice = 3
                break
        except ValueError:
            print('Please enter either 1 or 2...')
        
        
def convertAgain(again):
    if again == 1:
        whichOne()
    else:
        quit()



def main():
    btcPriceFound = getPrice()
    btcFloat, btcDisplay = convertPriceFloat(btcPriceFound)
    print('------------------------------')
    print('BTC TO USD CONVERTER')
    print('BY NICK KULUNGIAN')
    print('------------------------------')
    print('1 BTC =',btcFloat)
    which = whichOne()
    while True:
        if which == 1:
            userAnsUb,ansUb = priceConvertUb(btcFloat)
            print('$',userAnsUb, 'is',ansUb,'BTC')
            which = 0
            break
        elif which == 2:
            userAnsBu,ansBu = priceConvertBu(btcFloat)
            print(userAnsBu,'BTC', 'is','$',ansBu)
            which = 0
            break
        elif which == 3:
            sys.exit()
        else:
            print('Please input 1 or 2...')
            try:
                which = int(input("Enter 1 to convert USD to BTC, 2 to convert BTC to USD, 3 to exit: "))
                break
            except ValueError:
                print('Please input 1 or 2...')
                                
    while True:
        try:
            again = int(input("Enter 1 to do another conversion, any other key to exit: "))
            
            while True:
                if again == 1:
                    userAnsPt1,userAnsPt2, theOne, theType = reDone(btcFloat)
                    if theType == 1:
                        print('$',userAnsPt1,'is','{:.2f}'.format(userAnsPt2),'BTC')
                        again = 0
                        again = int(input("Enter 1 to do another conversion, any other key to exit: "))
                    elif theType == 2:
                        print(userAnsPt1,'BTC','is $',userAnsPt2)
                        again = 0
                        again = int(input("Enter 1 to do another conversion, any other key to exit: "))
                else:
                    break
                    input('Press ENTER to exit')
        except ValueError:
            break
            input('Press ENTER to exit')

main()


    







