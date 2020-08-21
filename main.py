# Niroshan Sugirtharatnam (0410842)
from App import App
from helpers.Database import Database

Database.connect("db.sqlite3")

# start with app with the login screen
app = App()
# app.switch_to_login()

# INFO: for development only
app.current_user_id=1
app.switch_to_appointments()

# start the event listener at the very end to prevent blocking
app.mainloop()
