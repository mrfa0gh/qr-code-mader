import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_qr_with_text(input_text, custom_text, output_file):
    # Step 1: Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,  # Further reduced border size
    )
    qr.add_data(input_text)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    qr_width, qr_height = qr_img.size

    # Step 2: Add custom text in the center of the QR Code
    draw = ImageDraw.Draw(qr_img)

    try:
        font = ImageFont.truetype("arial.ttf", 20)  # You can adjust the font and size
    except:
        font = ImageFont.load_default()  # Fallback if the font is not found

    text_width, text_height = draw.textbbox((0, 0), custom_text, font=font)[2:]
    text_x = (qr_width - text_width) // 2
    text_y = (qr_height - text_height) // 2

    draw.rectangle(
        [(text_x - 2, text_y - 2), (text_x + text_width + 2, text_y + text_height + 2)],
        fill="white"
    )  # Add a smaller white background for the text
    draw.text((text_x, text_y), custom_text, fill="black", font=font)  # Add the custom text

    # Step 3: Save the resulting QR Code
    qr_img.save(output_file)
    print(f"QR Code saved as {output_file}")

# Input from user
input_text = input("Enter the text for the QR code: ")
custom_text = input("Enter the custom text to display in the center of the QR code: ")
output_file = "custom_qr_code.png"

generate_qr_with_text(input_text, custom_text, output_file)
