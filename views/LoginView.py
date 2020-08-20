# Niroshan Sugirtharatnam (0410842)
import tkinter as tk
from tkinter import messagebox
from views.IViewable import IViewable
from Style import Style
from Database import Database


class LoginView(IViewable):
    def __init__(self, root):
        self.root = root

        # set window size
        # self.root.master.maxsize(600, 250)
        self.root.master.minsize(600, 250)

        # mount elements to screen

        # keep reference to all containers, they must all be unmounted when screen gets switche
        self.login_frame = tk.Frame(master=self.root, relief=tk.RAISED, borderwidth=0)
        self.login_frame.grid(row=1, column=1, padx=15, pady=35)

        self.lbl_login_title = tk.Label(master=self.login_frame, text="Login", font=Style.font_title)
        self.lbl_login_title.grid(row=1, column=1, sticky="w", columnspan=3)

        self.lbl_username = tk.Label(master=self.login_frame, text="Username:", font=Style.font_regular)
        self.lbl_username.grid(row=2, column=1, sticky="w", pady=10)

        self.txt_username = tk.Entry(master=self.login_frame, width=30, font=Style.font_regular)
        self.txt_username.grid(row=2, column=2, columnspan=2)

        self.lbl_password = tk.Label(master=self.login_frame, text="Password:", font=Style.font_regular)
        self.lbl_password.grid(row=3, column=1, sticky="w")

        self.txt_password = tk.Entry(master=self.login_frame, show="\u2022", width=30, font=Style.font_regular)
        self.txt_password.grid(row=3, column=2, columnspan=2)

        self.btn_login = tk.Button(master=self.login_frame, width=12, text="Login", font=Style.font_regular)
        self.btn_login.grid(row=4, column=2, pady=15)

        self.btn_reset = tk.Button(master=self.login_frame, width=12, text="Clear", font=Style.font_regular)
        self.btn_reset.grid(row=4, column=3, pady=15)

        # setup all button functionalities
        self.__bind_event_handlers()

        # at the end, focus on the main user input
        self.txt_username.focus()

    def unmount(self):
        # unbind then remove elements
        self.btn_login.unbind_all("<ButtonRelease-1>")
        self.btn_reset.unbind_all("<ButtonRelease-1>")
        self.txt_username.unbind_all("<Return>")
        self.txt_password.unbind_all("<Return>")
        self.root.unbind_all("<Return>")

        self.login_frame.destroy()

    def __bind_event_handlers(self):
        self.btn_login.bind("<ButtonRelease-1>", self.__handle_login)
        self.btn_reset.bind("<ButtonRelease-1>", self.__handle_reset)
        self.txt_username.bind("<Return>", self.__handle_login)
        self.txt_password.bind("<Return>", self.__handle_login)
        self.root.bind("<Return>", self.__handle_login)

    def __handle_login(self, _):
        user_id = Database.verify_login_credentials(self.txt_username.get(), self.txt_password.get())

        if user_id is not False:
            # correct credentials
            self.root.current_user_id = user_id
            self.root.switch_to_appointments()
        else:
            # no bueno
            messagebox.showerror(title="Login Error", message="Username/Password not found!")

    def __handle_reset(self, _):
        self.txt_password.delete(0, tk.END)
        self.txt_username.delete(0, tk.END)
        self.txt_username.focus()
