# Niroshan Sugirtharatnam (0410842)
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from views.IViewable import IViewable
from helpers.Style import Style
from helpers.Database import Database
from datetime import datetime, date
from time import mktime, strftime, localtime


class AppointmentView(IViewable):
    def __init__(self, root):
        self.root = root

        # set window size
        self.root.master.minsize(900, 600)

        # get user data from db
        self.user_data = Database.get_userdata(self.root.current_user_id)

        # mount elements to screen

        # panel just for username to take up the top
        self.p_username = tk.Frame(master=self.root, relief=tk.RAISED, borderwidth=1)
        self.p_username.grid(row=1, column=1, sticky="we", columnspan=2)

        # personal info panel
        self.p_info = tk.Frame(master=self.root, relief=tk.RAISED, borderwidth=1)
        self.p_info.grid(row=2, column=1, sticky="nw")

        self.lbl_username2 = tk.Label(master=self.p_username, text="Username: " + self.user_data["username"], font=Style.font_title, width=50)
        self.lbl_username2.grid(row=1, column=1, sticky="we", columnspan=4)

        self.lbl_first_name = tk.Label(master=self.p_info, text="First Name:", font=Style.font_key, borderwidth=1)
        self.lbl_first_name.grid(row=2, column=1, sticky="w", pady=5)
        self.lbl_first_name2 = tk.Label(master=self.p_info, text=self.user_data["first_name"], font=Style.font_regular)
        self.lbl_first_name2.grid(row=2, column=2, sticky="w", pady=5, padx=15)

        self.lbl_last_name = tk.Label(master=self.p_info, text="Last Name:", font=Style.font_key)
        self.lbl_last_name.grid(row=3, column=1, sticky="w", pady=5)
        self.lbl_last_name2 = tk.Label(master=self.p_info, text=self.user_data["last_name"], font=Style.font_regular)
        self.lbl_last_name2.grid(row=3, column=2, sticky="w", pady=5, padx=15)

        self.lbl_age = tk.Label(master=self.p_info, text="Age:", font=Style.font_key)
        self.lbl_age.grid(row=4, column=1, sticky="w", pady=5)
        self.lbl_age2 = tk.Label(master=self.p_info, text=self.user_data["age"], font=Style.font_regular)
        self.lbl_age2.grid(row=4, column=2, sticky="w", pady=5, padx=15)

        self.lbl_city = tk.Label(master=self.p_info, text="City:", font=Style.font_key)
        self.lbl_city.grid(row=2, column=3, sticky="w", pady=5, padx=25)
        self.lbl_city2 = tk.Label(master=self.p_info, text=self.user_data["city"], font=Style.font_regular)
        self.lbl_city2.grid(row=2, column=4, sticky="w", pady=5)

        self.lbl_address = tk.Label(master=self.p_info, text="Street:", font=Style.font_key)
        self.lbl_address.grid(row=3, column=3, sticky="w", pady=5, padx=25)
        self.lbl_address2 = tk.Label(master=self.p_info, text=self.user_data["address"], font=Style.font_regular)
        self.lbl_address2.grid(row=3, column=4, sticky="w", pady=5)

        self.lbl_gender = tk.Label(master=self.p_info, text="Gender:", font=Style.font_key)
        self.lbl_gender.grid(row=4, column=3, sticky="w", pady=5, padx=25)
        self.lbl_gender2 = tk.Label(master=self.p_info, text=self.user_data["gender"], font=Style.font_regular)
        self.lbl_gender2.grid(row=4, column=4, sticky="w", pady=5)

        self.padding = tk.Label(master=self.p_info)
        self.padding.grid(row=4, column=5, padx=15)

        # appointments panel
        self.p_apmt = tk.Frame(master=self.root, relief=tk.RAISED, borderwidth=1)
        self.p_apmt.grid(row=2, column=2, sticky="nswe", rowspan=2)

        self.lbl_apt_title = tk.Label(master=self.p_apmt, text="Book an Appointment", font=Style.font_title)
        self.lbl_apt_title.grid(row=1, column=1, sticky="w", columnspan=2, pady=10)

        # populated by values from the db
        self.available_doctors = {} # use the available doctors as reference. it contains the id associated with the selected dr index
        self.doctors = []
        self.doctor_value = tk.StringVar()

        self.lbl_doctor = tk.Label(master=self.p_apmt, text="Doctor:", font=Style.font_key)
        self.lbl_doctor.grid(row=2, column=1, sticky="w")
        self.cbo_doctors = ttk.Combobox(master=self.p_apmt, value=self.doctors, font=Style.font_regular, state="readonly", textvariable=self.doctor_value)
        self.cbo_doctors.grid(row=2, column=2, sticky="we")

        self.lbl_day = tk.Label(master=self.p_apmt, text="Day:", font=Style.font_key)
        self.lbl_day.grid(row=3, column=1, sticky="w")
        self.txt_day = tk.Entry(master=self.p_apmt, font=Style.font_regular)
        self.txt_day.grid(row=3, column=2, sticky="we")

        self.lbl_month = tk.Label(master=self.p_apmt, text="Month:", font=Style.font_key)
        self.lbl_month.grid(row=4, column=1, sticky="w")

        self.months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        self.month_value = tk.StringVar()

        self.cbo_month = ttk.Combobox(master=self.p_apmt, value=self.months, font=Style.font_regular, state="readonly", textvariable=self.month_value)
        self.cbo_month.grid(row=4, column=2, sticky="we")

        self.lbl_year = tk.Label(master=self.p_apmt, text="Year:", font=Style.font_key)
        self.lbl_year.grid(row=5, column=1, sticky="w")
        self.txt_year = tk.Entry(master=self.p_apmt, font=Style.font_regular)
        self.txt_year.grid(row=5, column=2, sticky="we")

        self.btn_search_apmt = tk.Button(master=self.p_apmt, font=Style.font_regular, text="Search")
        self.btn_search_apmt.grid(row=6, column=1, sticky="we", columnspan=2, pady=10, padx=5)

        # self.cbo_month.state(statespec=)

        # user's appointments list
        self.p_user_apts = tk.Frame(master=self.root, relief=tk.RAISED, borderwidth=1)
        self.p_user_apts.grid(row=3, column=1, sticky="nw")

        self.lbl_schedule_title = tk.Label(master=self.p_user_apts, text=self.user_data['username'] + "'s Appointments", font=Style.font_title)
        self.lbl_schedule_title.grid(row=1, column=1, sticky="we", columnspan=3)

        self.user_schedules = {}


        # start booking search from today's date
        today = date.today()
        self.txt_day.insert(0, today.strftime("%d"))
        self.month_value.set(today.strftime("%B"))
        self.txt_year.insert(0, today.strftime("%Y"))

        # initialize list used for adding dynamically createing buttons and labels for booking
        self.schedules = {}

        # setup all button functionalities
        self.__bind_event_handlers()

        # at the end, focus on the main user input
        # self.txt_username.focus()

        self.__build_doctors_list()
        self.__show_users_appointments()


    def unmount(self):
        # unbind then remove elements
        self.btn_search_apmt.unbind_all("<ButtonRelease-1>")

        self.p_username.destroy()
        self.p_info.destroy()
        self.p_apmt.destroy()

    def __bind_event_handlers(self):
        self.btn_search_apmt.bind("<ButtonRelease-1>", self.__handle_search_available_bookings)

    def __handle_search_available_bookings(self, _):
        self.__build_schedule(self.search_available_bookings())

    def search_available_bookings(self):
        time_string = self.month_value.get() + " " + self.txt_day.get().zfill(2) + " " + self.txt_year.get()
        time_format = "%B %d %Y"
        try:
            a = datetime.strptime(time_string, time_format)
        except ValueError:
            messagebox.showerror(title="Invalid Date", message="The date looks invalid")
            return

        starting_timestring = time_string + " 10:00:00 +0400"
        ending_timestring = time_string + " 15:00:00 +0400"
        start_timestamp = mktime(datetime.strptime(starting_timestring, time_format + " %H:%M:%S %z").timetuple())
        ending_timestamp = mktime(datetime.strptime(ending_timestring, time_format + " %H:%M:%S %z").timetuple())
        doctor_id = self.available_doctors[list(self.available_doctors.keys())[self.cbo_doctors.current()]]['id']
        unavailable_slots = Database.get_unavailable_timeslots_for_doctor(doctor_id, start_timestamp=start_timestamp,
                                                                          end_timestamp=ending_timestamp)
        return unavailable_slots

    def __build_doctors_list(self):
        # get list of doctors that his patient is allowed to see
        self.available_doctors = Database.get_doctors_available_to_patient(self.root.current_user_id)
        print(self.available_doctors)

        # populate the combobox with the list of doctors
        self.doctors = []
        for d in list(self.available_doctors.values()):
            self.doctors.append(d['name'])

        self.cbo_doctors['values'] = self.doctors
        self.doctor_value.set(self.doctors[0])

    def __build_schedule(self, unavailable_slots):
        # remove old elements if there are any
        for key in list(self.schedules):
            if self.schedules[key].get('btn', False):
                self.schedules[key]['btn'].destroy()
            elif self.schedules[key].get('lbl', False):
                self.schedules[key]['lbl'].destroy()

        unavailable_slots_dict = {}
        # create dictionary for constant time lookup O(1)
        for u in unavailable_slots:
            unavailable_slots_dict[u[0]] = True

        starting_row = 7
        self.schedules = {}

        hours = range(10, 15)
        minutes = range(0, 60, 15)

        datestring = self.month_value.get() + " " + self.txt_day.get().zfill(2) + " " + self.txt_year.get()

        current_row = starting_row
        for hour in hours:
            for minute in minutes:
                this_time = str(hour)+":"+str(minute).zfill(2)
                time_timestamp = round(mktime(datetime.strptime(datestring + " " + this_time + ":00 +0400", "%B %d %Y %H:%M:%S %z").timetuple()))

                self.schedules[this_time] = {}
                self.schedules[this_time]['lbl'] = tk.Label(master=self.p_apmt, text=this_time, font=Style.font_regular)
                self.schedules[this_time]['lbl'].grid(row=current_row, column=1)

                if unavailable_slots_dict.get(time_timestamp, False) is not True:
                    # show button only if time is available
                    self.schedules[this_time]['btn'] = tk.Button(master=self.p_apmt, text="Schedule for: "+this_time, font=Style.font_regular, command=lambda t=this_time: self.__schedule_appointment(t))
                    self.schedules[this_time]['btn'].grid(row=current_row, column=2, sticky="we")
                else:
                    self.schedules[this_time]['lbl'] = tk.Label(master=self.p_apmt, text="Unavailable", font=Style.font_regular, bg="red")
                    self.schedules[this_time]['lbl'].grid(row=current_row, column=2, sticky="we")

                current_row += 1

    def __schedule_appointment(self, schedule_time):
        # create timestamp from time
        datetime_string = self.month_value.get() + " " + self.txt_day.get().zfill(2) + " " + self.txt_year.get() + " " + schedule_time + ":00 +0400"
        timestamp = round(mktime(datetime.strptime(datetime_string, "%B %d %Y %H:%M:%S %z").timetuple()))

        # get doctor id
        doctor_id = self.available_doctors[list(self.available_doctors.keys())[self.cbo_doctors.current()]]['id']
        success = Database.book_appointment(doctor_id, self.root.current_user_id, timestamp)

        if success:
            # rebuild available doctors list
            self.__build_doctors_list()

            # rebuild schedule without the removed timeslot
            self.__build_schedule(self.search_available_bookings())

            # re-render appointments list (not yet implemented)
            self.__show_users_appointments()

    def __show_users_appointments(self):
        appointments = Database.get_users_appointments(self.root.current_user_id, round(datetime.now().timestamp()))
        current_row = 3
        self.afd = {}

        print("drs", self.available_doctors)

        # display appointments on screen
        for appointment in appointments:
            timestamp = appointment[0]
            display_time = strftime("%D %H:%M", localtime(timestamp))

            color = "white" if current_row % 2 is 0 else "orange"

            lbl_display_time = tk.Label(master=self.p_user_apts, text=display_time, bg=color, font=Style.font_key)
            lbl_display_time.grid(row=current_row, column=1, sticky="we")

            lbl_display_dr = tk.Label(master=self.p_user_apts, text="Dr. " + self.available_doctors[appointment[1]]['name'], bg=color, font=Style.font_regular)
            lbl_display_dr.grid(row=current_row, column=2, sticky="we")
            self.user_schedules[timestamp] = {}
            self.user_schedules[timestamp]['time'] = lbl_display_time
            self.user_schedules[timestamp]['dr'] = lbl_display_dr

            current_row += 1

