# Import the necessary libraries
import PyPDF2
import os

# Set the source and destination folders
source_folder = '/Users/orkravitz/Downloads/ProtectMyPDF/split_source'
destination_folder = '/Users/orkravitz/Downloads/ProtectMyPDF/split_dest'

# Iterate through the files in the source folder
for filename in os.listdir(source_folder):
    # Check if the file is a PDF
    if filename.endswith('.pdf'):
        # Open the PDF file in read-binary mode
        with open(os.path.join(source_folder, filename), 'rb') as file:
            # Create a PDF object
            pdf = PyPDF2.PdfFileReader(file)

            # Check if the PDF has more than 10 pages
            if pdf.getNumPages() > 10:
                # Initialize the split file counter
                split_file_count = 1

                # Split the PDF into smaller PDF files with a maximum of 10 pages each
                for page in range(0, pdf.getNumPages(), 10):
                    # Create a PDF writer for the split file
                    pdf_writer = PyPDF2.PdfFileWriter()

                    # Add the pages to the PDF writer
                    for i in range(page, min(page+10, pdf.getNumPages())):
                        pdf_writer.addPage(pdf.getPage(i))

                    # Create the split file name
                    split_filename = f'subset-{split_file_count}-{filename}'

                    # Increment the split file counter
                    split_file_count += 1

                    # Create the split file in the destination folder
                    with open(os.path.join(destination_folder, split_filename), 'wb') as output:
                        # Write the split pages to the split file
                        pdf_writer.write(output)

print('Split complete!')
