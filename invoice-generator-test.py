from reportlab.pdfgen import canvas
import os

# Step 1: Define the folder to save PDFs
pdf_folder = "Invoices"  # Replace with your desired folder name
os.makedirs(pdf_folder, exist_ok=True)  # Create the folder if it doesn't exist

# Step 2: Define the PDF file name and full path
pdf_file_name = "example.pdf"
pdf_path = os.path.join(pdf_folder, pdf_file_name)


# Step 3: Create the PDF
c = canvas.Canvas(pdf_path, pagesize=(595.27, 841.89))
c.drawString(50, 800, "INVOICE")
c.drawString(50, 775, "Integrity Roofing LLC.")
c.drawString(50, 750, "135 Victoria Circle")
c.drawString(50, 725, "North Wilkesboro, NC 28659")
c.drawString(250, 775, "jodyclonch@gmail.com")
c.drawString(250, 750, "336-902-8899")
c.drawString(250, 725, "integrityroofing.com")
c.line(50, 710, 500, 710)

c.save()

print(f"PDF saved successfully at: {pdf_path}")
