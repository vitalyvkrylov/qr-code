from PIL import Image, ImageDraw  # Импортируем необходимые модули для работы с изображениями.
from amzqr import amzqr  # Импортируем библиотеку для создания QR-кодов.
import math  # Импортируем библиотеку для выполнения математических расчетов.


# Функция для рисования сердца
def draw_heart(draw, x_center, y_center, size, color):
    points = []  # Инициализируем список для хранения координат точек сердца
    # Цикл для создания точек по контуру сердца
    for angle in range(360):  # Угол меняется от 0 до 359 градусов для создания замкнутого контура
        theta = math.radians(angle)  # Преобразуем угол из градусов в радианы
        # Вычисляем координаты точки на контуре сердца
        x = x_center + size * 16 * math.sin(theta) ** 3
        y = y_center - size * (
                13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - math.cos(4 * theta))
        points.append((x, y))  # Добавляем точку в список координат
    # Рисуем контур сердца
    draw.polygon(points, fill=color)


# Пути для сохранения изображения сердца и QR-кода
data_save = "img/heart.png"  # Ссылка или текст, который будет закодирован в QR-код
data_qr = "qr/heart_qr.png"
url = "https://ege-drive.ru"

# Параметры изображения
image_width = 400  # Ширина изображения в пикселях.
image_height = 400  # Высота изображения в пикселях.
background_color = "white"  # Цвет фона изображения.
heart_color = "red"  # Цвет звезды.
heart_size = 10
mode = "RGB"

# Задаем центр и размер сердца
x_center, y_center = 200, 200

# Основная часть программы
# Создаем изображение размером 400x400 с белым фоном
image_size = (image_width, image_height)
image = Image.new(mode, image_size, background_color)
draw = ImageDraw.Draw(image)

# Вызываем функцию для рисования сердца
draw_heart(draw, x_center, y_center, heart_size, heart_color)

# Сохранение изображения
image.save(data_save)  # Сохраняем изображение звезды по указанному пути.

# Данные для кодирования в QR-код
data = url  # URL или текст, который будет закодирован в QR-код.

# Настройка QR-кода
amzqr.run(
    words=data,  # Данные для кодирования.
    version=1,  # Версия QR-кода (1-40), 1 - минимальный размер.
    level='H',  # Уровень коррекции ошибок ('L', 'M', 'Q', 'H').
    picture=data_save,  # Фоновое изображение, в данном случае — звезда.
    colorized=True,  # Разрешить цветные QR-коды.
    contrast=1.0,  # Контрастность фона QR-кода.
    brightness=1.0,  # Яркость QR-кода.
    save_name=data_qr,  # Имя файла для сохранения QR-кода.
    save_dir="."  # Путь к папке для сохранения QR-кода.
)
