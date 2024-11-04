from amzqr import amzqr

# Данные для кодирования
data_save = "img/heart.pngg"  # Ссылка или текст, который будет закодирован в QR-код
data_qr = "qr/heart_qr.png"
url = "https://ege-drive.ru"

# Настройка QR-кода
amzqr.run(
    words=url,  # Данные для кодирования
    version=1,  # Версия QR-кода (1-40), 1 - минимальный размер
    level='H',  # Уровень коррекции ошибок ('L', 'M', 'Q', 'H')
    picture=data_save,  # Фоновое изображение в форме сердца
    colorized=True,  # Разрешить цветные QR-коды
    contrast=1.0,  # Контрастность фона
    brightness=1.0,  # Яркость QR-кода
    save_name=data_qr,  # Имя файла для сохранения
    save_dir="."  # Путь к папке сохранения
)