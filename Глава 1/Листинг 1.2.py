import qrcode  # Импортируем библиотеку для генерации QR-кодов

# Данные для кодирования
data0 = "http://yandex.ru"  # URL для кодирования в первый QR-код
data1 = "http://ya.ru"  # URL для кодирования во второй QR-код
data2 = "http://rbc.ru"  # URL для кодирования в третий QR-код
data3 = "http://vc.ru"  # URL для кодирования в четвертый QR-код
data4 = "https://inf-ege.sdamgia.ru/"  # URL для кодирования в пятый QR-код
data5 = "https://inf-oge.sdamgia.ru/"  # URL для кодирования в шестой QR-код

# Пути и имена файлов для сохранения каждого QR-кода
name_qr_code0 = 'img/qr_0.png'  # Путь и имя файла для сохранения первого QR-кода
name_qr_code1 = 'img/qr_1.png'  # Путь и имя файла для сохранения второго QR-кода
name_qr_code2 = 'img/qr_2.png'  # Путь и имя файла для сохранения третьего QR-кода
name_qr_code3 = 'img/qr_3.png'  # Путь и имя файла для сохранения четвертого QR-кода
name_qr_code4 = 'img/qr_4.png'  # Путь и имя файла для сохранения пятого QR-кода
name_qr_code5 = 'img/qr_5.png'  # Путь и имя файла для сохранения шестого QR-кода

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
qr2 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr3 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr4 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr5 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

# Добавление данных (URL) в каждый QR-код
qr0.add_data(data0)  # Добавляем URL data0 в первый QR-код
qr1.add_data(data1)  # Добавляем URL data1 во второй QR-код
qr2.add_data(data2)  # Добавляем URL data2 в третий QR-код
qr3.add_data(data3)  # Добавляем URL data3 в четвертый QR-код
qr4.add_data(data4)  # Добавляем URL data4 в пятый QR-код
qr5.add_data(data5)  # Добавляем URL data5 в шестой QR-код

# Оптимизация размера QR-кодов
qr0.make(fit=True)  # Оптимизируем размер для первого QR-кода
qr1.make(fit=True)  # Оптимизируем размер для второго QR-кода
qr2.make(fit=True)  # Оптимизируем размер для третьего QR-кода
qr3.make(fit=True)  # Оптимизируем размер для четвертого QR-кода
qr4.make(fit=True)  # Оптимизируем размер для пятого QR-кода
qr5.make(fit=True)  # Оптимизируем размер для шестого QR-кода

# Создание и сохранение изображений QR-кодов
img0 = qr0.make_image(fill='black', back_color='white')  # Создаём изображение первого QR-кода (чёрный на белом фоне)
img1 = qr1.make_image(fill='black', back_color='white')  # Создаём изображение второго QR-кода
img2 = qr2.make_image(fill='black', back_color='white')  # Создаём изображение третьего QR-кода
img3 = qr3.make_image(fill='black', back_color='white')  # Создаём изображение четвёртого QR-кода
img4 = qr4.make_image(fill='black', back_color='white')  # Создаём изображение пятого QR-кода
img5 = qr5.make_image(fill='black', back_color='white')  # Создаём изображение шестого QR-кода

# Сохранение изображений в указанные файлы
img0.save(name_qr_code0)  # Сохраняем первый QR-код в файл img/qr_0.png
img1.save(name_qr_code1)  # Сохраняем второй QR-код в файл img/qr_1.png
img2.save(name_qr_code2)  # Сохраняем третий QR-код в файл img/qr_2.png
img3.save(name_qr_code3)  # Сохраняем четвертый QR-код в файл img/qr_3.png
img4.save(name_qr_code4)  # Сохраняем пятый QR-код в файл img/qr_4.png
img5.save(name_qr_code5)  # Сохраняем шестой QR-код в файл img/qr_5.png
