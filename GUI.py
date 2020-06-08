##GUI
### Imports ###
from tkinter import *
from Scraper import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
from scipy import stats

root = Tk() #create root window to put widgets onto
root.geometry("800x100")
root.title("Linear Regression between Stock Prices")
root.iconbitmap('images\stock.ico')

### FUNCTIONS ### 
def showCurrentPrice():
    tickerSymbol = inputStockOne.get() #get input text
    price = getCurrentPrice(scrapeData(tickerSymbol)) 
    priceLabel = Label(root,text="Current price of "+tickerSymbol+" is: $"+price)
    priceLabel.grid(row=2,column=1)
    return
def r2(x,y):
    return stats.pearsonr(x, y)[0] ** 2

def compareHistoricPrices():
    #how many days  
    lengthDesired = inputLength.get()
    #two inputted ticker symbols 
    tickerSymbolOne = (inputStockOne.get()).upper()
    tickerSymbolTwo = (inputStockTwo.get()).upper()
    # get price information from Scraper.py
    historic_prices_one = getHistoricPrices(scrapeData(tickerSymbolOne),int(lengthDesired))
    historic_prices_two = getHistoricPrices(scrapeData(tickerSymbolTwo),int(lengthDesired))
    #empty arrays 
    historic_prices_one_float = []
    historic_prices_two_float = []
    loop_length = min(len(historic_prices_one),len(historic_prices_two))
    # loop through and get data into new arrays 
    for i in range(0,loop_length) : 
        historic_prices_one_float.append(historic_prices_one[i])
        historic_prices_two_float.append(historic_prices_two[i])
    # dictionary for the assembled data
    d = {tickerSymbolOne: historic_prices_one_float,tickerSymbolTwo: historic_prices_two_float}
    # create data frame using above dictionary for plotting
    compareDf = pd.DataFrame(data = d)
    # pair plot through seaborn
    sns.jointplot(x=compareDf[tickerSymbolOne],y=compareDf[tickerSymbolTwo],kind='reg',stat_func=r2)
    #sns.pairplot(x_vars=['Day'],y_vars = ['Price'],data = compareDf, hue='stock',kind='reg')
    plt.show()

### SETUP WIDGETS ###

#labels
title = Label(root,text="Linear Regression between two Stock Prices")
instructions = Label(root,text="Choose two stocks and the number of past days to analyze:")
#buttons
submitButton = Button(root,text="Submit",state=NORMAL,bg="green",fg="white",command = compareHistoricPrices)
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