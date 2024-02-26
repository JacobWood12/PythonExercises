from tkinter import *
clicks = int(0)

def btn_click():
	global clicks
	clicks = int(clicks + 1)
	if clicks == 1:
		print("Button clicked once. You're safe.")
	else:
		print(f"Button clicked {clicks} times. You're safe.")

window = Tk()
btn = Button(window, text="Click me or else.", command=btn_click)
btn.pack()

window.mainloop()
