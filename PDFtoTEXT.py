# Importing PyPDF2
import PyPDF2

# Creating a PDF File Object
pdfFileObject = open(r"KaliLinux.pdf", 'rb')

# Creating A PDF Reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

# Printing Number Of Pages In PDF File
print(" No. Of Pages :", pdfReader.numPages)

# Creating A Page Object
pageObject = pdfReader.getPage(0)

# Extracting Text From Page
print(pageObject.extractText())

# Closing The PDF File Object
pdfFileObject.close()
