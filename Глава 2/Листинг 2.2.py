import qrcode

# Данные для кодирования
data = "https://example.com"

# Генерация QR-кода
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

# Создание и сохранение изображения

img = qr.make_image(fill='blue', back_color='yellow')
img.save('img-color/qr_code-color.png')

