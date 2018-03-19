# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 08:01:44 2018

@author: joshua.liu
"""

import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()
var = tkinter.StringVar()
label = tkinter.Label(frame, textvariable=var)
label.pack()
entry = tkinter.Entry(frame, textvariable=var)
entry.pack()

window.mainloop()