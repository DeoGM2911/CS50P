import customtkinter as ctk


class UI:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry("750x500")


app = ctk.CTk()
gui = UI(master=app)
app.mainloop()