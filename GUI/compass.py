""" A window with north, south, east and west buttons and a north label."""
from tkinter import Tk, Button, Label

window = Tk()
window.geometry("300x300")
window.title("Compass")

# North button.
north_btn = Button(window, text="North.", command=(print("You pressed the north button.")))
north_btn.pack(side="top")

# South button.
south_btn = Button(window, text="South.", command=(print("You pressed the south button.")))
south_btn.pack(side="bottom")

# East button.
east_btn = Button(window, text="East.", command=(print("You pressed the east button.")))
east_btn.pack(side="right")

# West button.
west_btn = Button(window, text="West.", command=(print("You pressed the west button.")))
west_btn.pack(side="left")

# North label.
north_label = Label(window, text="North.")
north_label.place(x=150,y=150,anchor="center")

window.mainloop()
