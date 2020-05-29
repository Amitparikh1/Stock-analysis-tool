##GUI
### Imports ###
from tkinter import *

### Basic Setup of Widgets ###
root = Tk() #create root window to put widgets onto
#labels
title = Label(root,text="Stock Analyzer")
instructions = Label(root,text="Stock 1:")
#buttons
submitButton = Button(root,text="Submit",state=NORMAL,bg="green",fg="white")
#input box
inputStock = Entry(root) # use .get() to get the text from the input box
inputStock.insert(0,"Ticker Symbol")
### Put on Screen ###
title.grid(row=0,column=1)
instructions.grid(row=1,column=0)
inputStock.grid(row=1,column=1)
submitButton.grid(row=1,column=2)

### Main loop ###
root.mainloop()