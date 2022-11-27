import qrcode

username = input("name: ")
phone_number = input("phone number: ")

QRcode = qrcode.make(username + " " + phone_number)
QRcode.save("MyFirstQRCode.png")