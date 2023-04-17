import tkinter as tk

def function1():
    print("on")


def toggle_functions():
    global functions_on
    functions_on = not functions_on
    if functions_on:
        function1()
        
    else:
        print("off")
    
functions_on = False
root = tk.Tk()

button = tk.Button(root, text="click", command= toggle_functions)
button.pack()

root.mainloop()