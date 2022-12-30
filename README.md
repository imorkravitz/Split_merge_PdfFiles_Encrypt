# Split_merge_PdfFiles_Encrypt
this project split PDF merged pdf files and encrypt merged files

2 Scripts:

1. Split pdf files from the source folder with adding subset-{num}-[name...]
   and split the pdf files to maximum 10 pages
   
   --- Java program that add watermarks. if pdf files contains smaller or equal to 10 pages - both scripts are no need to be use.
   
2. Merge subset-{num}-[name...] files from a source folder into one pdf file each [name] separately
   output to destination folder. the merged files are Encrypted 

Python 3.10

Libraries:
-
PyPDF2: pip install PyPDF2==2.2.1
-
PyMuPDF: pip install PyMuPDF
