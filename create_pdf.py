from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

doc = SimpleDocTemplate(
    "C:/Users/Dwigh/OneDrive/Desktop/Projects/Grant Writer/Pleasant_Park_Executive_Summary.pdf",
    pagesize=letter,
    rightMargin=0.75*inch,
    leftMargin=0.75*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=24, textColor=HexColor('#1a365d'), spaceAfter=6, alignment=1)
subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=14, textColor=HexColor('#4a5568'), spaceAfter=20, alignment=1)
heading_style = ParagraphStyle('Heading', parent=styles['Heading2'], fontSize=14, textColor=HexColor('#2c5282'), spaceBefore=16, spaceAfter=8)
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, leading=14, spaceAfter=8)
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10, leading=14, leftIndent=20, spaceAfter=4)

content = []

# Title
content.append(Paragraph("Pleasant Park Public School", title_style))
content.append(Paragraph("Library Learning Commons Modernization", subtitle_style))
content.append(Paragraph("Executive Summary", subtitle_style))
content.append(Spacer(1, 0.3*inch))

# Header
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
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))
content.append(header_table)
content.append(Spacer(1, 0.3*inch))

# Overview
content.append(Paragraph("PROJECT OVERVIEW", heading_style))
content.append(Paragraph("Pleasant Park Public School seeks approximately $250,000 for a comprehensive library modernization project transforming the traditional library into a modern Library Learning Commons. This project will enhance student learning, support technology integration, improve accessibility, and create a community hub for the school.", body_style))

# Challenge
content.append(Paragraph("THE CHALLENGE", heading_style))
challenge_data = [
    ['Issue', 'Detail'],
    ['Funding Gap', '$250,000 required; most grants cap at $10,000-$30,000'],
    ['Charitable Status', 'Schools cannot apply directly to most major foundations'],
    ['Stacking Required', 'Multiple smaller grants needed to reach target'],
]
challenge_table = Table(challenge_data, colWidths=[1.8*inch, 4.5*inch])
challenge_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2c5282')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cbd5e0')),
]))
content.append(challenge_table)
content.append(Spacer(1, 0.2*inch))

# Funding Opportunities
content.append(Paragraph("FUNDING OPPORTUNITIES", heading_style))

# Tier 1
content.append(Paragraph("Tier 1: Major Capital Grants ($50,000+)", bullet_style))
tier1_data = [
    ['Source', 'Amount', 'Status'],
    ['Canada Cultural Spaces Fund', '50% of costs', 'High priority'],
    ['Enabling Accessibility Fund', 'Up to $100,000', 'High priority'],
]
tier1_table = Table(tier1_data, colWidths=[3*inch, 1.5*inch, 1.5*inch])
tier1_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2c5282')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cbd5e0')),
]))
content.append(tier1_table)
content.append(Spacer(1, 0.15*inch))

# Tier 2
content.append(Paragraph("Tier 2: Corporate & Foundation Grants ($10,000-$50,000)", bullet_style))
tier2_data = [
    ['Source', 'Amount', 'Deadline'],
    ['Canada Post Community Foundation', 'Up to $25,000', 'February 2027'],
    ['TELUS Community Board', 'Up to $20,000', 'Quarterly'],
    ['RBC Foundation', 'Up to $25,000', 'Ongoing'],
    ['TD Friends of the Environment', 'Up to $10,000', 'Quarterly'],
    ['Ottawa Community Foundation', 'Up to $25,000+', 'Rolling'],
    ['Indigo Love of Reading', '$30,000/3 years', 'February annually'],
]
tier2_table = Table(tier2_data, colWidths=[3*inch, 1.5*inch, 1.5*inch])
tier2_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#4a5568')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cbd5e0')),
]))
content.append(tier2_table)
content.append(Spacer(1, 0.15*inch))

# Tier 3
content.append(Paragraph("Tier 3: School Board & Community Sources", bullet_style))
tier3_data = [
    ['Source', 'Amount', 'Notes'],
    ['Education Foundation of Ottawa', 'Varies', 'OCDSB schools eligible'],
    ['OCDSB School Council Grant', '$1,000', 'Fall application'],
    ['Community Fundraising', '$10,000-$25,000', 'Events, donations'],
]
tier3_table = Table(tier3_data, colWidths=[3*inch, 1.5*inch, 1.5*inch])
tier3_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#718096')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cbd5e0')),
]))
content.append(tier3_table)
content.append(Spacer(1, 0.2*inch))

# Key Barrier
content.append(Paragraph("KEY BARRIER: CHARITABLE STATUS", heading_style))
content.append(Paragraph("Most major foundations require applicants to be registered charities. Public schools are not charities. This means Pleasant Park cannot apply directly to most funding sources.", body_style))
content.append(Paragraph("Solution: Partner with a registered charity who can apply on the school's behalf:", body_style))
content.append(Paragraph("- Ottawa Community Foundation (fiscal sponsorship)", bullet_style))
content.append(Paragraph("- Education Foundation of Ottawa", bullet_style))
content.append(Paragraph("- Local service clubs (Rotary, Kiwanis, Lions)", bullet_style))
content.append(Spacer(1, 0.15*inch))

# Strategy
content.append(Paragraph("RECOMMENDED STRATEGY", heading_style))
content.append(Paragraph("Phase 1: Immediate Actions (This Week)", bullet_style))
content.append(Paragraph("- Contact Ottawa Community Foundation about fiscal sponsorship", bullet_style))
content.append(Paragraph("- Contact Education Foundation of Ottawa for partnership", bullet_style))
content.append(Paragraph("- Request meeting with OCDSB facilities department", bullet_style))
content.append(Spacer(1, 0.1*inch))
content.append(Paragraph("Phase 2: Large Capital Applications (Next 2 Weeks)", bullet_style))
content.append(Paragraph("- Contact Canada Cultural Spaces Fund program officer", bullet_style))
content.append(Paragraph("- Research Enabling Accessibility Fund intake dates", bullet_style))
content.append(Paragraph("- Obtain 3 preliminary renovation quotes", bullet_style))
content.append(Spacer(1, 0.1*inch))
content.append(Paragraph("Phase 3: Stacked Applications (Ongoing)", bullet_style))
content.append(Paragraph("- Submit corporate foundation applications quarterly", bullet_style))
content.append(Paragraph("- Apply to Canada Post Community Foundation (Feb 2027)", bullet_style))
content.append(Paragraph("- Launch community fundraising campaign", bullet_style))
content.append(Spacer(1, 0.2*inch))

# Projected Funding
content.append(Paragraph("PROJECTED FUNDING", heading_style))
funding_data = [
    ['Source', 'Potential Amount'],
    ['Canada Cultural Spaces Fund', '$100,000-$125,000'],
    ['Enabling Accessibility Fund', '$50,000-$100,000'],
    ['Corporate/Foundation Grants (stacked)', '$50,000-$100,000'],
    ['OCDSB Board Funding', '$25,000-$50,000'],
    ['Community Fundraising', '$10,000-$25,000'],
    ['TOTAL', '$235,000-$400,000'],
]
funding_table = Table(funding_data, colWidths=[3.5*inch, 2.5*inch])
funding_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2c5282')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -2), 'Helvetica'),
    ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ('BACKGROUND', (0, -1), (-1, -1), HexColor('#e2e8f0')),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cbd5e0')),
]))
content.append(funding_table)
content.append(Spacer(1, 0.2*inch))

# Conclusion
content.append(Paragraph("CONCLUSION", heading_style))
content.append(Paragraph("The $250,000 library modernization project is achievable through strategic grant stacking and charitable partnership. The critical first step is securing a charitable partner to unlock access to major funding sources.", body_style))
content.append(Paragraph("With coordinated effort across multiple funding streams, Pleasant Park can reasonably expect to secure $150,000-$250,000 in external funding over 2-3 years, covering a significant portion of the project cost.", body_style))

# Build PDF
doc.build(content)
print("PDF created successfully!")