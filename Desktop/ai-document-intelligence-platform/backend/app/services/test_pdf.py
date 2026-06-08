from app.services.pdf_service import extract_text_from_pdf

text = extract_text_from_pdf(
    "uploads/your_file.pdf"
)

print(text[:1000])
