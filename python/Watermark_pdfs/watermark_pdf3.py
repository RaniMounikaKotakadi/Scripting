# watermarker.py
from PyPDF2 import PdfFileWriter, PdfFileReader
def watermark(inputpdf, outputpdf, watermarkpdf):
    watermark = PdfFileReader(watermarkpdf)
    watermarkpage = watermark.getPage(0)
    pdf = PdfFileReader(inputpdf)
    pdfwrite = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        pdfpage = pdf.getPage(page)
        pdfpage.mergePage(watermarkpage)
        pdfwrite.addPage(pdfpage)
    with open(outputpdf, 'wb') as fh:
        pdfwrite.write(fh)
if __name__ == '__main__':
    watermark(inputpdf='Automating Deployment of S3 using Cloud-Formation.pdf',
              outputpdf='watermarked_w9.pdf',
              watermarkpdf='candlwatermark.pdf')