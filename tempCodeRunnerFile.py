from tkinter import *
from webbrowser import get

def list(wind):
    a.dolr = 3.75
    show.a.SR = 2
wind = Tk()           
wind.geometry("500x500")
sp = Spinbox(wind ,command=list) 
sp.pack() 

a = Listbox()
a.pack()
a.insert(1, "SR")
a.insert(2, "dolr")

show=Label
wind.mainloop()