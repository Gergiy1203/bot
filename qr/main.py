import segno


qrcode = segno.make_qr("92ckqY")
qrcode = segno.make_qr("Gs 1 Data Matrix,")
qrcode.save("metanit_qr.svg")
qrcode.show()
