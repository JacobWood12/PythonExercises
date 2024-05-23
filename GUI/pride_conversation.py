""" This contains the main screens and functionality of the app Pride Conversation. """

import tkinter as tk
import random

word_list = [
	{
		"word": "Word 1",
		"meaning": "Meaning of Word 1"
	},
	{
		"word": "Word 2",
		"meaning": "Meaning of Word 2"
	},
	{
		"word": "Word 3",
		"meaning": "Meaning of Word 3"
	},
]

window = tk.Tk()
window.geometry("300x600")
window.title("Pride Conversation")

word_to_display = random.choice(word_list)

question_label = tk.Label(wrap=200, text="Do you know the words used in the rainbow community?")
question_label.pack()

word_label = tk.Label(text=word_to_display["word"])
word_label.pack()

yes_button = tk.Button(text="I know this!")
yes_button.pack()

no_button = tk.Button(text="Not sure.")
no_button.pack()

window.mainloop()
