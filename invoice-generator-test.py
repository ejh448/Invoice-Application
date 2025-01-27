from reportlab.pdfgen import canvas
import os
import json

# Load JSON data
with open("company_data.json", "r") as file:
    data = json.load(file)

# Extract data
company_name = data["company_name"]
first_name = data["first_name"]
email = data["email"]
last_name = data["last_name"]
phone_number = data["phone_number"]
website = data["website"]
address = data["address"]
county = data["county"]
zipcode = data["zipcode"]
state = data["state"]
image_path = data["image_path"]


with open("customer_data.json", "r") as file:
    data = json.load(file)

customer_name = data["customer_name"]
customer_address = data["customer_address"]
customer_county = data["customer_county"]
customer_state = data["customer_state"]
customer_zipcode = data["customer_zipcode"]

with open("invoice_data.json", "r") as file:
    data = json.load(file)

invoice_number = data["invoice_number"]
invoice_date = data["invoice_date"]
invoice_due_date = data["invoice_due_date"]

# Create PDF folder and file
pdf_folder = "Invoices"
os.makedirs(pdf_folder, exist_ok=True) 
pdf_file_name = "example.pdf"
pdf_path = os.path.join(pdf_folder, pdf_file_name)




# Create canvas ######################################################
c = canvas.Canvas(pdf_path, pagesize=(595.27, 841.89))
page_width, page_height = c._pagesize

# Set starting position
margin = 50
current_y = page_height - margin

# Title
c.setFont("Helvetica-Bold", 20)
c.setFillColor("Blue")
c.drawString(margin, current_y, "INVOICE")
# Draw the company logo/image
if os.path.exists(image_path):
    image_width = 150  # Set the desired width
    image_height = 100  # Set the desired height
    c.drawImage(image_path, page_width - image_width - margin, current_y + 10 - image_height, 
                width=image_width, height=image_height)
else:
    print(f"Image not found at {image_path}")

current_y -= 30

c.setFont("Helvetica", 12)
c.setFillColor("Black")

# Company Info
c.drawString(margin, current_y, company_name)
current_y -= 15
c.drawString(margin, current_y, address)
current_y -= 15
c.drawString(margin, current_y, f"{county}, {state} {zipcode}")
current_y -= 15

# Contact Info
c.drawString(margin , current_y, phone_number)
current_y -= 15
c.drawString(margin , current_y, email)
current_y -= 15

# Horizontal line
c.line(margin, current_y, page_width - margin, current_y)
current_y -= 30 

#customer information
c.setFont("Helvetica-Bold", 15)
c.setFillColor("Blue")
c.drawString(margin, current_y, "Bill To")
c.setFillColor("Black")
c.setFont("Helvetica", 12)
current_y -= 15
c.drawString(margin, current_y, customer_name)
c.drawString(page_width - 200, current_y, f"Invoice No. {invoice_number}")
current_y -= 15
c.drawString(margin, current_y, customer_address)
c.drawString(page_width - 200, current_y, f"Invoice Date: {invoice_date}")
current_y -= 15
c.drawString(margin, current_y, f"{customer_county} {customer_state}, {customer_zipcode}")
current_y -= 20 


c.line(margin, current_y, page_width - margin, current_y)
current_y -= 20

# Items Table
c.setFont("Helvetica-Bold", 12)
c.setFillColor("Blue")
c.drawString(margin, current_y, "Description")
c.drawString(margin + 200, current_y, "Item")
c.drawString(page_width - 150, current_y, "Price")
c.setFillColor("Black")
c.setFont("Helvetica", 12)
current_y -= 20  # Line spacing for items

# Draw items dynamically
items = [
    {"Description": "Item 1", "Item": "bolts", "Price": "$100.00"},
    {"Description": "Item 1", "Item": "lumber", "Price": "$100.00"},
    {"Description": "Item 1", "Item": "shingles", "Price": "$100.00"},
    {"Description": "Item 1", "Item": "etc..", "Price": "$100.00"}
]

for item in items:
    c.drawString(margin, current_y, item["Description"])
    c.drawString(margin + 200, current_y, item["Item"])
    c.drawString(page_width - 150, current_y, item["Price"])
    current_y -= 20  # Spacing between items

# Draw total and other info
c.line(margin, current_y, page_width - margin, current_y)
current_y -= 20
c.setFont("Helvetica-Bold", 12)
c.drawString(page_width - 150, current_y, "Total: $250.00")
c.setFillColor("Red")
c.drawString(margin, current_y, f"Due Date: {invoice_due_date}")

# Save PDF
c.save()

print(f"PDF saved successfully at: {pdf_path}")
