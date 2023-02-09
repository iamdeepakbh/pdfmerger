import PyPDF2

# Create a PDF writer object
pdf_writer = PyPDF2.PdfFileWriter()

# List of input PDF files
files = ["file1.pdf", "file2.pdf", "file3.pdf"]

# Iterate through the input PDF files
for file in files:
    # Open the PDF file
    pdf_file = open(file, "rb")
    
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Iterate through all the pages in the input PDF file
    for page in range(pdf_reader.numPages):
        # Get a page from the input PDF file
        pdf_page = pdf_reader.getPage(page)
        
        # Add the page to the output PDF file
        pdf_writer.addPage(pdf_page)

# Create the output PDF file
with open("output.pdf", "wb") as f:
    pdf_writer.write(f)
