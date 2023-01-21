import customtkinter as ctk


class UI:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry("750x500")
        self.master.resizable(False, False)
        self.master.wm_title("Vehicle")
        self.master.tk_setPalette("black")
        
        # Create the label for prompting
        self.label = ctk.CTkLabel(self.master, text="Name", font=("Helvetica bold", 26))
        self.label.place(relx=0.5, rely=0.25, anchor="center")
        self.label = ctk.CTkLabel(self.master, text="Date of birth", font=("Helvetica bold", 26))
        self.label.place(relx=0.5, rely=0.55, anchor="center")

app = ctk.CTk()
gui = UI(master=app)
app.mainloop()