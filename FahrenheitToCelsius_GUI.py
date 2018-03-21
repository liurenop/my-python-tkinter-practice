# -*- coding: utf-8 -*-
"""
conver degrees Fahrenheit to degrees Celsius
"""
import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

def convert_to_celsius(entry):
    cels.set((int(entry.get()) - 32) *5 /9)

cels = tkinter.StringVar()
#fahr = tkinter.DoubleVar()

label_1 = tkinter.Label(frame, text='Temperature in Fahrenheit:')
label_1.pack()

entry = tkinter.Entry(frame)
entry.pack()

label_2 = tkinter.Label(frame, textvar =cels)
label_2.pack()

button_1 = tkinter.Button(frame, text='Convert', command=lambda:convert_to_celsius(entry))
button_1.pack()

button_2 = tkinter.Button(frame, text='Quit', command=window.destroy)
button_2.pack()

window.mainloop()
