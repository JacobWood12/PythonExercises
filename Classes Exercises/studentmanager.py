""" Imports tkinter for GUI. """
from tkinter import Tk, Listbox, Label, Button

class Student:
    """ Starts the student class. """

    def __init__(self, name):
        self.name = name
        self.grade = None

    def get_grade(self):
        """ Returns grade of selected student. """
        return self.grade

    def set_grade(self, grade):
        """ Sets grade of student. """
        self.grade = grade

    def display_name(self):
        """ Displays student's names. """
        print(self.name)
    
def show_grade():
    " Shows student's grades. Currently only show's the first student's grades (me). "
    # Show grade using a label.
    grade_label.config(text=csc_2[0].get_grade())

# Starts the dictionary with currently no students.
csc_2 = []

# Adds me as a student with Excellence.
csc_2.append(Student("Jacob."))
csc_2[0].set_grade("Excellence.")

# Adds Ken as a student with a grade of Achieved (he asked for it).
csc_2.append(Student("Ken."))
csc_2[1].set_grade("Achieved.")

# Sets up window.
window = Tk()
window.geometry("300x300")

# Sets up listbox.
students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0, "Jacob.")
students_listbox.insert(1, "Ken.")

# Sets up grade label.
grade_label = Label()
grade_label.pack()

# Show grade button.
show_grade_btn = Button(text="Show Grade.", command=show_grade)
show_grade_btn.pack()

window.mainloop()