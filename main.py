# Niroshan Sugirtharatnam (0410842)
from App import App
from Database import Database

Database.connect("db.sqlite3")

# start with app with the login screen
app = App()
app.switch_to_registration()

# start the event listener at the very end to prevent blocking
app.mainloop()
