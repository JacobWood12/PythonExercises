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

word_to_display = random.choice(word_list)

window = tk.Tk()
window.geometry("300x600")
window.title("Pride Conversation")

# Functions

def show_meaning_screen():
	WORD_screen.pack_forget()
	MEANING_screen.pack()

def next_word():
	global word_to_display

	word_to_display = random.choice(word_to_display)
	MEANING_screen.pack_forget()
	word_label.configure(text=word_to_display["word"])
	meaning_label.configure(text=word_to_display["meaning"])
	WORD_screen.pack()

# WORD Screen - Displays the word and the buttons for 'I know this!' and 'Not sure!'
WORD_screen = tk.Frame(window)
WORD_screen.pack()


question_label = tk.Label(WORD_screen, wrap=200, text="Do you know the words used in the rainbow community?")
question_label.pack()

word_label = tk.Label(WORD_screen, text=word_to_display["word"])
word_label.pack()

yes_button = tk.Button(WORD_screen, text="I know this!", command=show_meaning_screen)
yes_button.pack()

no_button = tk.Button(WORD_screen, text="Not sure.", command=show_meaning_screen)
no_button.pack()

# MEANING screen - Displays the meaning of the words and the buttons 'I got this!' and 'I understood it differently'
MEANING_screen = tk.Frame(window)

meaning_label = tk.Label(MEANING_screen, text=word_to_display["meaning"])
meaning_label.pack()

correct_button = tk.Button(MEANING_screen, text="I got this!", command=next_word)
correct_button.pack()

wrong_button = tk.Button(MEANING_screen, text="I understood it differently", command=next_word)
wrong_button.pack()

window.mainloop()
