import qrcode  # Импортируем библиотеку для генерации QR-кодов

# Данные для кодирования
data = "https://example.com"  # URL, который будет закодирован в QR-код

# Генерация QR-кода
qr = qrcode.QRCode(  # Создаём объект QR-кода с заданными параметрами
    version=1,  # Размер QR-кода (1 означает 21x21 модулей)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Уровень коррекции ошибок L (7% данных восстанавливается при повреждении)
    box_size=10,  # Размер одного квадратика (модуля) в QR-коде
    border=4  # Толщина границы QR-кода в модулях
)

qr.add_data(data)  # Добавляем данные (URL) в QR-код
qr.make(fit=True)  # Оптимизируем размер QR-кода для данных

# Создание и сохранение изображения
img = qr.make_image(fill='blue', back_color='yellow')  # Создаём изображение QR-кода с синим цветом и жёлтым фоном
img.save('img-color/qr_code-color.png')  # Сохраняем изображение в папке 'img-color' с названием 'qr_code-color.png'
