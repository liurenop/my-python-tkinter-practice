# -*- coding: utf-8 -*-
"""
Write a GUI application with a single button. Initially the button is labeled
0, but each time it is clicked, the value on the button increases by 1.
"""

import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

def add_up():
    number.set(number.get() + 1)
number = tkinter.IntVar()
number.set(0)
button = tkinter.Button(frame, textvariable=number, command=add_up)
button.pack()
window.mainloop()
