import io
from PIL import Image
from helpers.filefunc import add_watermark
import repository.clientrepo as clientrepo
async def create_client(avatar, gender: str, first_name: str, last_name: str, email: str):
    image = Image.open(io.BytesIO(avatar))
    print(image)
    watermarked_image = await add_watermark(image, "Sample Watermark")
    print(watermarked_image)
    image_bytes = io.BytesIO()
    watermarked_image.save(image_bytes, format="PNG")
    image_bytes = image_bytes.getvalue()
    if await clientrepo.create_participant(image_bytes, gender, first_name, last_name, email):
        return True
    else:
        return False
