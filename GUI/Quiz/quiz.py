# Import tkinter for GUI.
from tkinter import *

class quizStarter:
    def __init__(self, parent):
        # Sets window background colour to a dark red.
        background_colour="#C73D2D"
        # Sets up frame.
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame, text = "Quiz.", font=()) #Remember to choose a font.

# Start of program.
if __name__ == "__main__":
    root = Tk()
    # Title of window.
    root.title("Quiz")
    root.mainloop()