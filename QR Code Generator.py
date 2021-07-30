import pyqrcode
from pyqrcode import QRCode

#string which represent the QR code
s = input("Enter the data you want to make QR Code of: ")

#Generate QR Code
url=pyqrcode.create(s)

# To save as browser html document
url.svg("data.svg",scale=8)

# To save the png file
url.png('data.png', scale = 6)

#print(url.terminal(quiet_zone=1))
