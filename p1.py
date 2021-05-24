Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import PyPDF2

pdffileobj = open('EE_GATEPaper_2020.pdf','rb')
pdfreader =  PyPDF2.pdfFilereader(pdffileobj)

x = pdfreader.numPages
pageobj=pdfreader.getPage(x-1)
text=pageobj.extractText()

file1=open(r"C:\Users\jeeii\OneDrive\Desktop\P\\S.txt","a")
file1.writelines(text)
file1.close()