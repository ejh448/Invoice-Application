import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Creating Tabs
        self.add("Main")
        self.add("Settings")
        self.add("Folder")

        # Adding Widgets onto tabs
        self.label = customtkinter.CTkLabel(master=self.tab("Main"), text="This is tab 1")
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")


# The main application frame
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("750x750")

        # Configure grid to allow expansion
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add TabView
        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")  # Expands to fill parent


app = App()
app.mainloop()
