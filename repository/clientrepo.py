import database.db as db
from database.models import Participant
from helpers.filefunc import add_watermark
from PIL import Image, ImageDraw, ImageFont
import io
async def create_participant(avatar: bytes, gender: str, first_name: str, last_name: str, email: str):
    async with db.async_session() as session:
        db_participant = Participant(
            avatar=avatar,
            gender=gender,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        session.add(db_participant)
        await session.commit()
        return db_participant