import requests
from bs4 import BeautifulSoup as bs
import urllib3

def getPrice():
    s = requests.get('https://www.coinbase.com/charts').text
    soup = bs(s,"html.parser")
    btcPrice = soup.find("li", {"class": "top-balance"})
    btcPriceRaw = btcPrice.text
    return btcPriceRaw



def convertPriceFloat(btcPriceRaw):
    btcPriceInt = btcPriceRaw.split()
    btcPriceInt = btcPriceInt[3].replace("$","")
    btcPriceFloat = float(btcPriceInt)
    return btcPriceFloat


def whichOne():
    while True:
        try:
            typeCon = int(input("Enter 1 to convert USD to BTC, 2 to convert BTC to USD: "))
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
    theType = 0
    while True:
        try:
            theOne = int(input("Enter 1 to convert USD to BTC, 2 to convert BTC to USD: "))
            if theOne == 1:
                userAnsUb,ansUb = priceConvertUb(btcFloat)
                theType = 1
                return userAnsUb, ansUb, theOne, theType
                
            elif theOne == 2:
                theType = 2
                userAnsBu,ansBu = priceConvertBu(btcFloat)
                return userAnsBu, ansBu, theOne, theType
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
    btcFloat = convertPriceFloat(btcPriceFound)
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
        else:
            print('Please input 1 or 2...')
            try:
                which = int(input("Enter 1 to convert USD to BTC, 2 to convert BTC to USD: "))
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
                        print('$',userAnsPt1,'is',userAnsPt2,'BTC')
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


    







