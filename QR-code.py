import qrcode

# Данные для кодирования
data0 = "http://yandex.ru"
data1 = "http://ya.ru"
data2 = "http://rbc.ru"
data3 = "http://vc.ru"
data4 = "https://inf-ege.sdamgia.ru/"
data5 = "https://inf-oge.sdamgia.ru/"

name_qr_code0 = 'img/qr_0.png'
name_qr_code1 = 'img/qr_1.png'
name_qr_code2 = 'img/qr_2.png'
name_qr_code3 = 'img/qr_3.png'
name_qr_code4 = 'img/qr_4.png'
name_qr_code5 = 'img/qr_5.png'

# Генерация QR-кода
qr0 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr1 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr2 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr3 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr4 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr5= qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)


qr0.add_data(data0)
qr1.add_data(data1)
qr2.add_data(data2)
qr3.add_data(data3)
qr4.add_data(data4)
qr5.add_data(data5)

qr0.make(fit=True)
qr1.make(fit=True)
qr2.make(fit=True)
qr3.make(fit=True)
qr4.make(fit=True)
qr5.make(fit=True)

# Создание и сохранение изображения
img0 = qr0.make_image(fill='black', back_color='white')
img1 = qr1.make_image(fill='black', back_color='white')
img2 = qr2.make_image(fill='black', back_color='white')
img3 = qr3.make_image(fill='black', back_color='white')
img4 = qr4.make_image(fill='black', back_color='white')
img5 = qr5.make_image(fill='black', back_color='white')

img0.save(name_qr_code0)
img1.save(name_qr_code1)
img2.save(name_qr_code2)
img3.save(name_qr_code3)
img4.save(name_qr_code4)
img5.save(name_qr_code5)