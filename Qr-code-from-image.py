import qrcode
from PIL import Image
import base64

# 1. Чтение изображения и преобразование в байты
image_path = 'foto/img.png'  # Путь к вашему изображению
with open(image_path, "rb") as image_file:
    # Преобразуем изображение в байтовую строку и кодируем в base64
    image_bytes = image_file.read()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

# 2. Генерация QR-кода из закодированных данных
qr = qrcode.QRCode(
    version=1,  # Версия определяет размер QR-кода
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Высокий уровень коррекции ошибок
    box_size=10,  # Размер ячеек QR-кода
    border=4  # Граница вокруг QR-кода
)
qr.add_data(image_base64)
qr.make(fit=True)

# 3. Создание изображения QR-кода
qr_image = qr.make_image(fill='black', back_color='white')

# 4. Сохранение изображения QR-кода
output_path = 'qr_from_image.png'  # Укажите путь для сохранения QR-кода
qr_image.save(output_path)

print(f"QR-код с данными изображения успешно создан и сохранён как {output_path}!")
