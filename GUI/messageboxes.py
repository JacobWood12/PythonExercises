""" Various (I think all the) different types of messageboxes. """
# Tkinter is for the GUI.
from tkinter import Tk, Button, messagebox

# Sets up window.
window = Tk()
window.geometry("400x200")

def askokcancel():
	""" Brings up the Askokcancel messagebox. """
	messagebox.askokcancel("This text appears nowhere.","Continue?")

def askquestion():
	""" Brings up the Askquestion messagebox. """
	messagebox.askquestion("This text appears nowhere.","Hi.")

def askretrycancel():
	""" Brings up the Askretrycancel messagebox. """
	messagebox.askretrycancel("This text appears nowhere.", "Goodbye.")

def askyesno():
	""" Brings up the Askyesno messagebox. """
	messagebox.askyesno("This text appears nowhere.", "Is this working?")

def askyesnocancel():
	""" Brings up the Askyesnocancel messagebox. """
	messagebox.askyesnocancel("This text appears nowhere?","Should your computer explode?")

# Creates buttons in the window.
# Askokcancel button.
askokcancel_btn = Button(window, text="askokcancel", command=askokcancel)
askokcancel_btn.pack()

# Askquestion button.
askquestion_btn = Button(window, text="askquestion", command=askquestion)
askquestion_btn.pack()

# Askretrycancel button.
askretrycancel_btn = Button(window, text="askretrycancel", command=askretrycancel)
askretrycancel_btn.pack()

# Askyesno button.
askyesno_btn = Button(window, text="askyesno", command=askyesno)
askyesno_btn.pack()

# Askyesnocancel button.
askyesnocancel_btn = Button(window, text="askyesnocancel", command=askyesnocancel)
askyesnocancel_btn.pack()

# Starts the main event loop and opens the window.
window.mainloop()
