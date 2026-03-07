"""Generate QUICKSTART.pdf from QUICKSTART.md using ReportLab"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import re

# Read markdown
with open(r'C:\nanobot\instance3\workspace\QUICKSTART.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Create PDF
doc = SimpleDocTemplate(
    r'C:\nanobot\instance3\workspace\QUICKSTART.pdf',
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm
)

# Define styles
styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    name='CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=HexColor('#2563eb'),
    spaceAfter=20,
    spaceBefore=0,
    borderPadding=10,
))

styles.add(ParagraphStyle(
    name='CustomH2',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=HexColor('#1e40af'),
    spaceBefore=20,
    spaceAfter=10,
    borderWidth=1,
    borderColor=HexColor('#ddd'),
    borderPadding=5,
))

styles.add(ParagraphStyle(
    name='CustomH3',
    parent=styles['Heading3'],
    fontSize=12,
    textColor=HexColor('#3b82f6'),
    spaceBefore=15,
    spaceAfter=8,
))

styles.add(ParagraphStyle(
    name='CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    spaceBefore=6,
    spaceAfter=6,
))

styles.add(ParagraphStyle(
    name='CustomCode',
    parent=styles['Code'],
    fontName='Courier',
    fontSize=8,
    leading=10,
    backColor=HexColor('#f1f5f9'),
    textColor=HexColor('#1e293b'),
    leftIndent=10,
    rightIndent=10,
    spaceBefore=10,
    spaceAfter=10,
    borderWidth=1,
    borderColor=HexColor('#e2e8f0'),
    borderPadding=8,
))

styles.add(ParagraphStyle(
    name='InlineCode',
    parent=styles['Normal'],
    fontName='Courier',
    fontSize=9,
    textColor=HexColor('#b91c1c'),
    backColor=HexColor('#fef2f2'),
))

styles.add(ParagraphStyle(
    name='Footer',
    parent=styles['Normal'],
    fontSize=9,
    textColor=HexColor('#94a3b8'),
    alignment=TA_CENTER,
    spaceBefore=30,
))

# Parse and build content
story = []

lines = content.split('\n')
i = 0
in_code_block = False
code_block = []
in_table = False
table_rows = []

def process_inline(text):
    """Convert markdown inline formatting to ReportLab markup"""
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<font face="Courier" size="9" color="#dc2626" backColor="#f1f5f9">\1</font>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<link href="\2" color="#2563eb">\1</link>', text)
    return text

while i < len(lines):
    line = lines[i]
    
    # Code blocks
    if line.startswith('```'):
        if in_code_block:
            # End code block
            code_text = '\n'.join(code_block)
            story.append(Preformatted(code_text, styles['CustomCode']))
            code_block = []
            in_code_block = False
        else:
            in_code_block = True
        i += 1
        continue
    
    if in_code_block:
        code_block.append(line)
        i += 1
        continue
    
    # Tables
    if '|' in line and not line.strip().startswith('#'):
        if line.strip().startswith('|'):
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            if all(c.replace('-', '').replace(':', '') == '' for c in cells):
                # Skip separator row
                i += 1
                continue
            table_rows.append(cells)
            in_table = True
        i += 1
        continue
    elif in_table and table_rows:
        # End of table, create it
        if table_rows:
            # Determine column widths
            num_cols = len(table_rows[0])
            col_width = (doc.width - 1*cm) / num_cols
            
            # Process inline formatting in table cells
            processed_rows = []
            for row in table_rows:
                processed_row = [Paragraph(process_inline(cell), styles['CustomBody']) for cell in row]
                processed_rows.append(processed_row)
            
            t = Table(processed_rows, colWidths=[col_width]*num_cols)
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2563eb')),
                ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#ffffff')),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#ddd')),
                ('BACKGROUND', (0, 1), (-1, -1), HexColor('#ffffff')),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#ffffff'), HexColor('#f8fafc')]),
                ('LEFTPADDING', (0, 0), (-1, -1), 6),
                ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ]))
            story.append(t)
            story.append(Spacer(1, 10))
            table_rows = []
            in_table = False
        i += 1
        continue
    
    # Headers
    if line.startswith('# '):
        story.append(Paragraph(line[2:], styles['CustomTitle']))
        story.append(Spacer(1, 10))
    elif line.startswith('## '):
        story.append(Paragraph(line[3:], styles['CustomH2']))
    elif line.startswith('### '):
        story.append(Paragraph(line[4:], styles['CustomH3']))
    elif line.startswith('---'):
        story.append(Spacer(1, 15))
    elif line.strip().startswith('- '):
        text = '• ' + process_inline(line.strip()[2:])
        story.append(Paragraph(text, styles['CustomBody']))
    elif line.strip().startswith(('1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ')):
        text = process_inline(line.strip())
        story.append(Paragraph(text, styles['CustomBody']))
    elif line.strip():
        story.append(Paragraph(process_inline(line), styles['CustomBody']))
    
    i += 1

# Add footer
story.append(Spacer(1, 30))
story.append(Paragraph('nanobot Quick Start Guide — Generated 2026-03-05', styles['Footer']))

# Build PDF
doc.build(story)
print('PDF created successfully!')
