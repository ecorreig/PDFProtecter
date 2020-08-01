# PDFProtecter

This is a small script to password protect several PDF files *with different password for each one of them*.
Furthermore, it does it recursively for all pdf files in all the subdirectories of the chosen folder (Note that
the pdf files directly in the root folder are not processed.) The script outputs a txt file with the passwords
of all the processed files in that directory. Furthermore, you can set a "mother" password for all the files.

Python 3.6 is required, since I got attached to f-strings and the secrets package dependency needs it too.

## TODO
- Some error handling
- Better directory handling
- Maybe output passwords in a separate directory
