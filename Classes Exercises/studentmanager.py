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
    grade_label.config(text=csc_2[0].get_grade())

# Starts the dictionary with currently no students.
csc_2 = []

# Adds me as a student with Excellence.
csc_2.append(Student("Jacob"))
csc_2[0].set_grade("Excellence.")

# Adds Ken as a student with a grade of Achieved (he asked for it).
csc_2.append(Student("Ken"))
csc_2[1].set_grade("Achieved.")

# Sets up window.
window = Tk()
window.geometry("300x300")

grade_label = Label()
grade_label.pack()

# Show grade button.
show_grade_btn = Button(text="Show Grade.", command=show_grade)
show_grade_btn.pacck()

window.mainloop()