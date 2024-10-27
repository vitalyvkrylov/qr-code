from PIL import Image

# Открываем сгенерированный QR-код
img = qr.make_image(fill='black', back_color='white')
img = img.convert("RGB")

# Открываем изображение логотипа
logo = Image.open('logo.png')

# Изменяем размер логотипа под QR-код
box = (img.size[0] // 4, img.size[1] // 4)
logo = logo.resize(box)

# Вставляем логотип в центр QR-кода
pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)

# Сохраняем QR-код с логотипом
img.save('qr_with_logo.png')
