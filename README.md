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
In order to execute script using mac:
-
in the directory: library/launchdaemons/

add .plist file

_

Format:
-

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>com.example.program1</string>
    <key>Program</key>
    <string>/path/to/program1</string>
    <key>StartInterval</key>
    <integer>3600</integer>
  </dict>
</plist>


save and put in the directroy.

-
then open Terminal and do this:
-
1. sudo chown root:wheel /Library/LaunchDaemons/myfile.plist
2. sudo chmod 600 /Library/LaunchDaemons/myfile.plist

and execute command:

sudo launchctl load /library/launchdaemons/myfile.plist

***********
