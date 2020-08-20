# Niroshan Sugirtharatnam (0410842)
import tkinter as tk
from views.LoginView import LoginView


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.current_view = None
        self.setup()
        self.pack()

    def setup(self):
        self.master.title("Doctor's Appointment App")
        self.master.maxsize(800, 600)
        self.master.minsize(800, 600)

    # Sign up screen
    def switch_to_registration(self):
        if self.current_view is not None:
            self.current_view.unmount()

        # TODO: add this view
        # self.current_route =

    # Login screen
    def switch_to_login(self):
        if self.current_view is not None:
            self.current_view.unmount()

        self.current_view = LoginView(self)

    # Appointment screen
    def switch_to_appointments(self):
        if self.current_view is not None:
            self.current_view.unmount()

        # TODO: add this view
        # self.current_route =
