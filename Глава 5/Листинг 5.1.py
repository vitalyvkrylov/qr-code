import math
from PIL import Image, ImageDraw
import qrcode

def draw_heart(draw, x_center, y_center, size, color):
    points = []  # Список для хранения координат сердца
    # Цикл для создания точек по контуру сердца
    for angle in range(360):  # Проходим по углам от 0 до 359 градусов для полного контура
        theta = math.radians(angle)  # Преобразуем угол из градусов в радианы
        # Вычисляем координаты точки на контуре сердца
        x = x_center + size * 16 * math.sin(theta) ** 3
        y = y_center - size * (13 * math.cos(theta) - 5 * math.cos(2 * theta) -
                                2 * math.cos(3 * theta) - math.cos(4 * theta))
        points.append((x, y))  # Добавляем координаты точки в список

    # Рисуем контур сердца на изображении
    draw.polygon(points, fill=color)  # Соединяем точки, заполняя фигуру цветом `color`

def add_qr_code(image, data, position, size):
    # Генерация QR-кода
    qr = qrcode.QRCode(version=1, box_size=10, border=5)  # Создание QR-кода
    qr.add_data(data)  # Добавление данных в QR-код
    qr.make(fit=True)  # Подгонка QR-кода под размер

    # Создание изображения QR-кода с красным фоном
    qr_image = qr.make_image(fill_color="white", back_color="red")  # Фон QR-кода изменен на красный
    qr_image = qr_image.resize(size)  # Изменение размера QR-кода

    # Обрезаем QR-код по размеру сердца
    qr_width, qr_height = qr_image.size
    heart_width = size[0]  # Ширина области сердца
    heart_height = size[1]  # Высота области сердца
    qr_image_cropped = qr_image.crop((0, 0, heart_width, heart_height))  # Обрезаем QR-код

    # Определение позиции для QR-кода
    x, y = position
    image.paste(qr_image_cropped, (x, y))  # Наложение QR-кода на изображение

# Параметры изображения
width, height = 400, 400  # Ширина и высота изображения
background_color = (255, 255, 255)  # Цвет фона (белый)

# Создаем новое изображение
image = Image.new("RGB", (width, height), background_color)  # Создаем новое изображение с белым фоном
draw = ImageDraw.Draw(image)  # Создаем объект для рисования на изображении

# Параметры сердца
heart_color = (255, 0, 0)  # Цвет сердца (красный)
x_center = width // 2  # Центр по оси X
y_center = height // 2  # Центр по оси Y
size = 100  # Размер сердца (размер области QR-кода)

# Рисуем сердце
draw_heart(draw, x_center, y_center, size / 10, heart_color)  # Рисуем сердце, уменьшая его размер для корректного отображения

# Добавляем QR-код
qr_data = "https://ege-drive.ru"  # Данные для QR-кода (замените на ваши данные)
qr_position = (width // 4 + 120, height // 4 + 15)  # Позиция QR-кода
qr_size = (size + 10, size + 10)  # Размер QR-кода равен размеру сердца

add_qr_code(image, qr_data, qr_position, qr_size)  # Добавляем QR-код на изображение

# Сохраняем изображение
image.save("qr/heart_with_qr.png")  # Сохраняем изображение в файл
