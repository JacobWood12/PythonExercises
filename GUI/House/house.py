''' Tkinter is for the GUI. '''
from tkinter import Tk, Frame, Label, TOP, PhotoImage, Button, LEFT

# Defines height and width of the main window.
w_width = 500
w_height = 700

# Defines background colour as a light greyish purple.
bg_colour = "#E7DDFF"

# Initialises window.
window = Tk()
window.geometry(str(w_width) + "x" + str(w_height))
window.title("My App.")

# Initialises main frame and packs it.
main_frame=Frame(background=bg_colour, width=w_width, height=w_height)
main_frame.pack()

# Add widgets to the root window.
Label(main_frame, text = "House", font =("Verdana", 15)).pack(side = TOP, pady = 10)

# Creates a PhotoImage to use the house.png image.
# If you're downloading this, make sure to download the image as well and change the path below.
photo = PhotoImage(file = r"/Users/jacobwood/Documents/Programming/PythonExercises/GUI/house/house.png")

# Resizes image to fit on button.
photoimage = photo.subsample(3,3)

# Uses the image option to set the image on it's own button.
# The compound option is used to align the image on the LEFT side of the button.
Button(main_frame, image = photoimage, compound= LEFT).pack(side = TOP)

window.mainloop()
