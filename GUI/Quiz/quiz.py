# Import tkinter for GUI.
from tkinter import *
        # Sets up frame.
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

# Start of program.
if __name__ == "__main__":
    root = Tk()
    # Title of window.
    root.title("Quiz")
    root.mainloop()