##GUI
### Imports ###
from tkinter import *

### Basic Setup ###
root = Tk() #create root window to put widgets onto
#labels
title = Label(root,text="Stock Analyzer")
instructions = Label(root,text="Pick a stock")
#buttons
submitButton = Button(root,text="Submit",state=NORMAL,bg="green",fg="white")

### Put on Screen ###
title.grid(row=0,column=0)
instructions.grid(row=1,column=1)
submitButton.grid(row=1,column=2)
### Main loop ###
root.mainloop()