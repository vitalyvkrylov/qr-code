from MyQR import myqr

myqr.run(
    words="http://ege-drive.ru",
    version=20, level="H",
    picture="qr-from-foto/img_1.png",
    colorized=True,
    save_name='img-with-logo-from-qr-from-foto/samurai.png',
    contrast=3.0,
    brightness=10.0)
# Dynamic pictures should use gif format pictures
# words parameter is to specify the content of the QR code
# version parameter is the control side length, it is an int type, the range is 1-40, the larger the number, the larger the side length
# level is the error correction level, the range is L, M, Q, H, increasing from left to right
# picture parameter is to specify the name of the picture file to be used, the picture here is in the directory that this python file belongs to
# colorized parameter is to specify that the generated QR code image is colored, if it is False or not set, the generated image is black and white
# The contrast parameter is to set the contrast of the picture
# The brightness parameter is to adjust the brightness of the picture
