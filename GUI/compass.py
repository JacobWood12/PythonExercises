""" A window with north, south, east and west buttons and a north label. """
# Tkinter is for the GUI.
from tkinter import Tk, Button, Label

# Sets up window.
window = Tk()
window.geometry("300x300")
window.title("Compass.")

# North button.
north_button = Button(window, text="North.", command=(print("You pressed the north button.")))
north_button.pack(side="top")

# South button.
south_button = Button(window, text="South.", command=(print("You pressed the south button.")))
south_button.pack(side="bottom")

# East button.
east_button = Button(window, text="East.", command=(print("You pressed the east button.")))
east_button.pack(side="right")

# West button.
west_button = Button(window, text="West.", command=(print("You pressed the west button.")))
west_button.pack(side="left")

# North label.
north_label = Label(window, text="North.")
north_label.place(x=150,y=150,anchor="center")

# Starts main event loop and opens the window.
window.mainloop()
