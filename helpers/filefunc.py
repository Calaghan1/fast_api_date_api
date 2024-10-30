from PIL import Image, ImageDraw, ImageFont

async def add_watermark(image: Image.Image, watermark_text: str = "Watermark") -> Image.Image:
    
    watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(watermark)

    # Настройки водяного знака
    font_size = int(image.width / 15)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Получение размеров текста с помощью textbbox
    bbox = draw.textbbox((1, 13), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    # Позиция для текста водяного знака
    position = (image.width - text_width - 10, image.height - text_height - 10)
    
    # Наложение текста водяного знака
    draw.text(position, watermark_text, (0, 0, 0, 128), font=font)
    watermarked_image = Image.alpha_composite(image.convert("RGBA"), watermark)

    return watermarked_image.convert("RGB")
