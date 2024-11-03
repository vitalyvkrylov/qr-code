import qrcode  # Импортируем библиотеку для генерации QR-кодов

# Данные для кодирования
data0 = "http://yandex.ru"  # URL для кодирования в первый QR-код

# Пути и имена файлов для сохранения каждого QR-кода
name_qr_code0 = 'img/qr.png'  # Путь и имя файла для сохранения первого QR-кода

# Генерация QR-кодов
qr0 = qrcode.QRCode(  # Создаём объект QR-кода для первого URL с параметрами:
    version=1,  # Размер QR-кода, 1 означает 21x21 модулей
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Уровень коррекции ошибок L (восстанавливает до 7% данных)
    box_size=10,  # Размер одного модуля в QR-коде
    border=4  # Толщина границы вокруг QR-кода в модулях
)

# Аналогичным образом создаём объекты QR-кодов для остальных данных
qr1 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

# Добавление данных (URL) в каждый QR-код
qr0.add_data(data0)  # Добавляем URL data0 в первый QR-код

# Оптимизация размера QR-кодов
qr0.make(fit=True)  # Оптимизируем размер для первого QR-кода

# Создание и сохранение изображений QR-кодов
img0 = qr0.make_image(fill='black', back_color='white')  # Создаём изображение первого QR-кода (чёрный на белом фоне)

# Сохранение изображений в указанные файлы
img0.save(name_qr_code0)  # Сохраняем первый QR-код в файл img-with-logo/qr_0.png