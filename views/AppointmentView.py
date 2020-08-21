# Niroshan Sugirtharatnam (0410842)
import tkinter as tk
from tkinter import messagebox
from views.IViewable import IViewable
from Style import Style
from Database import Database


class AppointmentView(IViewable):
    def __init__(self, root):
        self.root = root

        # set window size
        self.root.master.minsize(900, 400)

        # get user data from db
        self.user_data = Database.get_userdata(self.root.current_user_id)

        # mount elements to screen

        self.p_username = tk.Frame(master=self.root, relief=tk.RAISED, borderwidth=1)
        self.p_username.grid(row=1, column=1, sticky="nw")

        # personal info panel
        self.p_info = tk.Frame(master=self.root, relief=tk.RAISED, borderwidth=1)
        self.p_info.grid(row=2, column=1, sticky="nw")

        self.lbl_username2 = tk.Label(master=self.p_username, text="Username: " + self.user_data["username"], font=Style.font_title, width=50)
        self.lbl_username2.grid(row=1, column=1, sticky="w", columnspan=4)

        self.lbl_first_name = tk.Label(master=self.p_info, text="First Name:", font=Style.font_key, borderwidth=1)
        self.lbl_first_name.grid(row=2, column=1, sticky="e", pady=5)
        self.lbl_first_name2 = tk.Label(master=self.p_info, text=self.user_data["first_name"], font=Style.font_regular)
        self.lbl_first_name2.grid(row=2, column=2, sticky="w", pady=5)

        self.lbl_last_name = tk.Label(master=self.p_info, text="Last Name:", font=Style.font_key)
        self.lbl_last_name.grid(row=3, column=1, sticky="e", pady=5)
        self.lbl_last_name2 = tk.Label(master=self.p_info, text=self.user_data["last_name"], font=Style.font_regular)
        self.lbl_last_name2.grid(row=3, column=2, sticky="w", pady=5)

        self.lbl_age = tk.Label(master=self.p_info, text="Age:", font=Style.font_key)
        self.lbl_age.grid(row=4, column=1, sticky="e", pady=5)
        self.lbl_age2 = tk.Label(master=self.p_info, text=self.user_data["age"], font=Style.font_regular)
        self.lbl_age2.grid(row=4, column=2, sticky="w", pady=5)

        self.lbl_city = tk.Label(master=self.p_info, text="City:", font=Style.font_key)
        self.lbl_city.grid(row=2, column=3, sticky="e", pady=5)
        self.lbl_city2 = tk.Label(master=self.p_info, text=self.user_data["city"], font=Style.font_regular)
        self.lbl_city2.grid(row=2, column=4, sticky="w", pady=5)

        self.lbl_address = tk.Label(master=self.p_info, text="Street:", font=Style.font_key)
        self.lbl_address.grid(row=3, column=3, sticky="e", pady=5)
        self.lbl_address2 = tk.Label(master=self.p_info, text=self.user_data["address"], font=Style.font_regular)
        self.lbl_address2.grid(row=3, column=4, sticky="w", pady=5)

        self.lbl_gender = tk.Label(master=self.p_info, text="Gender:", font=Style.font_key)
        self.lbl_gender.grid(row=4, column=3, sticky="e", pady=5)
        self.lbl_gender2 = tk.Label(master=self.p_info, text=self.user_data["gender"], font=Style.font_regular)
        self.lbl_gender2.grid(row=4, column=4, sticky="w", pady=5)

        # availabilities panel
        self.p_avail = tk.Frame(master=self.root, relief=tk.RAISED, borderwidth=1)
        self.p_avail.grid(row=2, column=1, padx=15, pady=35, sticky="sw")


        # setup all button functionalities
        self.__bind_event_handlers()

        # at the end, focus on the main user input
        # self.txt_username.focus()

    def unmount(self):
        # unbind then remove elements
        # self.btn_login.unbind_all("<ButtonRelease-1>")
        # self.btn_reset.unbind_all("<ButtonRelease-1>")
        # self.txt_username.unbind_all("<Return>")
        # self.txt_password.unbind_all("<Return>")
        # self.root.unbind_all("<Return>")

        self.p_username.destroy()
        self.p_info.destroy()
        self.p_avail.destroy()

    def __bind_event_handlers(self):
        # self.btn_login.bind("<ButtonRelease-1>", self.__handle_login)
        # self.btn_reset.bind("<ButtonRelease-1>", self.__handle_reset)
        # self.txt_username.bind("<Return>", self.__handle_login)
        # self.txt_password.bind("<Return>", self.__handle_login)
        # self.root.bind("<Return>", self.__handle_login)
        pass