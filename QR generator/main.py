import qrcode

img = qrcode.QRCode(box_size=20, border=2)
usr_input = input("Text / Link to generate QR code: ")
img.add_data(usr_input)
usr_input = input("FileName: ")

img.make(fit=True)
qrc = img.make_image(fill_color="orange", back_color="black")

qrc.save(usr_input + ".png")

