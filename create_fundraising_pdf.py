from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors

doc = SimpleDocTemplate(
    "C:/Users/Dwigh/OneDrive/Desktop/Projects/Grant Writer/Pleasant_Park_Fundraising_Options.pdf",
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
subheading_style = ParagraphStyle('SubHeading', parent=styles['Heading3'], fontSize=12, textColor=HexColor('#2d3748'), spaceBefore=12, spaceAfter=6)
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, leading=14, spaceAfter=8)
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10, leading=14, leftIndent=20, spaceAfter=4)
highlight_style = ParagraphStyle('Highlight', parent=styles['Normal'], fontSize=10, leading=14, leftIndent=20, spaceAfter=4, textColor=HexColor('#2c5282'))

content = []

# Title
content.append(Paragraph("Pleasant Park Public School", title_style))
content.append(Paragraph("High-Engagement Fundraising Options", subtitle_style))
content.append(Paragraph("Low-Cost, High-Return Events", subtitle_style))
content.append(Spacer(1, 0.3*inch))

# Header
header_data = [
    ['Prepared for:', 'Ottawa-Carleton District School Board'],
    ['Prepared by:', 'Lighthouse AI'],
    ['Date:', 'March 4, 2026'],
    ['Subject:', 'Proven Fundraising Events for Library Modernization']
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
content.append(Paragraph("OVERVIEW", heading_style))
content.append(Paragraph("The following fundraising events have been selected based on three criteria: high community engagement, low implementation cost, and proven fundraising success at other schools. Each option includes actual amounts raised by schools and implementation guidance.", body_style))
content.append(Spacer(1, 0.15*inch))

# Summary Table
content.append(Paragraph("QUICK COMPARISON", heading_style))
summary_data = [
    ['Event Type', 'Potential Revenue', 'Cost', 'Effort'],
    ['Fun Run / Walk-a-thon', '$5,000 - $25,000+', 'Very Low', 'Medium'],
    ['Read-a-thon', '$12,000 - $60,000+', 'Very Low', 'Low'],
    ['Silent Auction', '$8,000 - $15,000+', 'Low', 'High'],
    ['Restaurant Spirit Night', '$250 - $1,000/night', 'None', 'Very Low'],
    ['Movie Night', '$500 - $2,000', 'Very Low', 'Low'],
    ['Talent Show', '$500 - $3,000', 'Very Low', 'Medium'],
    ['Craft Fair', '$5,000 - $10,000+', 'Low', 'High'],
]
summary_table = Table(summary_data, colWidths=[2*inch, 1.8*inch, 1.2*inch, 1.2*inch])
summary_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2c5282')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cbd5e0')),
    ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
]))
content.append(summary_table)
content.append(Spacer(1, 0.25*inch))

# DETAILED OPTIONS

# 1. Fun Run / Walk-a-thon
content.append(Paragraph("1. FUN RUN / WALK-A-THON", heading_style))
content.append(Paragraph("HIGHEST RECOMMENDATION", highlight_style))

content.append(Paragraph("What It Is:", subheading_style))
content.append(Paragraph("Students collect pledges from family and friends for walking or running laps during a designated school event. Can be themed (color run, pajama run, superhero run) to increase excitement.", body_style))

content.append(Paragraph("Proven Results:", subheading_style))
content.append(Paragraph("- Studies show walk-a-thons raise $5,000 - $25,000 for schools", bullet_style))
content.append(Paragraph("- Crystal Springs Elementary (WA) raised $31,061 for playground and STEM", bullet_style))
content.append(Paragraph("- Apex Leadership Co has raised over $80 million for 5,000+ schools", bullet_style))
content.append(Paragraph("- One school: for every $5 raised, students threw water balloons at PE teacher", bullet_style))

content.append(Paragraph("Why It Works:", subheading_style))
content.append(Paragraph("- 100% profit (no product costs)", bullet_style))
content.append(Paragraph("- High student engagement and excitement", bullet_style))
content.append(Paragraph("- Promotes health and fitness", bullet_style))
content.append(Paragraph("- Whole school participation", bullet_style))
content.append(Paragraph("- Easy to promote via social media", bullet_style))

content.append(Paragraph("Implementation:", subheading_style))
content.append(Paragraph("- Set up online pledge platform (PledgeStar, DoJiggy, 99Pledges)", bullet_style))
content.append(Paragraph("- Choose a fun theme (color powder, costumes, obstacles)", bullet_style))
content.append(Paragraph("- Create class competitions with small prizes", bullet_style))
content.append(Paragraph("- Hold during school hours for maximum participation", bullet_style))
content.append(Paragraph("- Costs: Color powder ($50-100), prizes ($200-500)", bullet_style))

content.append(Paragraph("Estimated Revenue:", subheading_style))
content.append(Paragraph("$10,000 - $25,000 per event (based on school size of 300-500 students)", body_style))
content.append(Spacer(1, 0.15*inch))

# 2. Read-a-thon
content.append(Paragraph("2. READ-A-THON", heading_style))
content.append(Paragraph("HIGHEST RECOMMENDATION", highlight_style))

content.append(Paragraph("What It Is:", subheading_style))
content.append(Paragraph("Students collect pledges based on minutes read or books completed during a set period (typically 2 weeks). Combines fundraising with literacy promotion.", body_style))

content.append(Paragraph("Proven Results:", subheading_style))
content.append(Paragraph("- Central Elementary (TX) raised $62,484", bullet_style))
content.append(Paragraph("- Westwood Elementary (CA) raised $54,314", bullet_style))
content.append(Paragraph("- Lafayette Read-a-thon raised over $27,000", bullet_style))
content.append(Paragraph("- Typical schools raise $12,000+ with full participation", bullet_style))

content.append(Paragraph("Why It Works:", subheading_style))
content.append(Paragraph("- Aligns perfectly with school mission (literacy)", bullet_style))
content.append(Paragraph("- Very low cost - almost 100% profit", bullet_style))
content.append(Paragraph("- Parents love that it promotes reading", bullet_style))
content.append(Paragraph("- Can run alongside regular curriculum", bullet_style))
content.append(Paragraph("- Works for all ages and reading levels", bullet_style))

content.append(Paragraph("Implementation:", subheading_style))
content.append(Paragraph("- Use platform like Read-a-thon.com or ReadaFun (handles pledges)", bullet_style))
content.append(Paragraph("- Set 2-week reading period", bullet_style))
content.append(Paragraph("- Create reading challenges by grade level", bullet_style))
content.append(Paragraph("- Offer prizes for top readers and top fundraisers", bullet_style))
content.append(Paragraph("- Host reading celebrations (PJ day, hat day) at milestones", bullet_style))
content.append(Paragraph("- Costs: Platform fee (typically 10-15% of funds raised)", bullet_style))

content.append(Paragraph("Estimated Revenue:", subheading_style))
content.append(Paragraph("$15,000 - $50,000+ (depending on school size and participation)", body_style))
content.append(Spacer(1, 0.15*inch))

# 3. Silent Auction
content.append(Paragraph("3. SILENT AUCTION", heading_style))

content.append(Paragraph("What It Is:", subheading_style))
content.append(Paragraph("An evening event where attendees bid on donated items and experiences. Often combined with dinner or social event. Items donated by local businesses cost the school nothing.", body_style))

content.append(Paragraph("Proven Results:", subheading_style))
content.append(Paragraph("- Elementary schools typically raise $8,000 - $15,000", bullet_style))
content.append(Paragraph("- One school's 'skip the carpool line' pass raised $1,000+ alone", bullet_style))
content.append(Paragraph("- Front row seats at all school events: huge moneymaker, costs nothing", bullet_style))
content.append(Paragraph("- Norwood High craft fair + auction: $10,000 profit", bullet_style))

content.append(Paragraph("Why It Works:", subheading_style))
content.append(Paragraph("- High-value items at zero cost (donated)", bullet_style))
content.append(Paragraph("- Creates community social event", bullet_style))
content.append(Paragraph("- Can combine with dinner for additional revenue", bullet_style))
content.append(Paragraph("- Unique experiences (teacher for a day, principal parking spot) cost nothing", bullet_style))

content.append(Paragraph("Implementation:", subheading_style))
content.append(Paragraph("- Start soliciting donations 2-3 months ahead", bullet_style))
content.append(Paragraph("- Create themed baskets (spa day, movie night, sports)", bullet_style))
content.append(Paragraph("- Include school-specific experiences:", bullet_style))
content.append(Paragraph("  - 'Skip the carpool line' pass", bullet_style))
content.append(Paragraph("  - Front row seats at events", bullet_style))
content.append(Paragraph("  - Teacher for a day", bullet_style))
content.append(Paragraph("  - Principal parking spot for a month", bullet_style))
content.append(Paragraph("- Use mobile bidding platform (BetterWorld, Handbid)", bullet_style))
content.append(Paragraph("- Costs: Venue, food, bidding platform", bullet_style))

content.append(Paragraph("Estimated Revenue:", subheading_style))
content.append(Paragraph("$8,000 - $15,000 (one-time event)", body_style))
content.append(Spacer(1, 0.15*inch))

# 4. Restaurant Spirit Nights
content.append(Paragraph("4. RESTAURANT SPIRIT NIGHTS", heading_style))

content.append(Paragraph("What It Is:", subheading_style))
content.append(Paragraph("Partner with local restaurants who donate a percentage of sales from families who dine on a designated night. Also called dine-to-donate or profit share nights.", body_style))

content.append(Paragraph("Proven Results:", subheading_style))
content.append(Paragraph("- Schools report $250 - $1,000 per night", bullet_style))
content.append(Paragraph("- Rated 'very successful' and 'very easy' to run", bullet_style))
content.append(Paragraph("- McDonald's McTeacher Nights: teachers serve, draws big crowd", bullet_style))
content.append(Paragraph("- California Tortilla: 25% of sales donated", bullet_style))
content.append(Paragraph("- Most restaurants: 15-20% of sales donated", bullet_style))

content.append(Paragraph("Why It Works:", subheading_style))
content.append(Paragraph("- 100% profit (no costs to school)", bullet_style))
content.append(Paragraph("- Very low effort - restaurant does most work", bullet_style))
content.append(Paragraph("- Builds community - families dine together", bullet_style))
content.append(Paragraph("- Can run monthly for steady income", bullet_style))
content.append(Paragraph("- Local businesses get exposure", bullet_style))

content.append(Paragraph("Implementation:", subheading_style))
content.append(Paragraph("- Contact local restaurants (Chick-fil-A, McDonald's, local favorites)", bullet_style))
content.append(Paragraph("- Schedule 1-2 nights per month", bullet_style))
content.append(Paragraph("- Promote via flyers, social media, school newsletter", bullet_style))
content.append(Paragraph("- Ask teachers to attend and greet families", bullet_style))
content.append(Paragraph("- Costs: None", bullet_style))

content.append(Paragraph("Estimated Revenue:", subheading_style))
content.append(Paragraph("$3,000 - $8,000 per year (monthly events)", body_style))
content.append(Spacer(1, 0.15*inch))

# 5. Movie Night
content.append(Paragraph("5. FAMILY MOVIE NIGHT", heading_style))

content.append(Paragraph("What It Is:", subheading_style))
content.append(Paragraph("Screen a family-friendly movie in the school gym or outdoors. Sell tickets, concessions, and add-on activities. Low-cost, high-engagement community event.", body_style))

content.append(Paragraph("Proven Results:", subheading_style))
content.append(Paragraph("- Typical revenue: $500 - $2,000 per event", bullet_style))
content.append(Paragraph("- Concessions are key profit driver", bullet_style))
content.append(Paragraph("- Can run multiple times per year", bullet_style))

content.append(Paragraph("Why It Works:", subheading_style))
content.append(Paragraph("- Low cost (public performance license ~$75-150)", bullet_style))
content.append(Paragraph("- Family-friendly, builds community", bullet_style))
content.append(Paragraph("- Concessions have high profit margins", bullet_style))
content.append(Paragraph("- Can theme around seasons (Halloween, holiday)", bullet_style))

content.append(Paragraph("Implementation:", subheading_style))
content.append(Paragraph("- Obtain public performance license (SWANK, MPLC)", bullet_style))
content.append(Paragraph("- Choose popular family film", bullet_style))
content.append(Paragraph("- Set up in gym or outdoor area", bullet_style))
content.append(Paragraph("- Sell: popcorn, drinks, candy, glow sticks", bullet_style))
content.append(Paragraph("- Add: raffle, 50/50 draw, bake sale", bullet_style))
content.append(Paragraph("- Costs: License ($75-150), concessions supplies", bullet_style))

content.append(Paragraph("Estimated Revenue:", subheading_style))
content.append(Paragraph("$500 - $2,000 per event", body_style))
content.append(Spacer(1, 0.15*inch))

# 6. Talent Show
content.append(Paragraph("6. TALENT SHOW", heading_style))

content.append(Paragraph("What It Is:", subheading_style))
content.append(Paragraph("Students showcase talents (singing, dancing, comedy, etc.) in an evening performance. Sell tickets and concessions. Low-cost, high-entertainment value.", body_style))

content.append(Paragraph("Proven Results:", subheading_style))
content.append(Paragraph("- Often one of the most profitable fundraisers", bullet_style))
content.append(Paragraph("- High participation from students", bullet_style))
content.append(Paragraph("- Creates memorable school community event", bullet_style))

content.append(Paragraph("Why It Works:", subheading_style))
content.append(Paragraph("- Minimal costs (auditorium/gym already available)", bullet_style))
content.append(Paragraph("- Students are the entertainment - no hired acts", bullet_style))
content.append(Paragraph("- Parents love watching their children perform", bullet_style))
content.append(Paragraph("- Can add concession sales, raffle", bullet_style))
content.append(Paragraph("- Builds school spirit", bullet_style))

content.append(Paragraph("Implementation:", subheading_style))
content.append(Paragraph("- Hold auditions 2-3 weeks before", bullet_style))
content.append(Paragraph("- Limit acts to 2-3 minutes for pacing", bullet_style))
content.append(Paragraph("- Charge $5-10 admission", bullet_style))
content.append(Paragraph("- Sell concessions and flowers for performers", bullet_style))
content.append(Paragraph("- Have teachers or local celebrities judge", bullet_style))
content.append(Paragraph("- Costs: Prizes, printing, concessions supplies", bullet_style))

content.append(Paragraph("Estimated Revenue:", subheading_style))
content.append(Paragraph("$500 - $3,000 per event", body_style))
content.append(Spacer(1, 0.15*inch))

# 7. Craft Fair
content.append(Paragraph("7. CRAFT FAIR / VENDOR MARKET", heading_style))

content.append(Paragraph("What It Is:", subheading_style))
content.append(Paragraph("Rent tables to crafters and vendors who sell their products. School keeps table fees. Can add bake sale, raffle, food truck percentage.", body_style))

content.append(Paragraph("Proven Results:", subheading_style))
content.append(Paragraph("- Norwood High (MA) raised $10,000 profit", bullet_style))
content.append(Paragraph("- 80+ crafters participated", bullet_style))
content.append(Paragraph("- Became popular annual community event", bullet_style))

content.append(Paragraph("Why It Works:", subheading_style))
content.append(Paragraph("- Vendors pay for tables - guaranteed income", bullet_style))
content.append(Paragraph("- No inventory risk for school", bullet_style))
content.append(Paragraph("- Draws community members who may not have children at school", bullet_style))
content.append(Paragraph("- Can run annually", bullet_style))

content.append(Paragraph("Implementation:", subheading_style))
content.append(Paragraph("- Reserve date 6 months ahead", bullet_style))
content.append(Paragraph("- Charge $30-75 per table (market rate)", bullet_style))
content.append(Paragraph("- Recruit 40-80 vendors", bullet_style))
content.append(Paragraph("- Add bake sale, raffle, food trucks", bullet_style))
content.append(Paragraph("- Promote heavily in community", bullet_style))
content.append(Paragraph("- Costs: Advertising, supplies", bullet_style))

content.append(Paragraph("Estimated Revenue:", subheading_style))
content.append(Paragraph("$5,000 - $10,000 (annual event)", body_style))
content.append(Spacer(1, 0.2*inch))

# RECOMMENDED STRATEGY
content.append(Paragraph("RECOMMENDED FUNDRAISING STRATEGY", heading_style))

content.append(Paragraph("Year 1 Plan:", subheading_style))
content.append(Paragraph("- Fall: Launch Read-a-thon (primary fundraiser)", bullet_style))
content.append(Paragraph("- Winter: Silent Auction + Dinner (community event)", bullet_style))
content.append(Paragraph("- Spring: Fun Run / Walk-a-thon (high engagement)", bullet_style))
content.append(Paragraph("- Monthly: Restaurant Spirit Nights (steady income)", bullet_style))
content.append(Paragraph("- Quarterly: Family Movie Nights", bullet_style))

content.append(Paragraph("Projected Year 1 Revenue:", subheading_style))
revenue_data = [
    ['Event', 'Low Estimate', 'High Estimate'],
    ['Read-a-thon', '$15,000', '$40,000'],
    ['Silent Auction', '$8,000', '$15,000'],
    ['Fun Run', '$10,000', '$25,000'],
    ['Spirit Nights (12)', '$3,000', '$8,000'],
    ['Movie Nights (4)', '$2,000', '$6,000'],
    ['TOTAL', '$38,000', '$94,000'],
]
revenue_table = Table(revenue_data, colWidths=[2.5*inch, 1.5*inch, 1.5*inch])
revenue_table.setStyle(TableStyle([
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
    ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
]))
content.append(revenue_table)
content.append(Spacer(1, 0.2*inch))

# Key Success Factors
content.append(Paragraph("KEY SUCCESS FACTORS", heading_style))
content.append(Paragraph("1. Start with Read-a-thon: Lowest effort, highest return, aligns with school mission", bullet_style))
content.append(Paragraph("2. Use online platforms: PledgeStar, 99Pledges, Read-a-thon.com handle money collection", bullet_style))
content.append(Paragraph("3. Create competitions: Class vs. class, grade vs. grade with small prizes", bullet_style))
content.append(Paragraph("4. Promote heavily: Social media, flyers, announcements, parent emails", bullet_style))
content.append(Paragraph("5. Thank donors publicly: Recognition boards, shout-outs, thank-you videos", bullet_style))
content.append(Paragraph("6. Make it fun: Themes, costumes, silly challenges for principals/teachers", bullet_style))
content.append(Spacer(1, 0.2*inch))

# Conclusion
content.append(Paragraph("CONCLUSION", heading_style))
content.append(Paragraph("With strategic implementation of these fundraising events, Pleasant Park can realistically generate $38,000 - $94,000 in Year 1. Combined with the grant stacking strategy, the $250,000 library modernization project becomes achievable over 3-4 years.", body_style))
content.append(Paragraph("The Read-a-thon and Fun Run are especially recommended as they offer the highest return on investment, require minimal upfront costs, and promote positive values (literacy and fitness) that align with the school's educational mission.", body_style))

# Build PDF
doc.build(content)
print("PDF created successfully!")