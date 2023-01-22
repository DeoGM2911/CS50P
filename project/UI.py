import customtkinter as ctk


class UI:
    def __init__(self, master: ctk.CTk):
        self.master = master
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.master.geometry("500x500")
        self.master.resizable(False, False)
        self.master.wm_title("Vehicle")
        
        # Create the label for prompting
        self.label0 = ctk.CTkLabel(self.master, text=f"Welcome to Deo's app!", font=("Helvetica bold", 24))
        self.label0.place(relx=0.5, rely=0.25, anchor="center")
        self.label0_1 = ctk.CTkLabel(self.master, font=("Helvetica bold", 15),
                                    text=f"This is an app for checking and generating license plate for vehicles!")
        self.label0_1.place(relx=0.5, rely=0.35, anchor="center")
        
        # Notes
        self.label1 = ctk.CTkLabel(self.master, font=("Helvetica bold", 12.5), 
                                text="* in indicates that the field is required!")
        self.label1.place(relx=0.24, rely=0.95, anchor="center")
        
        # Prompting for name
        self.entry1 = ctk.CTkEntry(self.master, placeholder_text="Your name here", 
                                text_color="white", width=150, height=20)
        self.entry1.place(relx=0.58, rely=0.45, anchor="center")
        self.label1_1 = ctk.CTkLabel(self.master, font=("Helvetica italic", 12.5), text="*Name:")
        self.label1_1.place(relx=0.36, rely=0.45, anchor="center")
        
        # Prompting for email
        self.entry5 = ctk.CTkEntry(self.master, placeholder_text="Your email", 
                            text_color="white", width=150, height=20)
        self.entry5.place(relx=0.58, rely=0.55, anchor="center")
        self.label5_1 = ctk.CTkLabel(self.master, font=("Helvetica italic", 15), text="Email:")
        self.label5_1.place(relx=0.36, rely=0.55, anchor="center")
        
        # Prompting for date of birth
        self.label234_1 = ctk.CTkLabel(self.master, font=("Helvetica italic", 15), text="*Date of birth:")
        self.label234_1.place(relx=0.31, rely=0.65, anchor="center")
        self.entry2 = ctk.CTkEntry(self.master, placeholder_text="Day", 
                                text_color="white", width=50, height=20)
        self.entry2.place(relx=0.475, rely=0.65, anchor="center")
        
        self.entry3 = ctk.CTkEntry(self.master, placeholder_text="Month", 
                                text_color="white", width=50, height=20)
        self.entry3.place(relx=0.59, rely=0.65, anchor="center")
        
        self.entry4 = ctk.CTkEntry(self.master, placeholder_text="Year", 
                                text_color="white", width=75, height=20)
        self.entry4.place(relx=0.73, rely=0.65, anchor="center")

        # Next button
        self.button0 = ctk.CTkButton(self.master, width=100, height=30, text="Next",
                                    bg_color="blue", font=("Heltevica", 15))
        self.button0.place(relx=0.5, rely=0.72, anchor="center")
        
        
app = ctk.CTk()
gui = UI(master=app)
app.mainloop()