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
wind.title("Mixr ")
wind.geometry("500x500+10+500")
wind.resizable(False,False) #Here cant change size 
title = Label(wind , text='Mixr',fg='gold', bg='black' , font=('tajawal ', 16,'bold'))
title.pack(fill=X)


xbutton  = tk.Button(wind,bg='black', fg='white', text='Open EDGE', command= lambda: open_app(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'))

xbutton.pack()

wind.mainloop()