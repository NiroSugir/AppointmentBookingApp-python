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
            Database.conn = sqlite3.connect(Database.db)
        except Error as e:
            print("Failed to connect to db", e, sep="\n")
            exit()

    @staticmethod
    def verify_login_credentials(username, password):
        try:
            cur = Database.conn.cursor()

            # TODO: bind parameters if you have time
            query = "SELECT user_id FROM Users where username='"+username+"' AND password='"+password+"';"
            cur.execute(query)
            rows = cur.fetchall()

            # correct credentials means username and password returned a row
            return rows[0] if len(rows) == 1 else False

        except Error as e:
            print("Failed to load users from db!", e, sep="\n")
            exit()

    @staticmethod
    def register_user(first_name, last_name, age, gender, address, city, username, password):
        try:
            cur = Database.conn.cursor()

            # TODO: bind parameters if you have time
            # TODO: hash password if you have time (don't forget to compare hashed pword in login method)
            query = "INSERT INTO Users (first_name, last_name, age, gender, address, city, username, password) VALUES ('"+first_name+"','"+last_name+"','"+str(age)+"','"+gender+"','"+address+"','"+city+"','"+username+"','"+password+"');"
            cur.execute(query)

            return True

        except IntegrityError as e:
            Database.__show_db_error("Username is already taken, please choose another!")
            return False
        except Error as e:
            print("Failed to load users from db!", e, sep="\n")
            exit()
