#create a qr code
#Author : Shraddha Mane

#Before ruuning this code install the qrcode code pkg using "pip install qrcode".

#Sample Input : Hey,This is Shraddha Mane!

import qrcode

text=input("Enter any text to create a QR code : ")
qr=qrcode.make(text)

qr.save("qr.jpg")
print("QR code  generated successfully..!")

