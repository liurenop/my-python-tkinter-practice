# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 08:35:34 2018
编写应用的MVC模式
@author: joshua.liu
"""
import tkinter

#The controller
def click():
    counter.set(counter.get() + 1)
    
if __name__ == '__main__':
    window = tkinter.Tk()
    #The model
    counter = tkinter.IntVar()
    counter.set(0)
    #The views
    frame = tkinter.Frame(window)
    frame.pack()
    label = tkinter.Label(frame, textvariable=counter)
    label.pack()
    button = tkinter.Button(frame, text='Click', command=click)
    button.pack()
    
    #Start the machinery
    window.mainloop()