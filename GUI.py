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
    priceLabel.pack(row=2,column=1)
    return

### SETUP WIDGETS ###

#labels
title = Label(root,text="Stock Analyzer")
instructions = Label(root,text="Choose a stock:")
#buttons
submitButton = Button(root,text="Submit",state=NORMAL,bg="green",fg="white",command = showCurrentPrice)
#input box
inputStock = Entry(root) # use .get() to get the text from the input box
inputStock.insert(0,"Ticker Symbol")

### PUT ON SCREEN ###
title.grid(row=0,column=1)
instructions.grid(row=1,column=0)
inputStock.grid(row=1,column=1)
submitButton.grid(row=1,column=2)




### MAIN LOOP ###
root.mainloop()