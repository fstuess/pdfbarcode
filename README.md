# pdfbarcode
Get a line with barcode and text onto pdfs
Written in python, you need reportlab and pyPdf.

Usage:

pdfbarcode.py -i input-pdf-filename  # writes to stdout

or:

pdfbarcode.py -i input-pdf-filename -o output-pdf-filename

First steps stolen from https://github.com/glokem/barcodepdf.

Todos: 
- more parameterization for positions and sizes
- checking for boundaries, text length
- multipage numbering if wanted






