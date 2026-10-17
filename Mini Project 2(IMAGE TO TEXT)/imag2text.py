import pytesseract

from PIL import Image

print("By sanskriti Saxena")
img = Image.open("output.png")
text = pytesseract.image_to_string(img) 

print("Extracted text from image:", text)

print("saxenasanskriti")