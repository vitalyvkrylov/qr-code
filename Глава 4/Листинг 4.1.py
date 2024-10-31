from PIL import Image, ImageDraw
from MyQR import myqr
import math

def draw_star(draw, x_center, y_center, radius, color):
    points = []
    for i in range(5):
        outer_angle = 2 * math.pi * (i * 2) / 5 - math.pi / 2
        inner_angle = 2 * math.pi * ((i * 2 + 1) / 5) - math.pi / 2

        # Внешняя точка звезды
        x_outer = x_center + radius * math.cos(outer_angle)
        y_outer = y_center + radius * math.sin(outer_angle)
        points.append((x_outer, y_outer))

        # Внутренняя точка звезды
        x_inner = x_center + (radius / 2) * math.cos(inner_angle)
        y_inner = y_center + (radius / 2) * math.sin(inner_angle)
        points.append((x_inner, y_inner))

    draw.polygon(points, fill=color)

# Параметры изображения
image_width = 400
image_height = 400
background_color = "white"
star_color = "black"
star_radius = 100

# Создание изображения
image = Image.new("RGB", (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)

# Рисование звезды
draw_star(draw, image_width // 2, image_height // 2, star_radius, star_color)

# Сохранение изображения
image.save("img/star_image.png")

myqr.run(
    words="http://ege-drive.ru",
    version=20, level="H",
    picture="img/star_image.png",
    colorized=True,
    save_name='qr/star_qr.png',
    contrast=3.0,
    brightness=10.0)