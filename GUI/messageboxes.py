""" Various (I think all the) different types of messageboxes. """
# Tkinter is for the GUI.
from tkinter import Tk, Button, messagebox

# Sets up window.
window = Tk()
window.geometry("400x200")

# Functions for the buttons.
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

def showinfo():
	""" Brings up the showinfo messagebox. """
	messagebox.showinfo("This text appears nowhere.","This is an showinfo messagebox.")

def showwarning():
	""" Brings up the showwarning messagebox. """
	messagebox.showwarning("This text appears nowhere.","Bad things might happen!")

def showerror():
	""" Brings up the showerror messagebox. """
	messagebox.showerror("This text appears nowhere.","Bad things have happened!")

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

# Showinfo button.
information_btn = Button(window, text="information", command=showinfo)
information_btn.pack()

# Showwarning button.
showwarning_btn = Button(window, text="showwarning", command=showwarning)
showwarning_btn.pack()

# Showerror button.
showerror_btn = Button(window, text="showerror", command=showerror)
showerror_btn.pack()

# Starts the main event loop and opens the window.
window.mainloop()
