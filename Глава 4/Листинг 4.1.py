from PIL import Image, ImageDraw  # Импортируем необходимые модули для работы с изображениями.
from amzqr import amzqr
import math  # Импортируем библиотеку для математических функций.


def draw_star(draw, x_center, y_center, radius, color):  # Определяем функцию для рисования звезды.
    points = []  # Инициализируем список для хранения координат вершин звезды.
    for i in range(5):  # Цикл для создания 5 вершин звезды.
        # Вычисляем угол для внешней точки звезды
        outer_angle = 2 * math.pi * (i * 2) / 5 - math.pi / 2
        # Вычисляем угол для внутренней точки звезды
        inner_angle = 2 * math.pi * ((i * 2 + 1) / 5) - math.pi / 2

        # Внешняя точка звезды
        x_outer = x_center + radius * math.cos(outer_angle)  # Вычисляем координату X внешней точки.
        y_outer = y_center + radius * math.sin(outer_angle)  # Вычисляем координату Y внешней точки.
        points.append((x_outer, y_outer))  # Добавляем внешнюю точку в список координат.

        # Внутренняя точка звезды
        x_inner = x_center + (radius / 2) * math.cos(inner_angle)  # Вычисляем координату X внутренней точки.
        y_inner = y_center + (radius / 2) * math.sin(inner_angle)  # Вычисляем координату Y внутренней точки.
        points.append((x_inner, y_inner))  # Добавляем внутреннюю точку в список координат.

    draw.polygon(points, fill=color)  # Рисуем многоугольник (звезду) с заданным цветом.

data_save = "img/star_image.png"
data_qr = "qr/star_qr.png"
url = "https://ege-drive.ru"

# Параметры изображения
image_width = 400  # Ширина изображения в пикселях.
image_height = 400  # Высота изображения в пикселях.
background_color = "white"  # Цвет фона изображения.
star_color = "black"  # Цвет звезды.
star_radius = 100  # Радиус звезды.

# Создание изображения
image = Image.new("RGB", (image_width, image_height),
                  background_color)  # Создаем новое изображение с заданными размерами и цветом фона.
draw = ImageDraw.Draw(image)  # Создаем объект для рисования на изображении.

# Рисование звезды
draw_star(draw, image_width // 2, image_height // 2, star_radius,
          star_color)  # Вызываем функцию для рисования звезды в центре изображения.

# Сохранение изображения
image.save(data_save)  # Сохраняем изображение звезды в указанной папке с заданным именем.

from amzqr import amzqr

# Данные для кодирования
data = url  # Ссылка или текст, который будет закодирован в QR-код

# Настройка QR-кода
amzqr.run(
    words=data,  # Данные для кодирования
    version=1,  # Версия QR-кода (1-40), 1 - минимальный размер
    level='H',  # Уровень коррекции ошибок ('L', 'M', 'Q', 'H')
    picture=data_save,  # Фоновое изображение в форме сердца
    colorized=True,  # Разрешить цветные QR-коды
    contrast=1.0,  # Контрастность фона
    brightness=1.0,  # Яркость QR-кода
    save_name=data_qr,  # Имя файла для сохранения
    save_dir="."  # Путь к папке сохранения
)
