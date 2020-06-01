##GUI
### Imports ###
from tkinter import *
from Analysis import *

root = Tk() #create root window to put widgets onto
root.title("Stock Analyzer Tool")
root.iconbitmap('images\stock.ico')
### FUNCTIONS ### 
def showCurrentPrice():
    tickerSymbol = inputStock.get() #get input text
    price = getCurrentPrice(scrapeData(tickerSymbol)) 
    priceLabel = Label(root,text="Current price of "+tickerSymbol+" is: $"+price)
    priceLabel.grid(row=2,column=1)
    return
def showHistoricPrices():
    lengthDesired = inputLength.get()
    tickerSymbol = inputStock.get() #get input text
    historic_prices = getHistoricPrices(scrapeData(tickerSymbol),int(lengthDesired))
    historic_prices_string = ""
    for price in historic_prices:
        historic_prices_string += "$"+price+"  "
    priceLabel = Label(root,text="Stock price for the last "+lengthDesired+ " days of "+tickerSymbol+" are: "+historic_prices_string)
    priceLabel.grid(row=2,column=1)
    return

### SETUP WIDGETS ###

#labels
title = Label(root,text="Stock Analyzer")
instructions = Label(root,text="Choose a stock:")
#buttons
submitButton = Button(root,text="Submit",state=NORMAL,bg="green",fg="white",command = showHistoricPrices)
#input boxes
inputStock = Entry(root) # use .get() to get the text from the input box
inputStock.insert(0,"Ticker Symbol")
inputLength = Entry(root) # use .get() to get the text from the input box
inputLength.insert(0,"Length")

### PUT ON SCREEN ###
title.grid(row=0,column=1)
instructions.grid(row=1,column=0)
inputStock.grid(row=1,column=1)
inputLength.grid(row=1,column=2)
submitButton.grid(row=1,column=3)




### MAIN LOOP ###
root.mainloop()