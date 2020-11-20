from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green, black, white

c = canvas.Canvas('simple_form.pdf')
c.setFont("Courier", 60)
# create a new PDF with Reportlab
#c = canvas.Canvas(packet, pagesize=letter)
#c.drawString(10, 100, "Hello world")
form = c.acroForm
x_loc = 153
y_loc = 334
#form.textfield(name='client', x=x_loc, y=y_loc, fillColor=white, width=170, height=20, textColor=black)
form.textfield(name='client', x=x_loc,   y=y_loc, fillColor=pink, width=264, height=20, textColor=black)
form.textfield(name='artist', x=x_loc+3, y=y_loc+60, fillColor=pink, width=264, height=20, textColor=black)
c.save()

# read your existing PDF
existing_pdf = PdfFileReader(open("contract.pdf", "rb"))
new_pdf = PdfFileReader(open("simple_form.pdf", "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
output.addPage(page)
page = new_pdf.getPage(0)
page.mergePage(existing_pdf.getPage(1))
output.addPage(page)

# page = existing_pdf.getPage(0)
# output.addPage(page)
# page = existing_pdf.getPage(1)
# output.addPage(page)
# page = existing_pdf.getPage(2)
# output.addPage(page)
# page = existing_pdf.getPage(3)
# output.addPage(page)

# page = new_pdf.getPage(0)
# page.mergePage(existing_pdf.getPage(1))
# output.addPage(page)

# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()