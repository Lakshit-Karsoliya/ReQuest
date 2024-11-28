from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit

def create_pdf(text):
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)
    width, height = letter 
    x_margin = 50
    y_position = height - 50
    max_width = width - 2 * x_margin
    lines = text.split('\n')
    for line in lines:
        wrapped_lines = simpleSplit(line, "Helvetica", 12, max_width)
        for wrapped_line in wrapped_lines:
            c.drawString(x_margin, y_position, wrapped_line)
            y_position -= 20 
            if y_position < 50: 
                c.showPage() 
                y_position = height - 50
    c.save()
    pdf_buffer.seek(0)
    return pdf_buffer


