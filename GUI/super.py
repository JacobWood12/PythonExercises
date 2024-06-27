from tkinter import Tk, Button

class customButton(Button):

	def __init__(self, parent, **kwargs):
		kwargs["bg"] = 'blue'
		kwargs["fg"] = 'white'

		super().__init__(parent, **kwargs)

def main():
	root = Tk()

	button = customButton(root, text="Super")
	button.pack()

	button = customButton(root, text="Super")
	button.pack()

	root.mainloop()

main()
