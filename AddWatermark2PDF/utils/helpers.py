import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_watermark_pdf(watermark_text):
    c = canvas.Canvas("watermark.pdf", pagesize=letter)
    width, height = letter
    c.drawString(width / 2, height / 2, watermark_text)
    c.save()

def apply_watermark(input_pdf, watermark_text, output_pdf):
    create_watermark_pdf(watermark_text)

    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    watermark = PyPDF2.PdfReader("watermark.pdf")
    watermark_page = watermark.pages[0]

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.merge_page(watermark_page)
        pdf_writer.add_page(page)

    # Create the 'pdfs' directory if it doesn't exist
    os.makedirs("AddWatermark2PDF/pdfs", exist_ok=True)

    # Construct the output PDF path within the 'pdfs' directory
    output_pdf_path = os.path.join("AddWatermark2PDF/pdfs", output_pdf)

    with open(output_pdf_path, "wb") as output_file:
        pdf_writer.write(output_file)

    # Clean up the temporary watermark file
    os.remove("watermark.pdf")