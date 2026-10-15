import qrcode 

print("By sanskriti Saxena")

upiid = input("Enter UPI ID: ")
name = input("Enter Name: ")
amount = input("Enter Amount: ")

upi_url = f"upi://pay?pa={upiid}&pn={name}&am={amount}"

#pa payee 
#pn payee name
#cu currency
#am amount

qr = qrcode.make(upi_url)
qr.save(r"E:\prototype\Assignment6\upi_qrcode2.png")
qr.show()
print("QR code generated successfully!")

print("saxenasanskriti")