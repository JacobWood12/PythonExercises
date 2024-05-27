import tkinter as tk
from login import *
from mainmenu import *
from trueorfalse import *

bg_color = "white"
app_width = 300
app_height = 500

current_screen = None

window = tk.Tk()
window.geometry(str(app_width) + "x" + str(app_height))
window.configure(background=bg_color)


app_title = tk.Label(text="True or False", font=("Arial",18), background=bg_color)
app_title.pack(pady=100)


# Initialise first screen - Login
login_screen = LoginScreen(master=window, background=bg_color)

# Initialise other screens
main_menu_screen = MainMenuScreen(master=window, background=bg_color)
game_screen = TrueOrFalseGame(master=window, width=250, height=200, background=bg_color)

current_screen = login_screen
current_screen.place(relx=.5, rely=.5,anchor=tk.CENTER)

# Note: For consistency, Frames will only use place()

def login_success(*args):
    print("Go to main menu")
    global main_menu_screen
    switch_screen(main_menu_screen)

def switch_screen(new_screen):
    global current_screen
    current_screen.place_forget()
    current_screen = new_screen
    current_screen.place(relx=.5, rely=.5,anchor=tk.CENTER)

def start_new_game(*args):
    print("Starting new game...")
    global game_screen
    switch_screen(game_screen)
    

window.bind("<<LoginSuccess>>", login_success)
window.bind("<<PlayGame>>", start_new_game)

window.mainloop()
