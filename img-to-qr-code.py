from PIL import Image
import qrcode

# Открываем изображение
img_path = 'img.png'
image = Image.open(img_path)

# Преобразуем изображение в чёрно-белое
image = image.convert('L')

# Уменьшаем изображение до 50x50 пикселей (размер можно варьировать)
image = image.resize((50, 50))

# Превращаем изображение в QR-код
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Высокий уровень коррекции для возможности встраивания изображения
)
qr.add_data(image.tobytes())
qr.make(fit=True)

# Сохраняем результат
img = qr.make_image(fill='black', back_color='white')
img.save('qr_from_image.png')
