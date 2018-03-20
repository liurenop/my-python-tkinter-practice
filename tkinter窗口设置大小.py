# -*- coding: utf-8 -*-
"""
tkinter窗口设置大小
"""

import tkinter

# 创建根窗口
root = tkinter.Tk()
root.title('Hello') #主窗口标题
# 设置窗口大小
root.geometry("300x200")#x是字母

#在窗体中创建一个框架，用它来承载其他小部件
app = tkinter.Frame(root)
#设置布局管理器
app.grid()

label = tkinter.Label(app, text ="hello world!")
label.grid()

button = tkinter.Button(app)
button.grid()
button.configure (text = 'click')

root.mainloop()