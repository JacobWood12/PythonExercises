# Import tkinter for GUI.
from tkinter import *
# Import randow to pick questions in a random order.
import random

# Names will be put in here later for scoreboard etc.
names = []
global questions_answers
# Will store questions that have already been asked so they don't get randomly picked again.
asked = []
score = int(0)

class QuizStarter:
    def __init__(self, parent):
        # Sets window background colour to a dark red.
        background_colour="#C73D2D"

        # Sets up frame.
        self.quiz_frame = Frame(parent, bg = background_colour, padx=100, pady=100)
        self.quiz_frame.grid()

        # Heading label widget.
        self.heading_label = Label(self.quiz_frame, text = "Quiz.", font=("Futura", "18", "bold"), bg=background_colour)
        self.heading_label.grid(row=0, padx=20)

        # Stores radio button values.
        self.var1=IntVar()

        # Username label.
        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Futura", "16"), bg=background_colour)
        self.user_label.grid(row=1, padx=20, pady=20)

        # Answer entry box.
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)

        # Continue button.
        self.continue_button = Button(self.quiz_frame, text="Continue.", font=("Roboto Slab", "13", "bold"), bg="orange", command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)

        # Radio button 1.
        self.rb1= Radiobutton(self.quiz_frame, text=questions_answers [qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, padx=10, pady=10,
            variable=self.var1, indicator = 0, background = "light blue")
        self.rb1.grid(row=2, sticky=W)

        # Radio button 2.
        self.rb2= Radiobutton(self.quiz_frame, text=questions_answers [qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, padx=10, pady=10,
            variable=self.var1, indicator = 0, background = "light blue")
        self.rb1.grid(row=2, sticky=W)

        # Radio button 3.
        self.rb3= Radiobutton(self.quiz_frame, text=questions_answers [qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, padx=10, pady=10,
            variable=self.var1, indicator = 0, background = "light blue")
        self.rb1.grid(row=3, sticky=W)

        # Radio button 4.
        self.rb4= Radiobutton(self.quiz_frame, text=questions_answers [qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, padx=10, pady=10,
            variable=self.var1, indicator = 0, background = "light blue")
        self.rb1.grid(row=4, sticky=W)

        # Confirm button.
        self.quiz_instance = Button(self.quiz_frame, text="Confirm.", font=("Roboto Slab", "13", "bold"), bg="SpringGreen3") # command="command=self.test_progress") to add.
        self.quiz_instance.grid(row=7, padx=5, pady=5)

        # Score label.
        self.score_label=Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT", "16"), bg=background_color)
        self.score_label.grid(row=8, padx=10, pady=1)
    
    def name_collection(self):
        name=self.entry_box.get()
        # Adds name entered earlier into previously empty names dictionary.
        names.append(name)
        # Closes starter window.
        self.quiz_frame.destroy()


def randomiser():
    # Makes this function used the qnum variable from elsewhere.
    global qnum
    # Picks a random order of questions.
    qnum = random.randint (1,10)
    # Checks question selected against previously asked question so they're not asked twice.
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser ()

randomiser()

# Start of program.
if __name__ == "__main__":
    root = Tk()
    # Title of window.
    root.title("Quiz")
    # Makes an instance of the QuizStarter class.
    quiz_instance = QuizStarter(root)
    # Keeps window from closing.
    root.mainloop()