# Imports tkinter for GUI.
from tkinter import *

# Starts the student class.
class Student:

    def __init__(self, name):
        self.name = name

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def display_name(self):
        print(self.first_name)
    
def show_grade():
    # Show grade using a label.
    grade_label.config(text=csc_l2[0].get_grade())
    pass


# Starts the dictionary with currently no students.
csc_l2 = []

# Adds me as a student with Excellence.
csc_l2.append(Student("Jacob"))
csc_l2[0].set_grade("Excellence.")

# Adds Ken as a student with a grade of Achieved (he asked for it).
csc_l2.append(Student("Ken"))
csc_l2[1].set_grade("Achieved.")

# Sets up window.
window = Tk()
window.geometry("300x300")

grade_label = Label()
grade_label.pack()

# This isn't finished.
grades_list = tk.listbox

window.mainloop()