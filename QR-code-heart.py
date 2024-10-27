from MyQR import myqr
from PIL import Image, ImageDraw


def create_star_shape(size):
    """Создает маску в форме звезды."""
    star = Image.new('L', (size, size), 0)  # 'L' - режим оттенков серого
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

    draw.polygon(points, fill=1)  # Рисуем звезду

    return star


def create_qr_code(data, shape_size):
    """Создает QR-код и накладывает маску в форме звезды."""
    # Генерация QR-кода с помощью MyQR
    myqr.run(
        words=data,
        version=1,
        level='H',
        save_name='temp_qr.png'
    )

    # Открываем сгенерированный QR-код
    qr_image = Image.open('temp_qr.png')

    # Создаем маску в форме звезды
    star_shape = create_star_shape(shape_size)

    # Создаем новое изображение с белым фоном
    qr_with_star = Image.new('L', (shape_size, shape_size), 255)
    qr_image = qr_image.resize((shape_size, shape_size))  # Изменяем размер QR-кода
    qr_with_star.paste(qr_image, (0, 0), star_shape)  # Накладываем QR-код на звезду

    return qr_with_star


# Пример использования
data = 'https://example.com'
shape_size = 400  # Размер маски звезды в пикселях
qr_star_image = create_qr_code(data, shape_size)

# Сохраняем изображение
qr_star_image.save('qr_star.png')
qr_star_image.show()  # Показываем изображение