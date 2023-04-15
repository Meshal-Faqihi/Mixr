import os

import subprocess
from tkinter import *
import tkinter as tk

####What is tk. ???!?!?!?
#### what diffrant . and =  ????!?!?

def add_num():
   num1 = int(Ent1.get())
   result = num1 * 3.75
   ansr.config(text="result"+str(result))

def open_app(path):
    os.startfile(path)
    


wind = Tk()
wind.title("Meshal ")
wind.geometry("500x500+10+500")
wind.resizable(False,False) #Here cant change size 
title = Label(wind , text='calculator',fg='gold', bg='black' , font=('tajawal ', 16,'bold'))
title.pack(fill=X)

Ent1 = tk.Entry(wind)
Ent1.pack()


# mybutton = tk.Button(wind, text ='Click ',bg='black',fg='white',command=add_num)
# mybutton.pack()

xbutton  = tk.Button(wind, text='Open Steam', command= lambda: open_app(r'C:\Program Files\Mozilla Firefox\firefox.exe'))
# xbutton = tk.Button(wind, text ='Click ',bg='black',fg='white',command=open_app(r'C:\Program Files\Mozilla Firefox\firefox.exe'))
xbutton.pack()

ansr = tk.Label(wind, text='eeeee')
ansr.pack()

wind.mainloop()