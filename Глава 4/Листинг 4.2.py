from PIL import Image, ImageDraw  # Импортируем необходимые модули для работы с изображениями.
from MyQR import myqr  # Импортируем библиотеку для генерации QR-кодов.
import math  # Импортируем библиотеку для математических функций.

# Функция для рисования сердца
def draw_heart(draw, x_center, y_center, size, color):
    points = []  # Инициализируем список для хранения координат точек сердца

    # Цикл для создания точек по контуру сердца
    for angle in range(360):  # Угол меняется от 0 до 359 градусов для создания замкнутого контура
        theta = math.radians(angle)  # Преобразуем угол из градусов в радианы

        # Вычисляем координаты точки на контуре сердца
        x = x_center + size * 16 * math.sin(theta) ** 3
        y = y_center - size * (13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - math.cos(4 * theta))
        points.append((x, y))  # Добавляем точку в список координат

    # Рисуем контур сердца
    draw.polygon(points, fill=color)

# Основная часть программы
# Создаем изображение размером 400x400 с белым фоном
image_size = (400, 400)
image = Image.new("RGB", image_size, "white")
draw = ImageDraw.Draw(image)

# Задаем центр и размер сердца
x_center, y_center = 200, 200
size = 10
color = "red"

# Вызываем функцию для рисования сердца
draw_heart(draw, x_center, y_center, size, color)

# Сохраняем и показываем изображение
image.save("img/heart.png")

myqr.run(  # Запускаем генерацию QR-кода.
    words="http://ege-drive.ru",  # URL, который будет закодирован в QR-коде.
    version=20,  # Указываем версию QR-кода (размер).
    level="H",  # Уровень коррекции ошибок (высокий).
    picture="img/heart.png",  # Изображение звезды, добавляемое в QR-код.
    colorized=True,  # Если True, QR-код будет цветным.
    save_name='qr/heart_qr.png',  # Имя файла для сохранения QR-кода.
    contrast=3.0,  # Уровень контрастности QR-кода.
    brightness=10.0  # Яркость QR-кода.
)
