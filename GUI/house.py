''' Tkinter is for the GUI. '''
from tkinter import *

w_width = 500
w_height = 700

bg_color = "#E7DDFF"

window = Tk()
window.geometry(str(w_width) + "x" + str(w_height))
window.title("My App")

main_frame=Frame(background=bg_color, width=w_width, height=w_height)
main_frame.pack()

# Adding widgets to the root window
Label(main_frame, text = "House", font =(
	"Verdana", 15)).pack(side = TOP, pady = 10)

# Creating a photoimage object to use image
photo = PhotoImage(file = r"/Users/jacobwood/Documents/Programming/PythonExercises/GUI/house.png")

# Resizing image to fit on button
photoimage = photo.subsample(3,3)

# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
Button(main_frame, image = photoimage,
	   compound= LEFT).pack(side = TOP)

window.mainloop()
