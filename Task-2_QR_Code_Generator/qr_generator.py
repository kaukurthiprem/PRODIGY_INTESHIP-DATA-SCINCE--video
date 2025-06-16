import qrcode

data = input("Enter text or URL: ")
img = qrcode.make(data)
img.save("qr_code.png")
print("QR Code saved as 'qr_code.png'")