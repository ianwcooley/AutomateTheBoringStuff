#! python3
# combinePdfs.py - Combines all the PDFs in the provided directory into
# a single PDF.
# Usage:
#   ./combinePdfs.py <directory>

import PyPDF2, os, sys

directory = sys.argv[1]

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(os.path.join(directory, filename), 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    # Loop through all the pages and add them.
    for pageObj in pdfReader.pages:
        pdfWriter.add_page(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open(os.path.join(directory, 'combined.pdf'), 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
