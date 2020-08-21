# Niroshan Sugirtharatnam (0410842)
import tkinter as tk
from tkinter import messagebox
from views.IViewable import IViewable
from Style import Style
from Database import Database


class RegistrationView(IViewable):
    def __init__(self, root):
        self.root = root

        # set window size
        self.root.master.minsize(600, 580)

        self.gender = tk.IntVar()

        # mount elements to screen

        # keep reference to all containers, they must all be unmounted when screen gets switche
        self.registration_frame = tk.Frame(master=self.root, relief=tk.RAISED, borderwidth=0)
        self.registration_frame.grid(row=1, column=1, padx=15, pady=35)

        self.lbl_registration_title = tk.Label(master=self.registration_frame, text="Sign Up", font=Style.font_title)
        self.lbl_registration_title.grid(row=1, column=1, sticky="w", columnspan=3, pady=20)

        # New Section
        self.lbl_first_name = tk.Label(master=self.registration_frame, text="First Name:", font=Style.font_regular)
        self.lbl_first_name.grid(row=2, column=1, sticky="w", pady=5)

        self.txt_first_name = tk.Entry(master=self.registration_frame, width=30, font=Style.font_regular)
        self.txt_first_name.grid(row=2, column=2, columnspan=2)

        # New Section
        self.lbl_last_name = tk.Label(master=self.registration_frame, text="Last Name:", font=Style.font_regular)
        self.lbl_last_name.grid(row=3, column=1, sticky="w", pady=5)

        self.txt_last_name = tk.Entry(master=self.registration_frame, width=30, font=Style.font_regular)
        self.txt_last_name.grid(row=3, column=2, columnspan=2)

        # New Section
        self.lbl_age = tk.Label(master=self.registration_frame, text="Age:", font=Style.font_regular)
        self.lbl_age.grid(row=4, column=1, sticky="w", pady=5)

        self.txt_age = tk.Entry(master=self.registration_frame, width=30, font=Style.font_regular)
        self.txt_age.grid(row=4, column=2, columnspan=2)

        # New Section
        self.lbl_gender = tk.Label(master=self.registration_frame, text="Gender:", font=Style.font_regular)
        self.lbl_gender.grid(row=5, column=1, sticky="w", pady=5)

        # new section gender
        self.radio_gender_male = tk.Radiobutton(text="Male", variable=self.gender, value=0, master=self.registration_frame, font=Style.font_regular)
        self.radio_gender_male.grid(row=5, column=2, sticky="w")

        self.radio_gender_female = tk.Radiobutton(text="Female", variable=self.gender, value=1, master=self.registration_frame, font=Style.font_regular)
        self.radio_gender_female.grid(row=6, column=2, sticky="w")

        # New Section
        self.lbl_city = tk.Label(master=self.registration_frame, text="City:", font=Style.font_regular)
        self.lbl_city.grid(row=7, column=1, sticky="w", pady=5)

        self.txt_city = tk.Entry(master=self.registration_frame, width=30, font=Style.font_regular)
        self.txt_city.grid(row=7, column=2, columnspan=2)

        # New Section
        self.lbl_address = tk.Label(master=self.registration_frame, text="Address:", font=Style.font_regular)
        self.lbl_address.grid(row=8, column=1, sticky="w", pady=5)

        self.txt_address = tk.Entry(master=self.registration_frame, width=30, font=Style.font_regular)
        self.txt_address.grid(row=8, column=2, columnspan=2)

        # New Section
        self.lbl_username = tk.Label(master=self.registration_frame, text="Username:", font=Style.font_regular)
        self.lbl_username.grid(row=9, column=1, sticky="w", pady=5)

        self.txt_username = tk.Entry(master=self.registration_frame, width=30, font=Style.font_regular)
        self.txt_username.grid(row=9, column=2, columnspan=2)

        # New Section
        self.lbl_password = tk.Label(master=self.registration_frame, text="Password:", font=Style.font_regular)
        self.lbl_password.grid(row=10, column=1, sticky="w", pady=5)

        self.txt_password = tk.Entry(master=self.registration_frame, show="\u2022", width=30, font=Style.font_regular)
        self.txt_password.grid(row=10, column=2, columnspan=2)

        # New Section
        self.lbl_password2 = tk.Label(master=self.registration_frame, text="Verify Password:", font=Style.font_regular)
        self.lbl_password2.grid(row=11, column=1, sticky="w", pady=5)

        self.txt_password2 = tk.Entry(master=self.registration_frame, show="\u2022", width=30, font=Style.font_regular)
        self.txt_password2.grid(row=11, column=2, columnspan=2)

        # Les Buttons
        self.btn_signup = tk.Button(master=self.registration_frame, width=12, text="Sign Up", font=Style.font_regular)
        self.btn_signup.grid(row=12, column=2, pady=10)

        self.btn_reset = tk.Button(master=self.registration_frame, width=12, text="Clear", font=Style.font_regular)
        self.btn_reset.grid(row=12, column=3, pady=10)

        # setup all button functionalities
        self.__bind_event_handlers()

        # at the end, focus on the main user input
        self.txt_age.insert(0, "0")
        self.txt_first_name.focus()

    def unmount(self):
        # unbind then remove elements
        self.btn_signup.unbind_all("<ButtonRelease-1>")
        self.btn_signup.unbind_all("<Return>")
        self.btn_signup.unbind_all("<space>")
        self.btn_reset.unbind_all("<ButtonRelease-1>")
        self.root.unbind_all("<Return>")
        self.txt_password2.unbind_all("<Return>")

        self.registration_frame.destroy()

    @staticmethod
    def __show_validation_error_message(msg):
        messagebox.showerror(title="Sign Up Error", message=msg)

    def __bind_event_handlers(self):
        self.btn_signup.bind("<ButtonRelease-1>", self.__handle_login)
        self.btn_signup.bind("<Return>", self.__handle_login)
        self.btn_signup.bind("<space>", self.__handle_login)
        self.btn_reset.bind("<ButtonRelease-1>", self.__handle_reset)
        self.root.bind("<Return>", self.__handle_login)
        self.txt_password2.bind("<Return>", self.__handle_login)

    def __handle_login(self, _):
        first_name = self.txt_first_name.get().strip()
        last_name = self.txt_last_name.get().strip()
        age = int("0" if self.txt_age.get().strip() == "" else self.txt_age.get().strip())
        gender = "Female" if self.gender == 1 else "Male"
        address = self.txt_address.get().strip()
        city = self.txt_city.get().strip()
        username = self.txt_username.get().strip()
        password = self.txt_password.get().strip()
        password2 = self.txt_password2.get().strip()

        # validate inputs
        valid = True
        if len(first_name) < 2 or len(first_name) > 25:
            RegistrationView.__show_validation_error_message("First name looks invalid")
            valid = False
        elif len(last_name) < 2 or len(last_name) > 25:
            RegistrationView.__show_validation_error_message("Last name looks invalid")
            valid = False
        elif age < 0 or age > 150:
            RegistrationView.__show_validation_error_message("Age looks invalid")
            valid = False
        elif len(city) < 2 or len(city) > 25:
            RegistrationView.__show_validation_error_message("City looks invalid")
            valid = False
        elif len(address) < 5 or len(address) > 25:
            RegistrationView.__show_validation_error_message("Address looks invalid")
            valid = False
        elif len(username) < 4 or len(username) > 25:
            RegistrationView.__show_validation_error_message("Username must be between 3 & 25 characters long")
            valid = False
        elif len(password) < 4 or len(password) > 25:
            RegistrationView.__show_validation_error_message("Password must be between 4 & 25 characters long")
            valid = False
        elif password != password2:
            RegistrationView.__show_validation_error_message("Passwords do not match")
            valid = False

        # save to db
        if valid:
            new_user_id = Database.register_user(
                first_name,
                last_name,
                age,
                gender,
                address,
                city,
                username,
                password
            )

            # database handles showing the correct error message
            if new_user_id is not False:
                # autologin and switch to appointments screen
                self.root.current_user_id = new_user_id
                self.root.switch_to_appointments()

    def __handle_reset(self, _):
        self.txt_first_name.delete(0, tk.END)
        self.txt_last_name.delete(0, tk.END)
        self.txt_age.delete(0, tk.END)
        self.txt_username.delete(0, tk.END)
        self.txt_password.delete(0, tk.END)
        self.txt_address.delete(0, tk.END)
        self.txt_city.delete(0, tk.END)
        self.gender.set(0)
        self.txt_age.insert(0, "0")

        self.txt_first_name.focus()
