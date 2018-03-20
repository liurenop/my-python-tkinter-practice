# -*- coding: utf-8 -*-
"""
统计字母的个数
"""
import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

# model
DNA = tkinter.StringVar()
text = tkinter.Text(frame)
text.pack()
count = {}

def DNA_Count(text):
    data = text.get('0.0', tkinter.END)
    for char in 'ATCG':
        count[char] = data.count(char)
    DNA.set('Num As:{0} Num Ts:{1} Num Cs:{2} Num Gs:{3}'.format(count['A'], count['T'], count['C'], count['G']))
    
# controller
button = tkinter.Button(frame, text='Count', command=lambda: DNA_Count(text))
button.pack()
# display
label = tkinter.Label(frame, textvariable=DNA)
label.pack()

window.mainloop()