# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:28:50 2018

@author: joshua.liu
"""

import tkinter

window = tkinter.Tk()

#The model
counter = tkinter.IntVar()
counter.set(0)

#Two controllers
def click_up():
    counter.set(counter.get()+1)
def click_down():
    counter.set(counter.get()-1)

#The views
frame = tkinter.Frame(window)
frame.pack()
button_1 = tkinter.Button(frame, text='Up', command=click_up)
button_1.pack()
button_2 = tkinter.Button(frame, text='Down', command=click_down)
button_2.pack()
label = tkinter.Label(frame, textvariable=counter)
label.pack()

window.mainloop()