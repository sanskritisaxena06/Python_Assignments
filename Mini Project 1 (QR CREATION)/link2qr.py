import qrcode

print("By sanskriti Saxena")

url = input("Enter URL: ")

if url.startswith("https://") or url.startswith("http://"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make()

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(r"E:\prototype\Assignment6\qrcode.png")
    img.show()

    print("QR code generated successfully!")
else:
    print("Invalid URL!")

print("saxenasanskriti")