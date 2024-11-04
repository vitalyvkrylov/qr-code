# Импортируем необходимые библиотеки
from PIL import Image, ImageDraw, ImageOps  # Импортируем классы для работы с изображениями и рисованием
from amzqr import amzqr  # Импортируем модуль для генерации QR-кодов

# Ссылка для QR-кода
url = "https://ege-drive.ru"  # URL, который будет закодирован в QR-коде

# Параметры QR-кода
qr_size = 300  # Размер QR-кода (ширина и высота в пикселях)
face_color = (255, 255, 0, 100)  # Цвет лица смайлика (полупрозрачный желтый, RGBA)
eye_color = (0, 0, 0)  # Цвет глаз смайлика (черный, RGB)

# Генерируем QR-код
qr_save_path = "../Глава 5/qr/qr_code_tmp.png"  # Путь для сохранения сгенерированного QR-кода
amzqr.run(
    words=url,  # Передаем URL для генерации QR-кода
    version=1,  # Устанавливаем версию QR-кода (1 - минимальная версия)
    level='H',  # Устанавливаем уровень коррекции ошибок (H - высокий)
    colorized=False,  # Указываем, что QR-код будет черно-белым
    save_name=qr_save_path  # Указываем имя файла для сохранения QR-кода
)

# Открываем и изменяем QR-код
qr_code_image = Image.open(qr_save_path).resize((qr_size, qr_size))  # Открываем сгенерированный QR-код и изменяем его размер до заданного

# Создаем маску для QR-кода
mask = Image.new("L", (qr_size, qr_size), 0)  # Создаем черную маску (L - режим оттенков серого)
draw_mask = ImageDraw.Draw(mask)  # Создаем объект для рисования на маске
draw_mask.ellipse([(0, 0), (qr_size, qr_size)], fill=255)  # Рисуем белый круг в маске для обрезки QR-кода

# Применяем маску к QR-коду, чтобы сделать его круглым
rounded_qr = Image.new("RGBA", (qr_size, qr_size), (255, 255, 255, 0))  # Создаем новое изображение с прозрачным фоном для обрезанного QR-кода
rounded_qr.paste(qr_code_image, (0, 0), mask)  # Обрезаем QR-код по маске, добавляя его в новое изображение

# Создаем изображение для смайлика
smiley_image = Image.new("RGBA", (qr_size, qr_size), (255, 255, 255, 0))  # Создаем новое изображение смайлика с прозрачным фоном
draw = ImageDraw.Draw(smiley_image)  # Создаем объект для рисования на изображении смайлика

# Рисуем лицо смайлика
face_radius = 150  # Радиус смайлика
face_center = (qr_size // 2, qr_size // 2)  # Вычисляем центр смайлика
draw.ellipse([  # Рисуем круг для лица смайлика
    (face_center[0] - face_radius, face_center[1] - face_radius),  # Верхний левый угол
    (face_center[0] + face_radius, face_center[1] + face_radius)   # Нижний правый угол
], fill=face_color)  # Задаем цвет лица смайлика

# Рисуем глаза
eye_radius = 10  # Радиус глаз
eye_y_offset = 30  # Смещение глаз по оси Y от центра
eye_x_offset = 25  # Смещение глаз по оси X от центра
left_eye_center = (face_center[0] - eye_x_offset, face_center[1] - eye_y_offset)  # Центр левого глаза
right_eye_center = (face_center[0] + eye_x_offset, face_center[1] - eye_y_offset)  # Центр правого глаза

draw.ellipse([  # Рисуем левый глаз
    (left_eye_center[0] - eye_radius, left_eye_center[1] - eye_radius),  # Верхний левый угол глаза
    (left_eye_center[0] + eye_radius, left_eye_center[1] + eye_radius)   # Нижний правый угол глаза
], fill=eye_color)  # Задаем цвет левого глаза
draw.ellipse([  # Рисуем правый глаз
    (right_eye_center[0] - eye_radius, right_eye_center[1] - eye_radius),  # Верхний левый угол глаза
    (right_eye_center[0] + eye_radius, right_eye_center[1] + eye_radius)   # Нижний правый угол глаза
], fill=eye_color)  # Задаем цвет правого глаза

# Рисуем улыбку
mouth_width = 50  # Ширина улыбки
mouth_height = 25  # Высота улыбки
mouth_center = (face_center[0], face_center[1] + 15)  # Центр улыбки (немного ниже центра лица)
draw.arc([  # Рисуем улыбку в виде дуги
    (mouth_center[0] - mouth_width, mouth_center[1] - mouth_height),  # Верхний левый угол дуги
    (mouth_center[0] + mouth_width, mouth_center[1] + mouth_height)   # Нижний правый угол дуги
], start=0, end=180, fill=eye_color, width=3)  # Устанавливаем цвет и ширину линии улыбки

# Применяем прозрачность к смайлику
smiley_image.putalpha(100)  # Устанавливаем прозрачность смайлика (0 - полностью прозрачный, 255 - полностью непрозрачный)
smiley_image.save("img/smile.png")  # Сохраняем итоговое изображение в файл

# Создаем новое изображение для объединения
combined_image = Image.new("RGBA", (qr_size, qr_size), (255, 255, 255, 0))  # Создаем новое изображение с прозрачным фоном для объединенного изображения
combined_image.paste(rounded_qr, (0, 0))  # Накладываем круглый QR-код на новое изображение
combined_image.paste(smiley_image, (0, 0), smiley_image)  # Накладываем смайлик на QR-код, сохраняя прозрачность

# Сохраняем и отображаем изображение
combined_image.save("qr/qr_smile_with_bg.png")  # Сохраняем итоговое изображение в файл