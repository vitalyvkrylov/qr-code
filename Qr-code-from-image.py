import qrcode
from PIL import Image
import base64

# 1. Чтение изображения и преобразование в байты
image_path = 'img.png'
with open(image_path, "rb") as image_file:
    # Преобразуем изображение в байтовую строку и закодируем в base64
    image_bytes = image_file.read()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

# 2. Генерация QR-кода из закодированных данных
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Высокий уровень коррекции ошибок
    box_size=10,
    border=4
)
qr.add_data(image_base64)
qr.make(fit=False)

# 3. Создание изображения QR-кода и сохранение
qr_image = qr.make_image(fill='black', back_color='white')
qr_image.save('qr_from_image_data.png')

print("QR-код с данными изображения успешно создан!")
