""" A window with north, south, east and west buttons and a north label. """
# Tkinter is for the GUI.
from tkinter import Tk, Button, Label

# Sets up window.
window = Tk()
window.geometry("300x300")
window.title("Compass.")

def button_pressed(direction):
	""" Changes the text of the label in the centre to the button pressed. """
	centre_label = Label(window, text=direction)
	centre_label.place(x=150,y=150,anchor="center")

# North button.
north_button = Button(window, text="North.", command= lambda: button_pressed("North."))
north_button.pack(side="top")

# South button.
south_button = Button(window, text="South.", command= lambda: button_pressed("South."))
south_button.pack(side="bottom")

# East button.
east_button = Button(window, text="East.", command= lambda: button_pressed("East."))
east_button.pack(side="right")

# West button.
west_button = Button(window, text="West.", command= lambda: button_pressed("West."))
west_button.pack(side="left")

# Starts main event loop and opens the window.
window.mainloop()
