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
-


***********
-
crontab -e
-

in Terminal:

* crontab -e
* press i
* write the script
* ese button
* then press :qw in order to exit end save the script
* in crontab -l , can see the new crontab installed



-
In order to allow mac use corn
-
go to apple settings >> Security & Privacy >> Privacy >> Full Disk Access 
![image](https://user-images.githubusercontent.com/63398613/210371553-717b5d1c-2547-4a42-9785-4f88f8b604b8.png)

allow corn and smbd and Terminal

in Terminal:
which corn >> will show the path and by finder>> Go >> find the file and drag to the Privacy area in the Security & Privacy



--
The Script for the 3 programs:
--
![image](https://user-images.githubusercontent.com/63398613/210372458-bf820ecd-589b-460f-a287-16f7f1f2f009.png)


