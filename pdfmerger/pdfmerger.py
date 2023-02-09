import PyPDF2

# Create a PDF writer object
pdf_writer = PyPDF2.PdfWriter()

# List of input PDF files
files = ["file1.pdf", "file2.pdf"]

# Iterate through the input PDF files
for file in files:
    # Open the PDF file
    pdf_file = open(file, "rb")

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Iterate through all the pages in the input PDF file
    for page in range(len(pdf_reader.pages)):
        # Get a page from the input PDF file
        pdf_page = pdf_reader.pages[page]

        # Add the page to the output PDF file
        pdf_writer.add_page(pdf_page)

# Create the output PDF file
with open("output.pdf", "wb") as f:
    pdf_writer.write(f)