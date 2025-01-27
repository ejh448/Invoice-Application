import customtkinter
from tkinter import filedialog
import os
import json
from invoiceGenerator import generate_invoice



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class MyTabView(customtkinter.CTkTabview):
    
    DATA_FILE = "company_data.json"
    CUSTOMER_DATA_FILE = "customer_data.json"
    INVOICE_DATA_FILE = "invoice_data.json"

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

        self.load_company_data()

    def initialize_main_tab(self):
        self.label = customtkinter.CTkLabel(master=self.tab("Main"), text="Invoice")
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # May need to remove later
        self.entry_frame = customtkinter.CTkFrame(self.tab("Main"), fg_color="gray")
        self.entry_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.company_name_label = customtkinter.CTkLabel(master=self.entry_frame, text="Company Label")
        self.company_name_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        self.name_label = customtkinter.CTkLabel(master=self.entry_frame, text="Owner Name")
        self.name_label.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.phone_number_label = customtkinter.CTkLabel(master=self.entry_frame, text="(111)111-1111")
        self.phone_number_label.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        
        self.address_label = customtkinter.CTkLabel(master=self.entry_frame, text="address")
        self.address_label.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        
        self.invoice_number_entry = customtkinter.CTkEntry(master=self.entry_frame, placeholder_text="invoice number")
        self.invoice_number_entry.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")

        self.invoice_date_entry = customtkinter.CTkEntry(master=self.entry_frame, placeholder_text="Invoice Date")
        self.invoice_date_entry.grid(row=1, column=2, padx=20, pady=10, sticky="nsew")

        self.invoice_due_date_entry = customtkinter.CTkEntry(master=self.entry_frame, placeholder_text="Due Date")
        self.invoice_due_date_entry.grid(row=3, column=2, padx=20, pady=10, sticky="nsew")

        self.customer_name_entry = customtkinter.CTkEntry(master=self.entry_frame, placeholder_text="Customer Name")
        self.customer_name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        self.customer_address_entry = customtkinter.CTkEntry(master=self.entry_frame, placeholder_text="Customer Address")
        self.customer_address_entry.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

        self.customer_county_entry = customtkinter.CTkEntry(master=self.entry_frame, placeholder_text="Customer County")
        self.customer_county_entry.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

        self.customer_zipcode_entry = customtkinter.CTkEntry(master=self.entry_frame, placeholder_text="Customer Zipcode")
        self.customer_zipcode_entry.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

        self.customer_state_entry = customtkinter.CTkEntry(master=self.entry_frame, placeholder_text="Customer State")
        self.customer_state_entry.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")



        # Scroll Frame for services
        self.scroll_frame = customtkinter.CTkScrollableFrame(master=self.tab("Main"), width=600, height=300, fg_color="gray", border_color="white")
        self.scroll_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")

        # Column headers
        self.service_label = customtkinter.CTkLabel(master=self.scroll_frame, text="Service", font=("Arial", 14, "bold"))
        self.service_label.grid(row=0, column=0, padx=50, pady=5)

        self.description_label = customtkinter.CTkLabel(master=self.scroll_frame, text="Description", font=("Arial", 14, "bold"))
        self.description_label.grid(row=0, column=1, padx=50, pady=5)

        self.price_label = customtkinter.CTkLabel(master=self.scroll_frame, text="Price", font=("Arial", 14, "bold"))
        self.price_label.grid(row=0, column=2, padx=50, pady=5)

        # Add button
        self.add_row_button = customtkinter.CTkButton(master=self.scroll_frame, text="+", width=100, command=self.add_new_row)
        self.add_row_button.grid(row=0, column=3, padx=50, pady=10, sticky="nsew")

        self.create_invoice_button = customtkinter.CTkButton(master=self.tab("Main"), text="Create Invoice", width=50, command=self.create_invoice)
        self.create_invoice_button.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        # Track current row index for entries
        self.current_row_index = 1

    def add_new_row(self):
        # Create new entries for service, description, and price
        service_entry = customtkinter.CTkEntry(master=self.scroll_frame, placeholder_text="Service")
        service_entry.grid(row=self.current_row_index, column=0, padx=10, pady=5, sticky="nsew")

        description_entry = customtkinter.CTkEntry(master=self.scroll_frame, placeholder_text="Description")
        description_entry.grid(row=self.current_row_index, column=1, padx=10, pady=5, sticky="nsew")

        price_entry = customtkinter.CTkEntry(master=self.scroll_frame, placeholder_text="Price")
        price_entry.grid(row=self.current_row_index, column=2, padx=10, pady=5, sticky="nsew")

        number_label = customtkinter.CTkLabel(master=self.scroll_frame, text=str(self.current_row_index))
        number_label.grid(row=self.current_row_index, column=3, padx=10, pady=5, sticky="nsew")


        # Increment the row index
        if (self.current_row_index < 10):
            self.current_row_index += 1

    def create_invoice(self):
        self.save_customer_data()
        self.save_invoice_data()
        self.save_service_data()
        generate_invoice()
        # This is where customer information will be pulled from the main screen
        # Add the ability to name the file?
        # Figure out how to handle file names
        # also have a popup for file name
        pass

    def save_service_data(self):
        # Collect all row data
        rows = []
        for row in range(1, self.current_row_index):
            service = self.scroll_frame.grid_slaves(row=row, column=0)[0].get()
            description = self.scroll_frame.grid_slaves(row=row, column=1)[0].get()
            price = self.scroll_frame.grid_slaves(row=row, column=2)[0].get()

            # Append to rows if all fields are filled
            if service and description and price:
                rows.append({
                    "service": service,
                    "description": description,
                    "price": price
                })

        # Save to JSON file
        with open("service_data.json", "w") as file:
            json.dump(rows, file, indent=4)

        print("Success", "Service data saved successfully.")


    def save_customer_data(self):
        data = {
            "customer_name": self.customer_name_entry.get(),
            "customer_address": self.customer_address_entry.get(),
            "customer_county": self.customer_county_entry.get(),
            "customer_state": self.customer_state_entry.get(),
            "customer_zipcode": self.customer_zipcode_entry.get()
        }

        if not all(value for key, value in data.items()):
            print("Error", "Customer All fields must be filled out.")
            return

        # Save to JSON file
        with open(self.CUSTOMER_DATA_FILE, "w") as file:
            json.dump(data, file)

        print("Success", "Data saved successfully.")
    
    def save_invoice_data(self):
        data = {
            "invoice_number": self.invoice_number_entry.get(),
            "invoice_date": self.invoice_date_entry.get(),
            "invoice_due_date": self.invoice_due_date_entry.get()
        }

        if not all(value for key, value in data.items()):
            print("Error", "Invoice fields must be filled out.")
            return

        # Save to JSON file
        with open(self.INVOICE_DATA_FILE, "w") as file:
            json.dump(data, file)

        print("Success", "Data saved successfully.")

    def initialize_settings_tab(self):
        self.settings_label = customtkinter.CTkLabel(master=self.tab("Settings"), text="This is the Settings")
        self.settings_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # Add entries
        self.company_name_entry = customtkinter.CTkEntry(self.tab("Settings"), placeholder_text="Company Name")
        self.company_name_entry.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        self.first_name_entry = customtkinter.CTkEntry(self.tab("Settings"), placeholder_text="First Name")
        self.first_name_entry.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        self.last_name_entry = customtkinter.CTkEntry(self.tab("Settings"), placeholder_text="Last Name")
        self.last_name_entry.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        self.phone_number_entry = customtkinter.CTkEntry(self.tab("Settings"), placeholder_text="Phone Number")
        self.phone_number_entry.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

        self.email_entry = customtkinter.CTkEntry(self.tab("Settings"), placeholder_text="Email")
        self.email_entry.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")

        self.website_entry = customtkinter.CTkEntry(self.tab("Settings"), placeholder_text="Website")
        self.website_entry.grid(row=5, column=0, padx=20, pady=10, sticky="nsew")

        self.address_entry = customtkinter.CTkEntry(self.tab("Settings"), placeholder_text="Address")
        self.address_entry.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        self.county_entry = customtkinter.CTkEntry(self.tab("Settings"), placeholder_text="County")
        self.county_entry.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

        self.zipcode_entry = customtkinter.CTkEntry(self.tab("Settings"), placeholder_text="Zipcode")
        self.zipcode_entry.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")
        
        self.state_entry = customtkinter.CTkEntry(self.tab("Settings"), placeholder_text="State")
        self.state_entry.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

        # Image selection widgets
        self.image_label = customtkinter.CTkLabel(master=self.tab("Settings"), text="No Image Selected")
        self.image_label.grid(row=4, column=1, padx=20, pady=10, sticky="nsew")
        self.pick_image_button = customtkinter.CTkButton(master=self.tab("Settings"), text="Select Image", command=self.select_image)
        self.pick_image_button.grid(row=5, column=1, padx=20, pady=10, sticky="nsew")

        # Save button
        self.save_button = customtkinter.CTkButton(master=self.tab("Settings"), text="Save", command=self.save_company_data)
        self.save_button.grid(row=6, column=1, padx=20, pady=10, sticky="nsew")

    def initialize_folder_tab(self):
        pass  # This tab is empty currently

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
            "email": self.email_entry.get(),
            "website": self.website_entry.get(),
            "address": self.address_entry.get(),
            "county": self.county_entry.get(),
            "zipcode": self.zipcode_entry.get(),
            "state": self.state_entry.get(),
            "image_path": self.image_path or "",
        }

        # Ensure all required fields are filled
        if not all(value for key, value in data.items() if key != "image_path"):
            print("Error", "Company fields except the image must be filled out.")
            return

        # Save to JSON file
        with open(self.DATA_FILE, "w") as file:
            json.dump(data, file)

        print("Success", "Data saved successfully.")
    

    def load_company_data(self):
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)

            # main tab populating entries
            self.company_name_entry.insert(0, data.get("company_name", ""))
            self.first_name_entry.insert(0, data.get("first_name", ""))
            self.last_name_entry.insert(0, data.get("last_name", ""))
            self.phone_number_entry.insert(0, data.get("phone_number", ""))
            self.address_entry.insert(0, data.get("address", ""))
            self.image_path = data.get("image_path", None)
            self.email_entry.insert(0, data.get("email",""))
            self.website_entry.insert(0, data.get("website",""))


            # maintab
            self.company_name_label.configure(text=data.get("company_name", "Company Label"))
            self.name_label.configure(text = f"{data.get('first_name', 'First')} {data.get('last_name', 'Last')}")
            self.phone_number_label.configure(text=data.get("phone_number", "(111)111-1111"))
            self.address_label.configure(text= f"{data.get('address', 'Address')} {data.get('county', 'County')} {data.get('state', 'State')}, {data.get('zipcode', 'Zipcode')} ")

            if self.image_path:
                self.image_label.configure(text=f"Image Selected: {os.path.basename(self.image_path)}")


# The main application frame
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.title("Invoice Application")

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")


app = App()
app.mainloop()
