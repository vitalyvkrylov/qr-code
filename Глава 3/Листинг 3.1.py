from MyQR import myqr  # Импортируем модуль myqr из библиотеки MyQR для создания QR-кодов

# Генерация QR-кода с настройками
myqr.run(  # Запускаем функцию создания QR-кода с заданными параметрами
    words="http://ege-drive.ru",  # Ссылка, которая будет закодирована в QR-код
    version=20,  # Устанавливаем размер QR-кода (от 1 до 40), 20 – более крупный QR-код
    level="H",  # Уровень коррекции ошибок H (восстанавливает до 30% данных при повреждении)
    picture="img-from-foto/samurai.png",  # Изображение, которое будет наложено на QR-код
    colorized=True,  # Цветной режим для QR-кода; если False, QR-код будет чёрно-белым
    save_name='qr-from-foto/qr-from-foto.png',  # Имя файла для сохранения результата
    contrast=3.0,  # Контрастность QR-кода и фона, где 1.0 — исходное значение
    brightness=10.0  # Яркость QR-кода и фона, где 1.0 — исходное значение
)