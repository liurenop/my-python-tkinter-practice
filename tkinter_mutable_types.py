# -*- coding: utf-8 -*-
"""
tkinter中的可变参数

Suppose you want to display a string, such as the current time or a score in a game, in several places in a GUI—the application’s status bar, some dialog boxes, and so on. Calling method config on each widget every time there is new information isn’t hard, but as the application grows, so too do the odds that we’ll forget to update at least one of the widgets that’s displaying the string. What we really want is a string that “knows” which widgets care about its value and can alert them itself when that value changes. 
Python’s strings, integers, floating-point numbers, and Booleans are immutable, so module tkinter provides one class for each of the immutable types: StringVar for str, IntVar for int, BooleanVar for bool, and DoubleVar for float. (The use of the word double is historical; it is short for “double-precision floating-point number.”) These mutable types can be used instead of the immutable ones; here we show how to use a StringVar instead of a str:
比如说你想在一个GUI中的某些地方展示一个字符串，像是当前的时间或是一场比赛中的比分，地方可能是应用程序的状态栏、一些对话框等等。当每一次需要更新一个数据时都对每一个widget调用config方法不是很困难。但是当程序逐渐变得复杂，就很有可能会发生我们在某次更新数据的过程中忘了某个widget的情况。我们真正想要的是让一个字符串能够知道哪些widget需要的它的更新数据，并且及时提醒这些widget。
Python的字符串、整数、浮点数和布尔值都是不可变的，所以tkinter模块为每一种不可变的数据类型都提供了一种相应的可变类：StringVar对应str，IntVar对应int，BooleanVar对应bool， DoubleVar对应float.这些可变的数据类型能够代替那些不可变数据类型。

"""
import tkinter

window = tkinter.Tk()
data = tkinter.StringVar()#data是可变的
data.set('Data to display')
label = tkinter.Label(window, textvariable=data)#label里用的是textvariable，不是text
label.pack()

window.mainloop()
