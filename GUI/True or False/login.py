""" Contains the login screen for the True or False game. """
import tkinter as tk

class LoginScreen(tk.Frame):
    """ Contains the login screen window, and checks the username and password. """
    username_label = username_entry = None
    password_label = password_entry = None
    error_label = None
    root = None
    
    def __init__(self, **kwargs):
        """ Sets up the login screen window."""
        
        self.root = kwargs['master']
        super().__init__(**kwargs)
        
        # Create the widgets
        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self,text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self,show="🍏")
        self.password_entry.pack()

        self.login_button = tk.Button(self,text="Login", command=self.verify_login)
        self.login_button.pack()

        self.error_label = tk.Label(self, text="There was an error", fg="red")
        
    def verify_login(self):
        """ Checks the user-entered username and password against the stored options. """
        print("Verifying login...")
        if self.username_entry.get() == "admin" and self.password_entry.get() == "pass":
            self.root.event_generate("<<LoginSuccess>>")
            print("Login successful...")
        else:
            print("")
            self.error_label.pack()
