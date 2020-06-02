##GUI
### Imports ###
from tkinter import *
from Analysis import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

root = Tk() #create root window to put widgets onto
root.geometry("600x200")
root.title("Stock Analyzer Tool")
root.iconbitmap('images\stock.ico')
### FUNCTIONS ### 
def showCurrentPrice():
    tickerSymbol = inputStockOne.get() #get input text
    price = getCurrentPrice(scrapeData(tickerSymbol)) 
    priceLabel = Label(root,text="Current price of "+tickerSymbol+" is: $"+price)
    priceLabel.grid(row=2,column=1)
    return
# def showHistoricPrices():
#     lengthDesired = inputLengthOne.get()
#     tickerSymbol = inputStockOne.get() #get input text
#     historic_prices = getHistoricPrices(scrapeData(tickerSymbol),int(lengthDesired))
#     historic_prices_string = ""
#     for price in historic_prices:
#         historic_prices_string += "$"+price+"  "
#     priceLabel = Label(root,text="Stock price for the last "+lengthDesired+ " days of "+tickerSymbol+" are: "+historic_prices_string)
#     priceLabel.grid(row=2,column=1)
#     return
def graphHistoricPrices():
    lengthDesired = inputLength.get()
    tickerSymbolOne = inputStockOne.get() #get input text
    tickerSymbolTwo = inputStockTwo.get()
    historic_prices_one = getHistoricPrices(scrapeData(tickerSymbolOne),int(lengthDesired))
    historic_prices_two = getHistoricPrices(scrapeData(tickerSymbolTwo),int(lengthDesired))
    historic_prices_combined = []
    stock_type = []
    days = []
    for i in range(0,int(lengthDesired)) : 
        historic_prices_combined.append(float(historic_prices_one[i]))
        stock_type.append(tickerSymbolOne)
        days.append(i+1)
        historic_prices_combined.append(float(historic_prices_two[i]))
        stock_type.append(tickerSymbolTwo)
        days.append(i+1)
    # for price in historic_prices_one:
    #     historic_int_prices_one.append(float(price))
    # for price in historic_prices_two:
    #     historic_int_prices_two.append(float(price))
    d = {'Day':days, 'Price':historic_prices_combined, 'stock': stock_type }
    compareDf = pd.DataFrame(data = d)
    sns.pairplot(x_vars=['Day'],y_vars = ['Price'],data = compareDf, hue='stock',kind='reg')
    plt.show()

### SETUP WIDGETS ###

#labels
title = Label(root,text="Stock Analyzer")
instructions = Label(root,text="Choose two stocks and the number of days:")
#buttons
submitButton = Button(root,text="Submit",state=NORMAL,bg="green",fg="white",command = graphHistoricPrices)
##input boxes
#stock 1 
inputStockOne = Entry(root) # use .get() to get the text from the input box
inputStockOne.insert(0,"Ticker Symbol")
#stock 2 
inputStockTwo = Entry(root) # use .get() to get the text from the input box
inputStockTwo.insert(0,"Ticker Symbol")
#length 
inputLength = Entry(root) # use .get() to get the text from the input box
inputLength.insert(0,"Length")

### PUT ON SCREEN ###
title.grid(row=0,column=1)
instructions.grid(row=1,column=0)
inputStockOne.grid(row=1,column=1)
inputStockTwo.grid(row=1,column=2)
inputLength.grid(row=2,column=1)
submitButton.grid(row=2,column=2)




### MAIN LOOP ###
root.mainloop()