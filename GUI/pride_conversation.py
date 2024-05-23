""" This contains the main screens and functionality of the app Pride Conversation. """

# Tkinter is for the GUI, random is for the random selection of words.
import tkinter as tk
import random

# Dictionary of words and their meanings randomly chosen to ask users.
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

# Picks a random word from the dictionary above.
word_to_display = random.choice(word_list)

# Sets up window.
window = tk.Tk()
window.geometry("300x600")
window.title("Pride Conversation")

# Functions in here.
def show_meaning_screen():
	""" Shows the meaning screen for a word after the user says if they know it or not. """
	WORD_screen.pack_forget()
	MEANING_screen.pack()

def next_word():
	""" Advances to the next word after the meaning screen. """
	global word_to_display

	word_to_display = random.choice(word_to_display)
	MEANING_screen.pack_forget()
	word_label.configure(text=word_to_display["word"])
	meaning_label.configure(text=word_to_display["meaning"])
	WORD_screen.pack()

# WORD Screen - Displays the word and the buttons for "I know this!" and "Not sure!".
WORD_screen = tk.Frame(window)
WORD_screen.pack()

# Label at the top of the word screen asking the user.
question_label = tk.Label(WORD_screen, wrap=200, text="Do you know the words used in the rainbow community?")
question_label.pack()

# Label showing the randomly selected word to the user.
word_label = tk.Label(WORD_screen, text=word_to_display["word"])
word_label.pack()

# Button to say the user knows the meaning of the word above.
yes_button = tk.Button(WORD_screen, text="I know this!", command=show_meaning_screen)
yes_button.pack()

# And another one to say that they don't.
no_button = tk.Button(WORD_screen, text="Not sure.", command=show_meaning_screen)
no_button.pack()

# MEANING screen - Displays the meaning of the words and the buttons "I got this!" and "I understood it differently".
MEANING_screen = tk.Frame(window)

# Label at the top of the meaning screen showing the user the meaning of the previous word.
meaning_label = tk.Label(MEANING_screen, text=word_to_display["meaning"])
meaning_label.pack()

# Button to say the user knew the meaning of the word above.
correct_button = tk.Button(MEANING_screen, text="I got this!", command=next_word)
correct_button.pack()

# And another one to say that they didn't.
wrong_button = tk.Button(MEANING_screen, text="I understood it differently", command=next_word)
wrong_button.pack()

# Starts the main event loop and opens the window.
window.mainloop()
