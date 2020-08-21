# Niroshan Sugirtharatnam (0410842)
from App import App
from helpers.Database import Database

# DB Singleton class used for all CRUD operations
Database.connect("db.sqlite3")

# start with app with the login screen
app = App()
app.switch_to_login()

# start the event listener at the very end to prevent blocking
app.mainloop()
