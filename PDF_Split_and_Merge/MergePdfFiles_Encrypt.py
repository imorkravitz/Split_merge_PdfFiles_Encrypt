import fitz
import os
import logging
import time

owner_pass = "***"  # owner password
user_pass = "***"  # user password
encrypt_meth = fitz.PDF_ENCRYPT_AES_256  # strongest algorithm

# create a logger
logger = logging.getLogger("MyLog")
logger.setLevel(logging.DEBUG)

# create a file handler
file_handler = logging.FileHandler("/Users/orkravitz/Downloads/ProtectMyPDF/Log/MergeLogFile.log")
file_handler.setLevel(logging.DEBUG)

# create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add the formatter to the file handler
file_handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(file_handler)

perm = int(
    fitz.PDF_PERM_ACCESSIBILITY  # always use this
    | fitz.PDF_PERM_PRINT  # permit printing
    | fitz.PDF_PERM_COPY  # permit copying
    | fitz.PDF_PERM_ANNOTATE  # permit annotations
)

def merge_pdfs(source_folder, destination_folder):
    logger.info("Check for Pdf files to merge.")

    # get a list of all PDF files in the source folder
    pdf_files = [f for f in os.listdir(source_folder) if f != ".DS_Store" and f.endswith(".pdf")]
    logger.info("Folder is empty.")

    # sort the list of PDF files
    pdf_files.sort()

    # create a dictionary to store the PDF documents for each group
    pdf_documents = {}

    # iterate through the PDF files
    for pdf_file in pdf_files:
        # check if the PDF file starts with "subset-"
        if pdf_file.startswith("subset-"):
            # extract the name of the group from the file name
            group_name = pdf_file.split("-")[-1]
            # open the PDF file using PyMuPDF
            pdf_document = fitz.open(os.path.join(source_folder, pdf_file))
            # add the PDF document to the dictionary
            if group_name in pdf_documents:
                pdf_documents[group_name].append(pdf_document)
            else:
                pdf_documents[group_name] = [pdf_document]

    # iterate through the groups in the dictionary
    for group_name, documents in pdf_documents.items():
        # create a new PDF document to hold the merged result
        merged_pdf = fitz.open()
        # iterate through the PDF documents and append them to the merged PDF
        for pdf_document in documents:
            merged_pdf.insert_pdf(pdf_document)
            # save the encrypted PDF to the destination folder
        file_path = os.path.join(destination_folder, group_name)
        merged_pdf.save(file_path, garbage=3, encryption=encrypt_meth, owner_pw=owner_pass, permissions=perm)
        logger.info("Files merged and saved to : " + file_path)

    # delete the subset files from the source folder
    for pdf_file in pdf_files:
        if pdf_file.startswith("subset-"):
            file_path = os.path.join(source_folder, pdf_file)
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                logger.error(f"Error: {file_path} does not exist")

    # close all PDF documents
    for documents in pdf_documents.values():
        for pdf_document in documents:
            pdf_document.close()

    logger.info('Merge complete!')
    time.sleep(10)  # Wait for 10 seconds after merging

# define the source and destination folders
source_folder = "/Users/orkravitz/Downloads/ProtectMyPDF/protected"
destination_folder = "/Users/orkravitz/Downloads/ProtectMyPDF/protected"

# merge the PDF files in the source folder and save the result to the destination folder
merge_pdfs(source_folder, destination_folder)

# run the program again for the next subset of PDF files (e.g. subset_1, subset_2, etc.)
merge_pdfs(source_folder, destination_folder)
