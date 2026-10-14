import pytesseract

from PIL import Image

print("By sanskriti Saxena")
img = Image.open(r"E:\prototype\Assignment7\output.png")
text = pytesseract.image_to_string(img) 

print("Extracted text from image:", text)

print("saxenasanskriti")