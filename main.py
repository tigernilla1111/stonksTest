import pandas as pd
import yfinance as yf
from datetime import datetime

class ownedStonk:
    def __init__(self, buyPrice, quantity, dividendYield = 0):
        self.buyPrice = buyPrice
        self.quantity = quantity
        self.dividendYield = dividendYield

class Stonk:
    def __init__(self, symbol, buyPrice, quantity, dividendYield = 0):
        self.currentPrice = buyPrice
        self.symbol = symbol
        self.purchaseInstances = []
        self.totalQuantity = quantity
        self.purchaseInstances.append(ownedStonk(buyPrice, quantity, dividendYield))


    def setPrice(self, newPrice):
        self.currentPrice = newPrice

    def getPrice(self):
        return self.currentPrice

    def addPurchaseInstance(self, buyPrice, quantity): #creates new purchase instance to existing stonk
        self.purchaseInstances.append(ownedStonk(buyPrice, quantity))
        self.totalQuantity += quantity


    def getStonkTotalProfit(self):#returns net profit on individuals stonks
        sum = 0
        for instance in self.purchaseInstances:
            sum = sum + ((self.currentPrice - instance.buyPrice) * instance.quantity)

    def getOwnedStockInstance(self, i):
        return self.purchaseInstances[i]

def getStonk(symbol):
    #edit = input("What symbol: ")
    for stonk in arrayOfStocks:
        if stonk.symbol == symbol:
            return stonk
    return False

if __name__ == '__main__':
    #check = Stonk(23, 1, symbol='THCX', dividendYield=4.20)
    arrayOfStocks = []
    #arrayOfStocks.append(check)

    while(True):
        x = input("A - buy more stock, C - change stonk price, RS - return stonk net profit, gp = get price of stonk")
        x = x.lower()


        if (x == 'a'): #adds stonk but checks to see if already bought symbol, update buyPrice
            tempSymbol = input('symbol: ')
            temp = getStonk(tempSymbol)
            if (temp):
                temp.addPurchaseInstance(input('buy price: '), input('quantity: '))
            else:
                temp = Stonk(tempSymbol, input('buy price: '), input('quantity: '))
                arrayOfStocks.append(temp)

        elif(x=='c'):
            change = getStonk(input("Symbol: "))
            change.setPrice(input("New price: "))

        elif(x =='gp'):
            print("today")
            print(datetime.today().strftime("%Y-%m-%d"))

        elif(x == 'p'):
            for stonk in arrayOfStocks:
                print("Symbol: " + stonk.symbol + "\nCurrent Price: " + stonk.getPrice() + "\nQuantity: " + stonk.totalQuantity)
        elif(x=='q' or x =='Q'):
            break


