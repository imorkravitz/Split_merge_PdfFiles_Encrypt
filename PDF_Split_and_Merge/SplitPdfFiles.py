# Import the necessary libraries
import PyPDF2
import os
import logging

# Set the source and destination folders
source_folder = "/Users/orkravitz/Downloads/ProtectMyPDF/pdf_toSplit_toEncrypt"
destination_folder = "/Users/orkravitz/Downloads/ProtectMyPDF/pdf_toSplit_toEncrypt"

# create a logger
logger = logging.getLogger("MyLog")
logger.setLevel(logging.DEBUG)

# create a file handler
file_handler = logging.FileHandler("/Users/orkravitz/Downloads/ProtectMyPDF/Log/SplitLogFile.log")
file_handler.setLevel(logging.DEBUG)

# create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add the formatter to the file handler
file_handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(file_handler)

# Iterate through the files in the source folder
for filename in os.listdir(source_folder):
    # Check if the file is a PDF and has more than 10 pages
    logger.info("Check for Pdf files over 10 pages.")

    if filename.endswith('.pdf'):
        # Open the PDF file in read-binary mode
        with open(os.path.join(source_folder, filename), 'rb') as file:
            # Create a PDF object
            pdf = PyPDF2.PdfFileReader(file)
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
                    split_filename = "subset-{}-{}".format(split_file_count, filename)

                    # Increment the split file counter
                    split_file_count += 1

                    # Create the split file in the destination folder
                    with open(os.path.join(destination_folder, split_filename), 'wb') as output:
                        # Write the split pages to the split file
                        pdf_writer.write(output)

                # Delete the original PDF file
                logger.info("Original file removed: " + filename)
                logger.info("Split file created: " + split_filename)
                os.remove(os.path.join(source_folder, filename))

                logger.info('Split complete!')

    else:
        logger.info("Folder is empty.")


