from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import os
import subprocess
from tkinter import *
import tkinter as tk

def open_app(path):
    os.startfile(path)

def Mute():
   devices = AudioUtilities.GetSpeakers()
   interface = devices.Activate(IAudioEndpointVolume._iid_ , CLSCTX_ALL, None)
   volume = cast(interface, POINTER(IAudioEndpointVolume))
   unvolume = cast(interface, POINTER(IAudioEndpointVolume))
   global oneButton_on
   oneButton_on = not oneButton_on
   if oneButton_on:
      volume.SetMute(0, None)
   else:
      unvolume.SetMute(1, None)
oneButton_on = True

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