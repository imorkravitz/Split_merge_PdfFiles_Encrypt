import fitz
import os
from collections import defaultdict

owner_pass = "AzUyT67U4$xZ098Pl%1Mxq3"  # owner password
user_pass = "AzUyT67U4$xZ098Pl%1Mxq3"  # user password
encrypt_meth = fitz.PDF_ENCRYPT_AES_256  # strongest algorithm

perm = int(
    fitz.PDF_PERM_ACCESSIBILITY  # always use this
    | fitz.PDF_PERM_PRINT  # permit printing
    | fitz.PDF_PERM_COPY  # permit copying
    | fitz.PDF_PERM_ANNOTATE  # permit annotations
)


def merge_pdfs(source_folder, destination_folder):
    # get a list of all PDF files in the source folder
    pdf_files = [f for f in os.listdir(source_folder) if f != ".DS_Store" and f.endswith(".pdf")]

    # sort the list of PDF files
    pdf_files.sort()

    # create a dictionary to store the PDF documents for each group
    pdf_documents = {}
    # iterate through the PDF files
    for pdf_file in pdf_files:
        # check if the PDF file starts with "subset_"
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
        # check if we have more than one PDF document to merge
        if len(documents) > 1:
            # create a new PDF document to hold the merged result
            merged_pdf = fitz.open()
            # iterate through the PDF documents and append them to the merged PDF
            for pdf_document in documents:
                merged_pdf.insert_pdf(pdf_document)
            # save the encrypted PDF to the destination folder
            file_path = os.path.join(destination_folder, group_name)
            merged_pdf.save(file_path, garbage=3, encryption=encrypt_meth, owner_pw=owner_pass, permissions=perm)

        # close all PDF documents
    for documents in pdf_documents.values():
        for pdf_document in documents:
            pdf_document.close()


print('Merge complete!')

# define the source and destination folders
source_folder = "/Users/orkravitz/Downloads/ProtectMyPDF/merge_source/"
destination_folder = "/Users/orkravitz/Downloads/ProtectMyPDF/merge_dest/"
# merge the PDF files in the source folder and save the result to the destination folder
merge_pdfs(source_folder, destination_folder)

# run the program again for the next subset of PDF files (e.g. subset_1, subset_2, etc.)
merge_pdfs(source_folder, destination_folder)
