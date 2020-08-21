# Niroshan Sugirtharatnam (0410842)
import sqlite3
from sqlite3 import Error, IntegrityError
from tkinter import messagebox


# singleton class with only static methods. internally, create a connection
# early and then use it all requests.
class Database:
    @staticmethod
    def __show_db_error(msg):
        messagebox.showerror(title="Database Error", message=msg)

    @staticmethod
    def connect(db):
        Database.db = db

        try:
            Database.conn = sqlite3.connect(Database.db, isolation_level=None)
        except Error as e:
            print("Failed to connect to db", e, sep="\n")
            exit()

    @staticmethod
    def verify_login_credentials(username, password):
        try:
            cur = Database.conn.cursor()

            query = "SELECT user_id FROM Users where username='"+username+"' AND password='"+password+"';"
            cur.execute(query)
            rows = cur.fetchall()

            # correct credentials means username and password returned a row
            return rows[0][0] if len(rows) == 1 else False

        except Error as e:
            print("Failed to load users from db!", e, sep="\n")
            exit()

    @staticmethod
    def register_user(first_name, last_name, age, gender, address, city, username, password):
        try:
            cur = Database.conn.cursor()

            # TODO: hash password if you have time (don't forget to compare hashed pword in login method)
            query = "INSERT INTO Users (first_name, last_name, age, gender, address, city, username, password) VALUES ('"+first_name+"','"+last_name+"','"+str(age)+"','"+gender+"','"+address+"','"+city+"','"+username+"','"+password+"');"
            cur.execute(query)

            return cur.lastrowid

        except IntegrityError as e:
            # Uniqueness username. username field is set to unique so we can avoid any race conditions
            if str(e).find("UNIQUE") != -1:
                # username already taken
                Database.__show_db_error("Username is already taken. Please choose another.")
            else:
                # maybe db locked up. for purpose of the project, show the error message so it
                # can be debugged and fixed
                Database.__show_db_error(e)

            return False
        except Error as e:
            print("Failed to register user db!", e, sep="\n")
            exit()

    @staticmethod
    def get_userdata(user_id):
        try:
            cur = Database.conn.cursor()
            print('user id', user_id)

            query = "SELECT username, first_name, last_name, age, city, gender, address FROM Users WHERE user_id="+str(user_id)+";"
            cur.execute(query)
            rows = cur.fetchall()

            if len(rows) != 1:
                Database.__show_db_error("Problem loading user from database. Please make sure the file is not corrupt.")
                exit();

            return {
                "username": rows[0][0],
                "first_name": rows[0][1],
                "last_name": rows[0][2],
                "age": int(rows[0][3]),
                "city": rows[0][4],
                "gender": rows[0][5],
                "address": rows[0][6],
            }

        except Error as e:
            print("Failed to load userdata from db!", e, sep="\n")
            exit()

    @staticmethod
    def get_doctors_available_to_patient(user_id):
        try:
            cur = Database.conn.cursor()

            # get the next appointment for this user. since they can only schedule with one doctor
            # the first one on the list (if any) will determine which doctor(s) this patient is
            # allowed to see
            query = "SELECT doctor_id FROM Appointments where user_id="+str(user_id)+" LIMIT 1;"
            cur.execute(query)
            rows = cur.fetchall()

            # by default may see any doctor
            clause = "" if len(rows) == 0 else " WHERE doctor_id="+str(rows[0][0])

            query = "SELECT doctor_id, name FROM Doctors"+clause+";"
            cur.execute(query)
            rows = cur.fetchall()

            doctors = {}

            for row in rows:
                doctors[row[0]] = {
                    "id": row[0],
                    "name": row[1]
                }

            return doctors

        except Error as e:
            print("Failed to load doctors from db!", e, sep="\n")
            exit()

    @staticmethod
    def get_unavailable_timeslots_for_doctor(doctor_id, start_timestamp, end_timestamp):
        try:
            cur = Database.conn.cursor()

            query = "SELECT appointment_time, user_id from Appointments WHERE doctor_id=" + str(doctor_id) + " AND appointment_time BETWEEN " + str(start_timestamp) + " AND " + str(end_timestamp) + ";"
            cur.execute(query)

            rows = cur.fetchall()

            return rows

        except Error as e:
            print("Failed to load timeslots from db!", e, sep="\n")
            exit()

    @staticmethod
    def book_appointment(doctor_id, user_id, timestamp):
        try:
            cur = Database.conn.cursor()

            # using composite primary key (doctor id + appointment time) to restrict dr from being booked
            # twice @ the same time
            query = "INSERT INTO Appointments (appointment_time, doctor_id, user_id) VALUES ("+str(timestamp)+","+str(doctor_id)+","+str(user_id)+");"
            cur.execute(query)

            return True

        except Error as e:
            if str(e).find("UNIQUE") is not False:
                Database.__show_db_error("Failed to book appointment, that timeslot is already taken!")
            else:
                Database.__show_db_error("Failed to book appointment!")
                print("Failed to book appointment!", e, sep="\n")

            return False

    @staticmethod
    def get_users_appointments(user_id, starting_timestamp):
        try:
            cur = Database.conn.cursor()

            query = "SELECT appointment_time, doctor_id from Appointments WHERE user_id=" + str(user_id) + " AND appointment_time >= " + str(starting_timestamp) + ";"
            cur.execute(query)
            rows = cur.fetchall()

            print(rows)

            return rows

        except Error as e:
            print("Failed to book appointment!", e, sep="\n")
            exit()
