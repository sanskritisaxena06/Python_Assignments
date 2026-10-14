from PIL import Image, ImageDraw, ImageFont
print("By sanskriti Saxena")

text = input("Enter the text to convert to image: ")

image = Image.new("RGB", (500, 300), "white")
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()

draw.text((100, 120), text, fill="black", font=font)

image.save(r"E:\prototype\Assignment8\output.png")
print("Image saved as output.png")
image.show()



print("saxenasanskriti")