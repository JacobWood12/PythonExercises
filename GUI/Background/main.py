# TKinter is for the GUI.
from tkinter import *

def red_click():
    print("You pressed the red button.")
    # Changes background to red.
    window['bg']='#e45858'

def blue_click():
    print("You pressed the blue button.")
    # Changes background to blue.
    window['bg']='#6246ea'

window = Tk()
# Sets size of the window otherwise it's to small to see the background.
window.geometry("400x200")

red_btn.pack()
blue_btn.pack()

window.mainloop()
