""" Brings up a window with buttons to change it's colour to red or blue. """
# Tkinter is for the GUI.
from tkinter import Tk, Button

def red_click():
    """ Run when the user clicks the red button, changes the window background to red. """
    print("You pressed the red button.")
    window['bg']='#e45858'

def blue_click():
    """ Runs when the user clicks the blue button, changes the window background to blue. """
    print("You pressed the blue button.")
    window['bg']='#6246ea'

window = Tk()
# Sets size of the window otherwise it's to small to see the background.
window.geometry("400x200")

# Create buttons.
red_btn = Button(window, text="Red.", command=red_click)
blue_btn= Button(window, text="Blue.", command=blue_click)

red_btn.pack()
blue_btn.pack()

window.mainloop()
