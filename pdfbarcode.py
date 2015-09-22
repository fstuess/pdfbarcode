#!/usr/bin/python

from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
import sys
import getopt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39

def add_BarCode(page,barText,pos=(0,0),color=(0,0,0),pagesize=A4):
    canvasPage = StringIO.StringIO()
    barcodePage = canvas.Canvas(canvasPage,pagesize=pagesize)
    barcodePage.setFillColorRGB(*color)
    barcode = code39.Extended39(barText,barWidth=0.3*mm,barHeight=10*mm,checksum=0)
    barcode.drawOn(barcodePage,pos[0],pos[1])
    barcodePage.setFont("Courier", 5*mm) # font type and size0
    barcodePage.drawRightString(200*mm, 5*mm, barText)
    barcodePage.save()
    canvasPage.seek(0)
    barcodePDF = PdfFileReader(canvasPage)
    page.mergePage(barcodePDF.getPage(0))
    return page

def usage():
    print """pdfbarcode -i file / --input=file -o file / --output=file"""
    
def getParms(argv):                         
    if len(argv)<2:
        usage()
        sys.exit(2)
    try:                                
        opts, args = getopt.getopt(argv[1:], "i:o:t:", ["input", "output", "text"])
    except getopt.GetoptError:
        print "incorrect command line"
        usage()
        sys.exit(2) 
    outputFile = None
    print "#",opts,args
    for opt, arg in opts:
        print "optarg", opt, arg
        if opt in ("-i", "--input"):
            inputFile = open(arg, "rb")
        if opt in ("-o", "--output"):
            outputFile = open(arg, "wb+")
        if opt in ("-t",  "--text"):
            text = arg
    if not outputFile:
        outputFile = sys.stdout
    return (inputFile, outputFile, text)

def write_out(newpdf,outfile):
    if outfile == sys.stdout:
        # must be seekable for pdf-writing. ugly.
        buffer = StringIO.StringIO()
        newpdf.write(buffer)
        buffer.flush()
        buffer.seek(0)
        outfile.write(buffer.read())
    else:
        newpdf.write(outfile)
        
if __name__ == "__main__":
    infile, outfile, text = getParms(sys.argv)
    pdfr = PdfFileReader(infile)
    newpdf = PdfFileWriter()
    for pageNum in range(pdfr.getNumPages()):
        page = pdfr.getPage(pageNum)
        newpdf.addPage(add_BarCode(page,text))
    write_out(newpdf, outfile)
        
        
        
        
  
