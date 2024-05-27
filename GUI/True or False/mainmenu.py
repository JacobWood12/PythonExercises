""" The main menu screen for the True or False game, after the user logs in. """
import tkinter as tk
from tkinter import messagebox

class MainMenuScreen(tk.Frame):
	""" The main menu screen with login, settings and exit buttons. Appears after the user enters their username and password. """
	button_width = 10
	play_game_button = settings_button = exit_button = None

	def __init__(self, **kwargs):
		""" The main menu window. """
		self.root = kwargs['master']
		super().__init__(**kwargs)

		self.play_game_button = tk.Button(self, text="Play Game", width=self.button_width, command=self.play_game)
		self.play_game_button.pack(pady=10)

		self.settings_button = tk.Button(self, text="Settings", width=self.button_width)
		self.settings_button.pack(pady=10)

		self.exit_button = tk.Button(self, text="Exit", width=self.button_width, command=self.exit)
		self.exit_button.pack(pady=10)

	def play_game(self):
		""" Starts the actual game, ran upon pressing the "Play Game" button. """
		print("Play Game")
		self.root.event_generate("<<PlayGame>>")

	def exit(self):
		""" Closes the window with confirmation, run upon pressing the "Exit" button. """
		answer = messagebox.askyesno("Exit","Are you sure you want to exit?")

		if answer == True:
			print("Exit app")
			self.root.destroy()
