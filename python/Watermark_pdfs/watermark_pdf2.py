import PyPDF2

template = PyPDF2.PdfFileReader(open(“inputPDF”, ‘rb’))
watermark = PyPDF2.PdfFileReader(open(“WaterMarkPDF”, ‘rb’))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
page = template.getPage(i)
page.mergePage(watermark.getPage(0))
output.addPage(page)

file = open(“waterMarked_PDF.pdf”, ‘wb’)
output.write(file)