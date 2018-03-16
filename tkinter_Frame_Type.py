# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:13:20 2018

tkinter中Frame类型

"""

import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
frame2 = tkinter.Frame(window, borderwidth=4, relief=tkinter.GROOVE)
frame2.pack()

first = tkinter.Label(frame, text='First label')#first在frame里
first.pack()
second = tkinter.Label(frame2, text='Second label')#second在frame2里
second.pack()
third = tkinter.Label(frame2, text='Third label')#third在frame2里
third.pack()

window.mainloop()