import cv2
d = cv2.QRCodeDetector()
val,points,straight_qrcode = d.detectAndDecode(cv2.imread("data.png"))   # data is the file containing QR Code
print(val)

#val  is  grayscale or color (BGR) image """containing QR code""".
#points is	optional output array of vertices of the found QR code quadrangle. Will be empty if not found.
#straight_qrcode is  The optional output image containing rectified and binarized QR code


#https://docs.opencv.org/4.5.2/de/dc3/classcv_1_1QRCodeDetector.html#a4172c2eb4825c844fb1b0ae67202d329
#refer the above link for qr code detector full refernce