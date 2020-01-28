# PDFProtecter

This is a small scrypt to password protect several PDF files *with different passwords for each one of them*.
Furthermore, it does it recursively for all pdf files in all the subdirectories of the chosen folder (Note that
the pdf files directly in the chosen folders are not processed.) The script outputs a txt file with the passwords
of all the processed files in that directory. Furthermore, you can set a "mother" password for all the files.

I know it might be somewhat uncomfortable depending on what you are doing, but it was the way I needed it.

## TODO
- Some error handling
- Better directory handling
- Maybe output passwords in a separate file