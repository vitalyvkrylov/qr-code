from PIL import Image, ImageDraw  # Импортируем необходимые модули для работы с изображениями.
from MyQR import myqr  # Импортируем библиотеку для генерации QR-кодов.
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

# Параметры изображения
image_width = 400  # Ширина изображения в пикселях.
image_height = 400  # Высота изображения в пикселях.
background_color = "white"  # Цвет фона изображения.
star_color = "black"  # Цвет звезды.
star_radius = 100  # Радиус звезды.

# Создание изображения
image = Image.new("RGB", (image_width, image_height), background_color)  # Создаем новое изображение с заданными размерами и цветом фона.
draw = ImageDraw.Draw(image)  # Создаем объект для рисования на изображении.

# Рисование звезды
draw_star(draw, image_width // 2, image_height // 2, star_radius, star_color)  # Вызываем функцию для рисования звезды в центре изображения.

# Сохранение изображения
image.save("img/star_image.png")  # Сохраняем изображение звезды в указанной папке с заданным именем.

myqr.run(  # Запускаем функцию создания QR-кода с заданными параметрами
    words="http://ege-drive.ru",  # Ссылка, которая будет закодирована в QR-код
    version=20,  # Устанавливаем размер QR-кода (от 1 до 40), 20 – более крупный QR-код
    level="H",  # Уровень коррекции ошибок H (восстанавливает до 30% данных при повреждении)
    picture="img/star_image.png",  # Изображение, которое будет наложено на QR-код
    colorized=True,  # Цветной режим для QR-кода; если False, QR-код будет чёрно-белым
    save_name='qr/star_qr.png',  # Имя файла для сохранения результата
    contrast=3.0,  # Контрастность QR-кода и фона, где 1.0 — исходное значение
    brightness=10.0  # Яркость QR-кода и фона, где 1.0 — исходное значение
)