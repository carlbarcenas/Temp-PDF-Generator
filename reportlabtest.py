from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm, mm
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont


#-------------------------------INITIALIZE----------------------------------
# Create and Initialize Report Page
pdf = canvas.Canvas("test.pdf") # CHANGEME
canvas.Canvas.setPageSize(pdf, (landscape(A4))) #8.27 x 11.69 inches

#--------------------------------PAGE 1: OFFENSE----------------------------
# Add Title and Subtitle
pdf.drawCentredString(5.845*inch, 7.75*inch, "POST GAME SHORT REPORT")
pdf.drawCentredString(5.845*inch, 7.55*inch, "Golden Eagles vs. NULL")

#****Offensive Tempo Analysis (OTA)
# Section Title String
pdf.drawString(0.5*inch, 6.75*inch, "OFFENSIVE TEMPO ANALYSIS")

# Variable Declaration for OTA
labels = None
poss = None
col_PPP = None

deadball_PPP = 0.00
madeBasket_PPP = 0.00
defRebound_PPP = 0.00
steal_PPP = 0.00
offRebound_PPP = 0.00

headers = [labels, poss, "1-6\nseconds", "7-12\nseconds", "13-18\nseconds", "19-24\nseconds", "25-30\nseconds", col_PPP]
data = [headers,
        ["Deadball",            100, 0, 0, 0, 0, 0, str(deadball_PPP) + " PPP"],
        ["Made Basket",         100, 0, 0, 0, 0, 0, str(madeBasket_PPP) + " PPP"],
        ["Defensive Rebound",   100, 0, 0, 0, 0, 0, str(defRebound_PPP) + " PPP"],
        ["Steal",               100, 0, 0, 0, 0, 0, str(steal_PPP) + " PPP"],
        ["Offensive Rebound",   100, 0, 0, 0, 0, 0, str(offRebound_PPP) + " PPP"],
        ["Overall",             100, 0, 0, 0, 0, 0, None],
        [None, None,            str(0.0)+" PPP", str(0.0)+" PPP", str(0.0)+" PPP", str(0.0)+" PPP", str(0.0)+" PPP", None]]

t=Table(data)#, colWidths=12*mm, rowHeights=5*mm) # Create Table
t.setStyle(TableStyle([
        ('ALIGN',(0,0),(-1,-1),'CENTER'), # Alignment for main table
        ('ALIGN', (0,0),(0,8),'RIGHT'), # Row Label Alignment
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'), # Vertical Alignment
        ('INNERGRID', (2,1), (-2, -2), 0.25, colors.wheat), # Add Grid
        ('BOX', (2,1), (-2,-2), 0.25, colors.black), # Add Box
        ('BACKGROUND', (2,1), (-2, -2), colors.navy),
        ('TEXTCOLOR', (2,1), (-2,-2), colors.wheat)
]))

t.wrapOn(pdf, 1.1*inch, 2.81*inch) # Determine table size
t.drawOn(pdf, 0.25*inch, 4.5*inch) # Determine table coords and draw


#--------------------------------PAGE 2: DEFENSE----------------------------
pdf.showPage()  # End previous page, begin new page

pdf.drawString(4*inch,2*inch, "TEST")



#-------------------------------SAVE CHANGES AND CLOSE----------------------
pdf.save()