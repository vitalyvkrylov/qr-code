import qrcode
from PIL import Image

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://ege-drive.ru")  # URL or data for the QR code
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Open the logo image
logo = Image.open('logo/logo.png')

# Resize the logo
box = (img.size[0] // 4, img.size[1] // 4)
logo = logo.resize(box)

# Calculate the position to place the logo at the center
pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

# Paste the logo onto the QR code
img.paste(logo, pos, logo.convert("RGBA"))  # Ensure transparency is handled

# Save the image with the logo
img.save('qr_with_logo.png')