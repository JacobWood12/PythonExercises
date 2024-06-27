""" Uses super init to create custom buttons. """
# Tkinter is for the GUI.
from tkinter import Tk, Button

class customButton(Button):
	""" Custom button class. """
	def __init__(self, parent, **kwargs):
		kwargs["bg"] = 'blue'
		kwargs["fg"] = 'white'

		super().__init__(parent, **kwargs)

def main():
	""" The main window. """
	root = Tk()

	button = customButton(root, text="Super")
	button.pack()

	button = customButton(root, text="Super")
	button.pack()

	root.mainloop()

main()
