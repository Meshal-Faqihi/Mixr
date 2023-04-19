from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import os
from tkinter import *
from tkinter import Tk, Scale, HORIZONTAL
import tkinter as tk



def open_app(path):
    os.startfile(path)

def Mute():
   devices = AudioUtilities.GetSpeakers()
   interface = devices.Activate(IAudioEndpointVolume._iid_ , CLSCTX_ALL, None)
   volume = cast(interface, POINTER(IAudioEndpointVolume))

   global Toggel_Button
   Toggel_Button = not Toggel_Button
   if Toggel_Button:
      volume.SetMute(0, None)
   else:
      volume.SetMute(1, None)
Toggel_Button = True

def Mic():
   devices = AudioUtilities.GetMicrophone()
   interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
   volume = cast(interface, POINTER(IAudioEndpointVolume))

   global Toggel_Button
   Toggel_Button = not Toggel_Button
   if Toggel_Button:
      volume.SetMute(0, None)
   else:
      volume.SetMute(1, None)
Toggel_Button = True

def SVolume(val):
   devices = AudioUtilities.GetSpeakers()
   interface = devices.Activate(IAudioEndpointVolume._iid_ , CLSCTX_ALL, None)
   volume = cast(interface, POINTER(IAudioEndpointVolume))
   voolume = float(val)
   volume.SetMasterVolumeLevel(voolume, None)
   print(f"Volume set to {voolume}")
   
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

Speakers = tk.Button(wind,bg='gray', fg='white',height=4,width=10, text='MuteAudio', command= Mute)
Speakers.pack()
Speakers.place(x=400,y=325)

Microphone  = tk.Button(wind,bg='red', fg='white' ,height=4,width=10, text='MuteMic', command= Mic)
Microphone.pack()
Microphone.place(x=400,y=400)

Levelvolume = Scale(wind, from_= -62.6, to = 4.9,width=20, orient= VERTICAL,command=SVolume )
Levelvolume.pack()
Levelvolume.place(x=420,y=200)

wind.mainloop()