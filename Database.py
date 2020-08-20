# Niroshan Sugirtharatnam (0410842)
import sqlite3
from sqlite3 import Error
from pprint import pprint

# singleton class with only static methods. internally, create a connection
# early and then use it all requests.
class Database:
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
