import customtkinter
import os
import json

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class MyTabView(customtkinter.CTkTabview):
    DATA_FILE = "company_data.json"

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Creating Tabs
        self.add("Main")
        self.add("Settings")
        self.add("Folder")

        # Adding Widgets onto tabs
        self.label = customtkinter.CTkLabel(master=self.tab("Main"), text="This is tab 1")
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        self.settings_label = customtkinter.CTkLabel(master=self.tab("Settings"), text="This is the Settings")
        self.settings_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        self.company_name_entry = customtkinter.CTkEntry(master=self.tab("Settings"), placeholder_text="Company Name")
        self.company_name_entry.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.first_name_entry = customtkinter.CTkEntry(master=self.tab("Settings"), placeholder_text="First Name")
        self.first_name_entry.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        self.last_name_entry = customtkinter.CTkEntry(master=self.tab("Settings"), placeholder_text="Last Name")
        self.last_name_entry.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

        self.phone_number_entry = customtkinter.CTkEntry(master=self.tab("Settings"), placeholder_text="Phone Number")
        self.phone_number_entry.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")

        self.address_entry = customtkinter.CTkEntry(master=self.tab("Settings"), placeholder_text="Address")
        self.address_entry.grid(row=5, column=0, padx=20, pady=10, sticky="nsew")

        self.zipcode_entry = customtkinter.CTkEntry(master=self.tab("Settings"), placeholder_text="Zipcode")
        self.zipcode_entry.grid(row=6, column=0, padx=20, pady=10, sticky="nsew")

        self.state_entry = customtkinter.CTkEntry(master=self.tab("Settings"), placeholder_text="State")
        self.state_entry.grid(row=7, column=0, padx=20, pady=10, sticky="nsew")

        self.image_label = customtkinter.CTkLabel(master=self.tab("Settings"), text="No Image Currently...")
        self.image_label.grid(row=8, column=0, padx=20, pady=10, sticky="nsew")

        self.pick_image_button = customtkinter.CTkButton(master=self.tab("Settings"), text="Select Image")
        self.pick_image_button.grid(row=9, column=0, padx=20, pady=10, sticky="nsew")

        self.save_button = customtkinter.CTkButton(master=self.tab("Settings"), text="Save", command=self.save_company_data)
        self.save_button.grid(row=10, column=0, padx=20, pady=10, sticky="nsew")

        self.load_company_data()

    def save_company_data(self):
        # Get data from entries
        data = {
            "company_name": self.company_name_entry.get(),
            "first_name": self.first_name_entry.get(),
            "last_name": self.last_name_entry.get(),
            "phone_number": self.phone_number_entry.get(),
            "address": self.address_entry.get(),
            "zipcode": self.zipcode_entry.get(),
            "state": self.state_entry.get(),
        }

        # Ensure all fields are filled
        if not all(data.values()):
            print("Error", "All fields must be filled out.")
            return

        # Save to JSON file
        with open(self.DATA_FILE, "w") as file:
            json.dump(data, file)

        print("Success", "Data saved successfully.")

    def load_company_data(self):
        # Check if file exists
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)

            # insert data into entries
            self.company_name_entry.insert(0, data.get("company_name", ""))
            self.first_name_entry.insert(0, data.get("first_name", ""))
            self.last_name_entry.insert(0, data.get("last_name", ""))
            self.phone_number_entry.insert(0, data.get("phone_number", ""))
            self.address_entry.insert(0, data.get("address", ""))
            self.zipcode_entry.insert(0, data.get("zipcode", ""))
            self.state_entry.insert(0, data.get("state", ""))


# The main application frame
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("750x750")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")


app = App()
app.mainloop()
