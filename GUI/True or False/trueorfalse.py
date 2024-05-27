import tkinter as tk
from tkinter import messagebox
from true_or_false_questions import questions


class TrueOrFalseGame(tk.Frame):

    button_width = 10
    question_label = feedback_label = None
    true_button = false_button = exit_button = next_button = None
    current_question_index = 0 # Start with the first question

    def __init__(self, **kwargs):

        self.root = kwargs['master']
        super().__init__(**kwargs)

        self.question_label = tk.Label(self, wrap=200, text=questions[self.current_question_index]["statement"], background=kwargs['background'])
        self.question_label.place(relx=0.5, y=15, anchor = tk.CENTER)

        self.true_button = tk.Button(self, text="True", width=self.button_width, command=lambda: self.check_answer(True))
        self.true_button.place(x=25, y=50)

        self.false_button = tk.Button(self, text="False", width=self.button_width, command=lambda: self.check_answer(False))
        self.false_button.place(x=150, y=50)

        # Only display feedback and Next bubtton after user answered
        self.feedback_label = tk.Label(self, wrap=200, text=questions[self.current_question_index]["feedback"], background=kwargs['background'])
        self.next_button = tk.Button(self, text="Next", width=self.button_width, command=self.next_question)

        self.exit_button = tk.Button(self, text="Quit Game", width=self.button_width, command=self.exit)
        self.exit_button.place(relx=0.5, y=200, anchor = tk.S)

    def check_answer(self, answer):
        
        if(questions[self.current_question_index]["answer"] == answer):
            print("CORRECT")
        else:
            print("WRONG")

        # Show feedback
        self.feedback_label.configure(text=questions[self.current_question_index]["feedback"])
        self.feedback_label.place(relx=0.5, y=100, anchor = tk.CENTER)

        # Show next button
        self.next_button.place(relx=0.5, y=150, anchor = tk.CENTER)

    def next_question(self):
        # Hide feedback and Next button
        self.feedback_label.place_forget()
        self.next_button.place_forget()

        # Replace question
        self.current_question_index = (self.current_question_index + 1) % len(questions)
        self.question_label.configure(text=questions[self.current_question_index]["statement"])
        

    def exit(self):
        answer = messagebox.askyesno("Exit","Are you sure you want to quit the game?")

        if answer == True:
            print("Quit game")
            self.root.destroy()
        
