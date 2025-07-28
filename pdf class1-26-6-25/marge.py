from PyPDF2 import PdfMerger


merger = PdfMerger()


pdf_files = ['pdfs/class1.pdf', 'pdfs/8-5-2025.pdf']


for pdf in pdf_files:
    merger.append(pdf)


merger.write("python.pdf")
merger.close()

print("PDFs merged successfully into 'python.pdf'")
