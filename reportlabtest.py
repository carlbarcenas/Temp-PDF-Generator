from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm, mm
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.platypus import (Flowable, SimpleDocTemplate, Table, TableStyle)


#-------------------------------INITIALIZE----------------------------------
# Create and Initialize Report Page
pdf = canvas.Canvas("test.pdf")
canvas.Canvas.setPageSize(pdf, (landscape(A4))) #8.27 x 11.69 inches

#--------------------------------PAGE 1: OFFENSE----------------------------
# Add Title and Subtitle
pdf.drawCentredString(5.845*inch, 7.75*inch, "POST GAME SHORT REPORT")
pdf.drawCentredString(5.845*inch, 7.55*inch, "Golden Eagles vs. NULL")

# Offensive Tempo Analysis
data = [[0, 0, 0, 0, 0],   # TEMP DATA, DELETEME
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

t=Table(data, colWidths=12*mm, rowHeights=5*mm) # Create Table
t.setStyle(TableStyle([
        ('ALIGN',(0,0),(-1,-1),'CENTER'), # Alignment
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'), # Vertical Alignment
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), # Add Grid
        ('BOX', (0,0), (-1,-1), 0.25, colors.black), # Add Box
]))

# Attaching Table to Canvas'
t.wrapOn(pdf, 1.1*inch, 2.81*inch) # Determine table size
t.drawOn(pdf, 1.2*inch, 4.5*inch) # Determine table coords and draw

# Adding table row and col names



#--------------------------------PAGE 2: DEFENSE----------------------------
pdf.showPage()  # End previous page, begin new page

pdf.drawString(4*inch,2*inch, "TEST")



#-------------------------------SAVE CHANGES--------------------------------
pdf.save()