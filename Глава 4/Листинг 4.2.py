from PIL import Image, ImageDraw  # Импортируем модули для работы с изображениями и инструментами рисования.
from amzqr import amzqr  # Импортируем библиотеку для создания QR-кодов с фоновыми изображениями.
import math  # Импортируем модуль для выполнения математических расчетов, включая тригонометрические функции.

# Функция для рисования сердца
def draw_heart(draw, x_center, y_center, size, color):
    points = []  # Инициализируем список для хранения координат, образующих контур сердца.
    # Цикл для создания точек по контуру сердца
    for angle in range(360):  # Проходим по углам от 0 до 359 градусов для полного контура.
        theta = math.radians(angle)  # Преобразуем угол из градусов в радианы для расчетов.
        # Вычисляем координаты точки на контуре сердца с использованием параметрических уравнений.
        x = x_center + size * 16 * math.sin(theta) ** 3
        y = y_center - size * (
                13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - math.cos(4 * theta))
        points.append((x, y))  # Добавляем координаты точки в список для формирования контура.
    # Рисуем контур сердца на изображении
    draw.polygon(points, fill=color)  # Соединяем точки, заполняя получившуюся фигуру цветом `color`.

# Пути для сохранения изображений
data_save = "img/heart.png"  # Путь для сохранения изображения сердца.
data_qr = "qr/heart_qr.png"  # Путь для сохранения QR-кода.
url = "https://ege-drive.ru"  # URL, который будет закодирован в QR-код.

# Параметры изображения
image_width = 400  # Ширина создаваемого изображения в пикселях.
image_height = 400  # Высота создаваемого изображения в пикселях.
background_color = "white"  # Цвет фона изображения.
heart_color = "red"  # Цвет фигуры сердца.
heart_size = 10  # Размерность для масштабирования фигуры сердца.
mode = "RGB"  # Цветовой режим изображения.

# Задаем координаты центра сердца
x_center, y_center = 200, 200  # Центр фигуры сердца по осям X и Y.

# Основная часть программы
# Создаем пустое изображение размером 400x400 с белым фоном
image_size = (image_width, image_height)  # Задаем размеры изображения.
image = Image.new(mode, image_size, background_color)  # Создаем изображение с заданными параметрами.
draw = ImageDraw.Draw(image)  # Инициализируем объект для рисования на изображении.

# Рисуем сердце на изображении
draw_heart(draw, x_center, y_center, heart_size, heart_color)  # Вызываем функцию для рисования сердца.

# Сохраняем изображение сердца
image.save(data_save)  # Сохраняем изображение с сердцем в указанный путь.

# Данные для кодирования в QR-код
data = url  # URL, который будет встроен в QR-код.

# Генерация QR-кода с наложением изображения сердца
amzqr.run(
    words=data,  # Данные для QR-кода.
    version=1,  # Версия QR-кода; 1 — минимальный размер (макс. 40).
    level='H',  # Уровень коррекции ошибок ('L', 'M', 'Q', 'H') — выбран высокий.
    picture=data_save,  # Путь к изображению сердца, используемому в качестве фона для QR-кода.
    colorized=True,  # Включаем цветное отображение QR-кода.
    contrast=1.0,  # Устанавливаем контраст изображения.
    brightness=1.0,  # Устанавливаем яркость изображения.
    save_name=data_qr,  # Имя файла для сохранения QR-кода с изображением.
    save_dir="."  # Директория для сохранения QR-кода.
)