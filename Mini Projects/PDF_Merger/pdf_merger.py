from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["1.pdf", "2.pdf"]:
    merger.append(pdf)
merger.close() 
merger.write("merged-pdf.pdf")