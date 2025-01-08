import customtkinter
from tkinter import filedialog
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

        # Initialize widgets
        self.initialize_main_tab()
        self.initialize_settings_tab()
        self.initialize_folder_tab()

        # Load saved data
        self.load_company_data()

    def initialize_main_tab(self):
        self.label = customtkinter.CTkLabel(master=self.tab("Main"), text="This is tab 1")
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

    def initialize_settings_tab(self):
        self.settings_label = customtkinter.CTkLabel(master=self.tab("Settings"), text="This is the Settings")
        self.settings_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # Add entries
        self.company_name_entry = self.create_entry(self.tab("Settings"), "Company Name", 1)
        self.first_name_entry = self.create_entry(self.tab("Settings"), "First Name", 2)
        self.last_name_entry = self.create_entry(self.tab("Settings"), "Last Name", 3)
        self.phone_number_entry = self.create_entry(self.tab("Settings"), "Phone Number", 4)
        self.address_entry = self.create_entry(self.tab("Settings"), "Address", 5)
        self.zipcode_entry = self.create_entry(self.tab("Settings"), "Zipcode", 6)
        self.state_entry = self.create_entry(self.tab("Settings"), "State", 7)

        # Image selection widgets
        self.image_label = customtkinter.CTkLabel(master=self.tab("Settings"), text="No Image Selected")
        self.image_label.grid(row=8, column=0, padx=20, pady=10, sticky="nsew")
        self.pick_image_button = customtkinter.CTkButton(master=self.tab("Settings"), text="Select Image", command=self.select_image)
        self.pick_image_button.grid(row=9, column=0, padx=20, pady=10, sticky="nsew")

        # Save button
        self.save_button = customtkinter.CTkButton(master=self.tab("Settings"), text="Save", command=self.save_company_data)
        self.save_button.grid(row=10, column=0, padx=20, pady=10, sticky="nsew")

    def initialize_folder_tab(self):
        pass  # This tab can be populated later as needed

    def create_entry(self, parent, placeholder, row):
        entry = customtkinter.CTkEntry(master=parent, placeholder_text=placeholder)
        entry.grid(row=row, column=0, padx=20, pady=10, sticky="nsew")
        return entry

    def select_image(self):
        # Open file dialog to select image
        filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp"), ("All files", "*.*")]
        filepath = filedialog.askopenfilename(title="Select Image", filetypes=filetypes)

        if filepath:
            self.image_path = filepath
            self.image_label.configure(text=os.path.basename(filepath))

    def save_company_data(self):
        data = {
            "company_name": self.company_name_entry.get(),
            "first_name": self.first_name_entry.get(),
            "last_name": self.last_name_entry.get(),
            "phone_number": self.phone_number_entry.get(),
            "address": self.address_entry.get(),
            "zipcode": self.zipcode_entry.get(),
            "state": self.state_entry.get(),
            "image_path": self.image_path,
        }

        # Ensure all required fields are filled
        if not all(value for key, value in data.items() if key != "image_path"):
            print("Error", "All fields except the image must be filled out.")
            return

        # Save to JSON file
        with open(self.DATA_FILE, "w") as file:
            json.dump(data, file)

        print("Success", "Data saved successfully.")

    def load_company_data(self):
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)

            self.company_name_entry.insert(0, data.get("company_name", ""))
            self.first_name_entry.insert(0, data.get("first_name", ""))
            self.last_name_entry.insert(0, data.get("last_name", ""))
            self.phone_number_entry.insert(0, data.get("phone_number", ""))
            self.address_entry.insert(0, data.get("address", ""))
            self.zipcode_entry.insert(0, data.get("zipcode", ""))
            self.state_entry.insert(0, data.get("state", ""))
            self.image_path = data.get("image_path", None)

            if self.image_path:
                self.image_label.configure(text=f"Image Selected: {os.path.basename(self.image_path)}")


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
