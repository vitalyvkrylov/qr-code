from PIL import Image, ImageDraw
from MyQR import myqr

def create_star_shape(size):
    """Создает изображение звезды заданного размера."""
    # Создаем новое изображение с белым фоном
    star = Image.new('RGB', (size, size), (255, 255, 255))  # 'RGB' для цветного изображения
    draw = ImageDraw.Draw(star)

    # Координаты для рисования звезды
    points = [
        (size // 2, 0),  # верхняя точка
        (size * 3 // 4, size * 3 // 4),  # правая нижняя
        (size, size * 3 // 4),  # правая
        (size * 5 // 8, size),  # нижняя правая
        (size // 2, size * 5 // 8),  # нижняя
        (size * 3 // 8, size),  # нижняя левая
        (0, size * 3 // 4),  # левая
        (size // 4, size * 3 // 4)  # левая нижняя
    ]

    draw.polygon(points, fill=(255, 215, 0))  # Рисуем звезду золотистым цветом

    return star


# Пример использования
size = 400  # Размер звезды в пикселях
star_image = create_star_shape(size)

# Сохраняем изображение
star_image.save('star_image.png')

myqr.run(
    words="http://ege-drive.ru",
    version=20, level="H",
    picture="star_image.png",
    colorized=True,
    save_name='star_qr.png',
    contrast=3.0,
    brightness=10.0)