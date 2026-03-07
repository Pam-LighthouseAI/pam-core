from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

# Create the PDF
doc = SimpleDocTemplate(
    "C:/Users/Dwigh/OneDrive/Desktop/Projects/Grant Writer/Pleasant_Park_Library_Executive_Summary.pdf",
    pagesize=letter,
    rightMargin=0.75*inch,
    leftMargin=0.75*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch
)

# Styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=HexColor('#1a365d'),
    spaceAfter=6,
    alignment=1
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=14,
    textColor=HexColor('#4a5568'),
    spaceAfter=20,
    alignment=1
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=HexColor('#2c5282'),
    spaceBefore=16,
    spaceAfter=8
)

subheading_style = ParagraphStyle(
    'SubHeading',
    parent=styles['Heading3'],
    fontSize=12,
    textColor=HexColor('#2d3748'),
    spaceBefore=12,
    spaceAfter=6
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    spaceAfter=8
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    leftIndent=20,
    spaceAfter=4
)

# Build content
content = []

# Title
content.append(Paragraph("Pleasant Park Public School", title_style))
content.append(Paragraph("Library Learning Commons Modernization", subtitle_style))
content.append(Paragraph("Executive Summary", subtitle_style))
content.append(Spacer(1, 0.3*inch))

# Header info
header_data = [
    ['Prepared for:', 'Ottawa-Carleton District School Board'],
    ['Prepared by:', 'Lighthouse AI'],
    ['Date:', 'March 4, 2026'],
    ['Subject:', 'Funding Opportunities for $250,000 Library Renovation']
]
header_table = Table(header_data, colWidths=[1.5*inch, 4.5*inch])
header_table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('TEXTCOLOR', (0, 0), (-1, -1), HexColor('#2d3748')),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))
content.append(header_table)
content.append(Spacer(1, 0.3*inch))

# Project Overview
content.append(Paragraph("PROJECT OVERVIEW", heading_style))
content.append(Paragraph(
    "Pleasant Park Public School seeks approximately