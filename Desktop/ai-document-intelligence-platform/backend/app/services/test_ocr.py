import pytesseract
from PIL import Image

image = Image.open("uploads/02 cef_page-0001.jpg")

text = pytesseract.image_to_string(image)

print(text[:2000])
