# Niroshan Sugirtharatnam (0410842)
from App import App

#
#
# class MyLabel(tk.Label):
#     def __init__(self, text, row, column, master=None):
#         super(MyLabel, self).__init__(master)
#         self.pack()
#         self.row = row
#         self.column = column
#         self.text = text
#
#
# class SomeView(tk.Frame):
#     def __init__(self, master=app, message="some message"):
#         super().__init__(master)
#         self.pack()


# start with app with the login screen
app = App()
app.switch_to_login()

# start the event listener at the very end to prevent blocking
app.mainloop()
