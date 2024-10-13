from PIL import Image
import qrcode

data = "https://example.com"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

# Открываем сгенерированный QR-код
img = qr.make_image(fill='white', back_color='white')
img = img.convert("RGB")

# Открываем изображение логотипа
logo = Image.open('logo/logo.png')

# Изменяем размер логотипа под QR-код
box = (img.size[0] // 8, img.size[1] // 8)
logo = logo.resize(box)

# Вставляем логотип в центр QR-кода
pos = (-(img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)

# Сохраняем QR-код с логотипом
img.save('img-with-logo/qr_with_logo.png')
