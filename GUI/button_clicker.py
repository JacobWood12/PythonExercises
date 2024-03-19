""" TKinter is for the GUI. """
from tkinter import Tk, Button

""" Random is for the safe/unsafe message. """
import random

CLICKS = int(0)

def btn_click():
    """ Runs every time the user CLICKS the button. """
    global CLICKS
    CLICKS = int(CLICKS + 1)
    if CLICKS == 1:
        print("Button clicked once. You're safe.")
    else:
        coin_flip = random.randint(1, 2)
        if coin_flip == 1:
            print(f"Button clicked {CLICKS} times. You're safe.")
        elif coin_flip == 2:
            print(f"Button clicked {CLICKS} times. You're in danger.")
        else:
            print("There was an error. Please try again.")
            print("TECHNICAL DETAILS.")
            print("The random number generator generated a number that was not 1 or 2.")

window = Tk()
btn = Button(window, text="Click me or else.", command=btn_click)
btn.pack()

window.mainloop()
