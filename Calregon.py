import os
import subprocess
from tkinter import *
import tkinter as tk

def open_app(path):
    os.startfile(path)

def Mute():
    os.system(r"C:\Users\mesh3\nircmd-x64\nircmd.exe mutesysvolume 1")

wind = Tk()
wind.title("Mixr ")
wind.geometry("500x500+10+500")
wind.resizable(False,False) #Here cant change size 
title = Label(wind , text='Mixr',fg='gold', bg='black' , font=('tajawal ', 16,'bold'))
title.pack(fill=X)

Edgebutton  = tk.Button(wind,bg='black', fg='white', text='Edge', command= lambda: open_app(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'))
Edgebutton.pack()

Steambutton  = tk.Button(wind,bg='black', fg='white', text='Steam', command= lambda: open_app(r'C:\Program Files (x86)\Steam\steam.exe'))
Steambutton.pack()

Mute  = tk.Button(wind,bg='black', fg='white', text='Mute', command= Mute)
Mute.pack()
wind.mainloop()