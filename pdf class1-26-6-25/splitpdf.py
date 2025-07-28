from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

# Extract page 2 to 5 (index starts from 0)
for i in range(1, 5):  # Page 2 to 5 = index 1 to 4
    writer.add_page(reader.pages[i])

with open("extracted_pages.pdf", "wb") as output_pdf:
    writer.write(output_pdf)

print("Pages 2 to 5 extracted successfully.")
