# Imports tkinter for GUI.
from tkinter import *

class Student:
    def __init__(self, name):
        self.first_name = name
    
    def display_name(self):
        print(self.first_name)

    def set_grade(self, grade):
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
def show_grade():
    # Show grade using a label.
    grade_label.config(text=csc_l2[0].get_grade())
    pass


csc_l2 = []

csc_l2.append(Student("Jacob"))
csc_l2[0].set_grade("Excellence.")

window = Tk()
window.geometry("300x300")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade.", command=show_grade)
show_grade_btn.pack()

window.mainloop()