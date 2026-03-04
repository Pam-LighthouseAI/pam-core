#!/usr/bin/env python
"""
Grant Template Library - Markdown to PDF Converter
Converts all markdown templates to professional PDF documents using ReportLab
"""

import os
import re
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, 
    PageBreak, ListFlowable, ListItem, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

# Base directory
BASE_DIR = Path(r"C:\nanobot\instance3\workspace\grant_templates")

# Define colors
DARK_BLUE = colors.HexColor('#1a365d')
MEDIUM_BLUE = colors.HexColor('#2c5282')
LIGHT_BLUE = colors.HexColor('#4299e1')
VERY_LIGHT_BLUE = colors.HexColor('#ebf8ff')
GRAY_TEXT = colors.HexColor('#4a5568')
LIGHT_GRAY = colors.HexColor('#f7fafc')
BORDER_GRAY = colors.HexColor('#cbd5e0')

def create_styles():
    """Create custom paragraph styles for the PDF"""
    styles = getSampleStyleSheet()
    
    # Title style (H1)
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=DARK_BLUE,
        spaceAfter=20,
        spaceBefore=10,
        fontName='Helvetica-Bold',
    ))
    
    # Heading 2
    styles.add(ParagraphStyle(
        name='CustomH2',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=MEDIUM_BLUE,
        spaceAfter=12,
        spaceBefore=25,
        fontName='Helvetica-Bold',
    ))
    
    # Heading 3
    styles.add(ParagraphStyle(
        name='CustomH3',
        parent=styles['Heading3'],
        fontSize=13,
        textColor=colors.HexColor('#2d3748'),
        spaceAfter=10,
        spaceBefore=18,
        fontName='Helvetica-Bold',
    ))
    
    # Heading 4
    styles.add(ParagraphStyle(
        name='CustomH4',
        parent=styles['Heading4'],
        fontSize=11,
        textColor=GRAY_TEXT,
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold',
    ))
    
    # Body text
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#333333'),
        spaceAfter=8,
        spaceBefore=4,
        alignment=TA_JUSTIFY,
        leading=14,
    ))
    
    # Bullet list item
    styles.add(ParagraphStyle(
        name='CustomBullet',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#333333'),
        spaceAfter=4,
        leftIndent=20,
        bulletIndent=10,
        leading=13,
    ))
    
    # Blockquote
    styles.add(ParagraphStyle(
        name='CustomQuote',
        parent=styles['Normal'],
        fontSize=10,
        textColor=MEDIUM_BLUE,
        spaceAfter=10,
        spaceBefore=10,
        leftIndent=20,
        rightIndent=20,
        backColor=VERY_LIGHT_BLUE,
        borderPadding=10,
        fontName='Helvetica-Oblique',
        leading=14,
    ))
    
    # Code block
    styles.add(ParagraphStyle(
        name='CustomCode',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#e2e8f0'),
        spaceAfter=10,
        spaceBefore=10,
        leftIndent=10,
        rightIndent=10,
        backColor=colors.HexColor('#2d3748'),
        fontName='Courier',
        leading=12,
    ))
    
    return styles

def clean_text(text):
    """Clean text for PDF rendering"""
    # Replace emojis with text equivalents
    emoji_replacements = {
        '📋': '[CHECKLIST]',
        '📁': '[LIBRARY]',
        '🎯': '[TARGET]',
        '🚀': '[QUICK START]',
        '📊': '[STATISTICS]',
        '📞': '[CONTACT]',
        '💡': '[TIP]',
        '📈': '[OUTCOMES]',
        '🔗': '[RESOURCES]',
        '⚠️': '[WARNING]',
        '✅': '[DONE]',
        '✓': '[OK]',
        '☐': '[ ]',
        '☑': '[X]',
        '█': '|',
    }
    
    for emoji, replacement in emoji_replacements.items():
        text = text.replace(emoji, replacement)
    
    # Escape special characters for reportlab
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    
    # Handle bold (**text** or __text__)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
    
    # Handle italic (*text* or _text_) - be careful not to match already processed
    text = re.sub(r'(?<!\*)\*(?!\*)([^*]+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
    
    # Handle inline code (`code`)
    text = re.sub(r'`([^`]+?)`', r'<font face="Courier" size="9">\1</font>', text)
    
    # Handle links [text](url)
    text = re.sub(r'\[([^\]]+?)\]\(([^)]+?)\)', r'<link href="\2" color="#2b6cb0">\1</link>', text)
    
    return text

def parse_table(lines, start_idx):
    """Parse a markdown table and return table data and end index"""
    table_data = []
    i = start_idx
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip separator line
        if re.match(r'^[\|\-\s:]+$', line):
            i += 1
            continue
        
        # Check if line is part of table
        if '|' in line:
            # Split by | and clean up
            parts = line.split('|')
            cells = []
            for part in parts:
                part = part.strip()
                if part:  # Skip empty parts (from leading/trailing |)
                    cells.append(clean_text(part))
            
            if cells:  # Only add if we have cells
                table_data.append(cells)
            i += 1
        else:
            break
    
    return table_data, i

def parse_list(lines, start_idx, ordered=False):
    """Parse a markdown list and return list items and end index"""
    items = []
    i = start_idx
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for list item
        if ordered:
            match = re.match(r'^\d+\.\s+(.+)$', line)
        else:
            match = re.match(r'^[-*]\s+(.+)$', line)
        
        if match:
            items.append(clean_text(match.group(1)))
            i += 1
        else:
            break
    
    return items, i

def parse_code_block(lines, start_idx):
    """Parse a code block and return code content and end index"""
    code_lines = []
    i = start_idx + 1  # Skip opening ```
    
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('```'):
            break
        code_lines.append(line)
        i += 1
    
    return ''.join(code_lines), i + 1

def create_table_element(table_data, styles):
    """Create a formatted table element"""
    if not table_data or len(table_data) < 1:
        return None
    
    # Normalize row lengths - find max columns
    max_cols = max(len(row) for row in table_data)
    
    # Pad rows to have equal columns
    normalized_data = []
    for row in table_data:
        padded_row = row + [''] * (max_cols - len(row))
        normalized_data.append(padded_row)
    
    # Determine column widths based on content
    available_width = 6.5 * inch
    col_widths = []
    
    for col_idx in range(max_cols):
        max_content = 0
        for row in normalized_data:
            if col_idx < len(row):
                max_content = max(max_content, len(row[col_idx]))
        # Estimate width based on content
        col_widths.append(min(available_width / max_cols, max(1.5*inch, max_content * 0.1*inch)))
    
    # Normalize widths to fit page
    total_width = sum(col_widths)
    if total_width > available_width:
        scale = available_width / total_width
        col_widths = [w * scale for w in col_widths]
    
    # Create paragraph objects for each cell
    formatted_data = []
    for row_idx, row in enumerate(normalized_data):
        formatted_row = []
        for cell in row:
            if row_idx == 0:  # Header row
                style = ParagraphStyle(
                    name='TableHeader',
                    fontSize=9,
                    textColor=colors.white,
                    fontName='Helvetica-Bold',
                    alignment=TA_LEFT,
                )
            else:
                style = ParagraphStyle(
                    name='TableCell',
                    fontSize=9,
                    textColor=colors.HexColor('#333333'),
                    fontName='Helvetica',
                    alignment=TA_LEFT,
                )
            formatted_row.append(Paragraph(cell, style))
        formatted_data.append(formatted_row)
    
    # Create table
    table = Table(formatted_data, colWidths=col_widths)
    
    # Build table style commands
    num_rows = len(formatted_data)
    style_commands = [
        # Header styling
        ('BACKGROUND', (0, 0), (-1, 0), MEDIUM_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        
        # Body styling
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        
        # Grid
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
        ('BOX', (0, 0), (-1, -1), 1, MEDIUM_BLUE),
        
        # Alignment
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]
    
    # Add alternating row colors for body rows
    for row_idx in range(1, num_rows):
        if row_idx % 2 == 1:  # Odd rows (1, 3, 5, ...)
            style_commands.append(('BACKGROUND', (0, row_idx), (-1, row_idx), LIGHT_GRAY))
    
    table.setStyle(TableStyle(style_commands))
    
    return table

def markdown_to_elements(markdown_content, styles):
    """Convert markdown content to ReportLab elements"""
    elements = []
    lines = markdown_content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip empty lines
        if not stripped:
            i += 1
            continue
        
        # Horizontal rule
        if stripped in ['---', '***', '___']:
            elements.append(HRFlowable(
                width="100%",
                thickness=1,
                color=BORDER_GRAY,
                spaceBefore=15,
                spaceAfter=15
            ))
            i += 1
            continue
        
        # Code block
        if stripped.startswith('```'):
            code_content, i = parse_code_block(lines, i)
            code_text = clean_text(code_content.replace('\n', '<br/>'))
            elements.append(Paragraph(f'<font face="Courier" size="8">{code_text}</font>', styles['CustomCode']))
            continue
        
        # Heading 1
        if stripped.startswith('# '):
            text = clean_text(stripped[2:])
            elements.append(Paragraph(text, styles['CustomTitle']))
            elements.append(HRFlowable(width="100%", thickness=2, color=MEDIUM_BLUE, spaceAfter=15))
            i += 1
            continue
        
        # Heading 2
        if stripped.startswith('## '):
            text = clean_text(stripped[3:])
            elements.append(Paragraph(text, styles['CustomH2']))
            i += 1
            continue
        
        # Heading 3
        if stripped.startswith('### '):
            text = clean_text(stripped[4:])
            elements.append(Paragraph(text, styles['CustomH3']))
            i += 1
            continue
        
        # Heading 4
        if stripped.startswith('#### '):
            text = clean_text(stripped[5:])
            elements.append(Paragraph(text, styles['CustomH4']))
            i += 1
            continue
        
        # Table
        if '|' in stripped and not stripped.startswith('>'):
            table_data, i = parse_table(lines, i)
            if table_data and len(table_data) > 0:
                table = create_table_element(table_data, styles)
                if table:
                    elements.append(table)
                    elements.append(Spacer(1, 10))
            continue
        
        # Unordered list
        if stripped.startswith('- ') or stripped.startswith('* '):
            list_items, i = parse_list(lines, i, ordered=False)
            for item in list_items:
                bullet_text = f'<bullet>&bull;</bullet> {item}'
                elements.append(Paragraph(bullet_text, styles['CustomBullet']))
            continue
        
        # Ordered list
        if re.match(r'^\d+\.\s+', stripped):
            list_items, i = parse_list(lines, i, ordered=True)
            for idx, item in enumerate(list_items, 1):
                numbered_text = f'{idx}. {item}'
                elements.append(Paragraph(numbered_text, styles['CustomBullet']))
            continue
        
        # Blockquote
        if stripped.startswith('>'):
            text = clean_text(stripped[1:].strip())
            elements.append(Paragraph(text, styles['CustomQuote']))
            i += 1
            continue
        
        # Regular paragraph
        text = clean_text(stripped)
        elements.append(Paragraph(text, styles['CustomBody']))
        i += 1
    
    return elements

def convert_to_pdf(md_path, pdf_path):
    """Convert a markdown file to PDF"""
    print(f"Converting: {md_path.name}")
    
    # Read markdown content
    with open(md_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Create PDF document
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Create styles
    styles = create_styles()
    
    # Convert markdown to elements
    elements = markdown_to_elements(markdown_content, styles)
    
    # Build PDF
    doc.build(elements)
    
    print(f"  Created: {pdf_path.name}")

def main():
    """Main function to convert all markdown files to PDF"""
    print("=" * 60)
    print("Grant Template Library - PDF Converter")
    print("=" * 60)
    print()
    
    # List of files to convert
    files_to_convert = [
        ("README.md", "README.pdf"),
        ("templates/united_way_full.md", "templates/united_way_full.pdf"),
        ("templates/united_way_canada_template.md", "templates/united_way_canada_template.pdf"),
        ("templates/federal_canada.md", "templates/federal_canada.pdf"),
        ("templates/foundation_private.md", "templates/foundation_private.pdf"),
        ("templates/corporate_sponsorship.md", "templates/corporate_sponsorship.pdf"),
        ("sections/organization_sections.md", "sections/organization_sections.pdf"),
        ("budgets/budget_templates.md", "budgets/budget_templates.pdf"),
        ("samples/youth_mentoring_sample.md", "samples/youth_mentoring_sample.pdf"),
        ("samples/sample_proposal.md", "samples/sample_proposal.pdf"),
        ("checklists/submission_checklists.md", "checklists/submission_checklists.pdf"),
        ("research/united_way_east_ontario.md", "research/united_way_east_ontario.pdf"),
        ("research/quick_reference.md", "research/quick_reference.pdf"),
    ]
    
    converted = 0
    errors = 0
    
    for md_rel, pdf_rel in files_to_convert:
        md_path = BASE_DIR / md_rel
        pdf_path = BASE_DIR / pdf_rel
        
        if md_path.exists():
            try:
                convert_to_pdf(md_path, pdf_path)
                converted += 1
            except Exception as e:
                print(f"  ERROR: {e}")
                import traceback
                traceback.print_exc()
                errors += 1
        else:
            print(f"SKIPPED: {md_rel} (not found)")
    
    print()
    print("=" * 60)
    print(f"Conversion complete!")
    print(f"  Successfully converted: {converted} files")
    print(f"  Errors: {errors}")
    print("=" * 60)

if __name__ == "__main__":
    main()
