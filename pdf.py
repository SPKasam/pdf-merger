import PyPDF2
import sys

inputs = sys.argv[1:]

def pdfmerger(inputs):
    merger = PyPDF2.PdfFileMerger()
    for pdf in inputs:
        merger.append(pdf)
    merger.write("super.pdf")

pdfmerger(inputs)
