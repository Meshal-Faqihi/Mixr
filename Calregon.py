import os
#from collections.abc import Mapping
from sound import Sound
import subprocess
from tkinter import *
import tkinter as tk

import ctypes
MUTE = 0x8000
SND_app = 0x80
ctypes.windll.winmm.waveOutSetVolume(0,MUTE)
#Sound.mute()

exit()
def open_app(path):
    os.startfile(path)
    
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

wind.mainloop()