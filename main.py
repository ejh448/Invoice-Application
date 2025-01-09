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

        self.image_path = None

        # Initialize widgets
        self.initialize_main_tab()
        self.initialize_settings_tab()
        self.initialize_folder_tab()

        # Load saved data
        self.load_company_data()

    def initialize_main_tab(self):
        self.label = customtkinter.CTkLabel(master=self.tab("Main"), text="Invoice")
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # May need to remove later
        #self.tab("Main").grid_columnconfigure(0, weight=1)

        self.company_name_label = customtkinter.CTkLabel(master=self.tab("Main"), text="Company Label")
        self.company_name_label.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.first_name_label = customtkinter.CTkLabel(master=self.tab("Main"), text="First")
        self.first_name_label.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        self.last_name_label = customtkinter.CTkLabel(master=self.tab("Main"), text="last")
        self.last_name_label.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

        self.phone_number_label = customtkinter.CTkLabel(master=self.tab("Main"), text="(111)111-1111")
        self.phone_number_label.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        
        self.address_label = customtkinter.CTkLabel(master=self.tab("Main"), text="address")
        self.address_label.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")

        self.county_label = customtkinter.CTkLabel(master=self.tab("Main"), text="county")
        self.county_label.grid(row=4, column=1, padx=20, pady=10, sticky="nsew")

        self.zipcode_label = customtkinter.CTkLabel(master=self.tab("Main"), text="zipcode")
        self.zipcode_label.grid(row=4, column=2, padx=20, pady=10, sticky="nsew")

        self.state_label = customtkinter.CTkLabel(master=self.tab("Main"), text="State")
        self.state_label.grid(row=4, column=3, padx=20, pady=10, sticky="nsew")

        self.invoice_number_label = customtkinter.CTkLabel(master=self.tab("Main"), text="Invoice number")
        self.invoice_number_label.grid(row=3, column=4, padx=20, pady=10, sticky="nsew")

        self.invoice_date_label = customtkinter.CTkLabel(master=self.tab("Main"), text="Invoice Date")
        self.invoice_date_label.grid(row=4, column=4, padx=20, pady=10, sticky="nsew")
        
        self.invoice_number_entry = customtkinter.CTkEntry(master=self.tab("Main"), placeholder_text="invoice number")
        self.invoice_number_entry.grid(row=3, column=5, padx=20, pady=10, sticky="nsew")

        self.invoice_date_entry = customtkinter.CTkEntry(master=self.tab("Main"), placeholder_text="Date")
        self.invoice_date_entry.grid(row=4, column=5, padx=20, pady=10, sticky="nsew")

        self.invoice_due_date_entry = customtkinter.CTkEntry(master=self.tab("Main"), placeholder_text="Due Date")
        self.invoice_due_date_entry.grid(row=5, column=5, padx=20, pady=10, sticky="nsew")

        self.invoice_due_date_label = customtkinter.CTkLabel(master=self.tab("Main"), text="Due Date")
        self.invoice_due_date_label.grid(row=5, column=4, padx=20, pady=10, sticky="nsew")



        self.customer_name_entry = customtkinter.CTkEntry(master=self.tab("Main"), placeholder_text="Customer Name")
        self.customer_name_entry.grid(row=5, column=0, padx=20, pady=10, sticky="nsew")

        self.customer_address_entry = customtkinter.CTkEntry(master=self.tab("Main"), placeholder_text="Customer Address")
        self.customer_address_entry.grid(row=6, column=0, padx=20, pady=10, sticky="nsew")

        self.customer_zipcode_entry = customtkinter.CTkEntry(master=self.tab("Main"), placeholder_text="Customer Zipcode")
        self.customer_zipcode_entry.grid(row=6, column=1, padx=20, pady=10, sticky="nsew")

        self.customer_state_entry = customtkinter.CTkEntry(master=self.tab("Main"), placeholder_text="Customer State")
        self.customer_state_entry.grid(row=6, column=2, padx=20, pady=10, sticky="nsew")



        # Scroll Frame for services
        self.scroll_frame = customtkinter.CTkScrollableFrame(master=self.tab("Main"), width=600, height=300)
        self.scroll_frame.grid(row=7, column=1, columnspan=3, padx=20, pady=10, sticky="nsew")

        # Column headers
        self.service_label = customtkinter.CTkLabel(master=self.scroll_frame, text="Service", font=("Arial", 14, "bold"))
        self.service_label.grid(row=0, column=0, padx=10, pady=5)

        self.description_label = customtkinter.CTkLabel(master=self.scroll_frame, text="Description", font=("Arial", 14, "bold"))
        self.description_label.grid(row=0, column=1, padx=10, pady=5)

        self.price_label = customtkinter.CTkLabel(master=self.scroll_frame, text="Price", font=("Arial", 14, "bold"))
        self.price_label.grid(row=0, column=2, padx=10, pady=5)

        # Add button
        self.add_row_button = customtkinter.CTkButton(master=self.scroll_frame, text="+", width=50, command=self.add_new_row)
        self.add_row_button.grid(row=0, column=3, padx=20, pady=10, sticky="nsew")

        self.create_invoice_button = customtkinter.CTkButton(master=self.tab("Main"), text="Create Invoice", width=50, command="")
        self.create_invoice_button.grid(row=6, column=4, padx=20, pady=10, sticky="nsew")


        # Track current row index for entries
        self.current_row_index = 1

    def add_new_row(self):
        """Add a new row of entry widgets under the column headers."""
        service_entry = customtkinter.CTkEntry(master=self.scroll_frame, placeholder_text="Service")
        service_entry.grid(row=self.current_row_index, column=0, padx=10, pady=5, sticky="nsew")

        description_entry = customtkinter.CTkEntry(master=self.scroll_frame, placeholder_text="Description")
        description_entry.grid(row=self.current_row_index, column=1, padx=10, pady=5, sticky="nsew")

        price_entry = customtkinter.CTkEntry(master=self.scroll_frame, placeholder_text="Price")
        price_entry.grid(row=self.current_row_index, column=2, padx=10, pady=5, sticky="nsew")

        # Increment the row index
        self.current_row_index += 1



    def initialize_settings_tab(self):
        self.settings_label = customtkinter.CTkLabel(master=self.tab("Settings"), text="This is the Settings")
        self.settings_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # Add entries
        self.company_name_entry = self.create_entry(self.tab("Settings"), "Company Name", 1)
        self.first_name_entry = self.create_entry(self.tab("Settings"), "First Name", 2)
        self.last_name_entry = self.create_entry(self.tab("Settings"), "Last Name", 3)
        self.phone_number_entry = self.create_entry(self.tab("Settings"), "Phone Number", 4)
        self.address_entry = self.create_entry(self.tab("Settings"), "Address", 5)
        self.county_entry = self.create_entry(self.tab("Settings"), "County", 6)
        self.zipcode_entry = self.create_entry(self.tab("Settings"), "Zipcode", 7)
        self.state_entry = self.create_entry(self.tab("Settings"), "State", 8)

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
            "county": self.county_entry.get(),
            "zipcode": self.zipcode_entry.get(),
            "state": self.state_entry.get(),
            "image_path": self.image_path or "",
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
            self.county_entry.insert(0, data.get("county", ""))
            self.zipcode_entry.insert(0, data.get("zipcode", ""))
            self.state_entry.insert(0, data.get("state", ""))
            self.image_path = data.get("image_path", None)


            #maintab
            # Populate Settings tab entries
            self.company_name_label.configure(text=data.get("company_name", "Company Label"))
            self.first_name_label.configure(text=data.get("first_name", "First"))
            self.last_name_label.configure(text=data.get("last_name", "Last"))
            self.phone_number_label.configure(text=data.get("phone_number", "(111)111-1111"))
            self.address_label.configure(text=data.get("address", "Address"))
            self.zipcode_label.configure(text=data.get("zipcode", "Zipcode"))
            self.state_label.configure(text=data.get("state", "State"))
                


            if self.image_path:
                self.image_label.configure(text=f"Image Selected: {os.path.basename(self.image_path)}")


# The main application frame
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")

        # Configure grid to allow expansion
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add TabView
        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")  # Expands to fill parent


app = App()
app.mainloop()
