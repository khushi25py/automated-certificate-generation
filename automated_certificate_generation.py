import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def create_certificate(intern_name, intern_pos, date, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter #letter=8.5X11 inches

    # Defines styles for the text
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title_style.fontName = 'Helvetica-Bold'
    title_style.fontSize = 36

    subtitle_style = styles['Heading2']
    subtitle_style.fontName = 'Helvetica-Bold'
    subtitle_style.fontSize = 24

    body_style = styles['BodyText']
    body_style.fontName = 'Helvetica'
    body_style.fontSize = 18

    # Draw the title
    c.setFont(title_style.fontName, title_style.fontSize)
    c.drawCentredString(width / 2, height - 2 * inch, "Certificate of Completion")

    # Draw the subtitle
    c.setFont(subtitle_style.fontName, subtitle_style.fontSize)
    c.drawCentredString(width / 2, height - 3 * inch, "This is to certify that")

    # Draw the intern's name
    c.setFont(body_style.fontName, body_style.fontSize + 10)
    c.drawCentredString(width / 2, height - 4 * inch, intern_name)

    c.setFont(body_style.fontName, body_style.fontSize)
    text = f"has successfully completed the internship as."
    c.drawCentredString(width / 2, height - 4.5* inch, text)

    c.setFont(body_style.fontName,body_style.fontSize)
    text=f"{intern_pos} on {date}."
    c.drawCentredString(width/2,height -5* inch,text)

    c.setFont(body_style.fontName, subtitle_style.fontSize)
    c.drawCentredString(width / 2, height - 6 * inch, "Congratulations!")

    c.save()
    print(f"Certificate saved to {output_path}")

if __name__ == "__main__":
    intern_name = input("Enter Intern's Name: ")
    intern_pos = input("Enter Intern's Position: ")
    date = input("Enter Completion Date (e.g., 3 August 2024): ")
    output_path = r"C:\Users\khush\OneDrive\Documents\PYTHON3\certificate.pdf"  # Full path where the certificate will be saved
    create_certificate(intern_name, intern_pos, date, output_path)
