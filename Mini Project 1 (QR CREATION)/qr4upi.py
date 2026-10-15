import qrcode 

print("By sanskriti Saxena")

upiid = input("Enter UPI ID: ")
name = input("Enter Name: ")

upi_url = f"upi://pay?pa={upiid}&pn={name}"

qr = qrcode.make(upi_url)
qr.save(r"E:\prototype\Assignment6\upi_qrcode.png")
qr.show()
print("QR code generated successfully!")

print("saxenasanskriti")