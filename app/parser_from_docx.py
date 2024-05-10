import docx
from docx import Document

document = Document()
document.add_paragraph("It was a dark and stormy night.")
docx.text.paragraph.Paragraph object at 0x10f19e760>
document.save("dark-and-stormy.docx")

document = Document("dark-and-stormy.docx")
document.paragraphs[0].text