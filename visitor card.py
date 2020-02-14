# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:03:49 2020

@author: dell
"""
from tkinter import *

if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
    gui.geometry("390x265")
    pane = Frame(gui)
    pane.pack(fill = BOTH, expand = True) 
  
    # set the background colour of GUI window 
    gui.configure(background="light green") 
  
    # set the title of GUI window 
    b1 = Label(pane, text = "VISITOR CARD",bg='pink',font=('Arial',25,'bold')) 
    b1.pack(fill = BOTH, expand = True) 
    b2 = Label(pane, text = "NANDINI CHOURASIA") 
    b2.pack(fill = BOTH, expand = True) 
    b3 = Label(pane, text = "SRMIST") 
    b3.pack(fill = BOTH, expand = True) 
    b4 = Label(pane, text = "CSE CC") 
    b4.pack(fill = BOTH, expand = True) 
    gui.mainloop() 
  

