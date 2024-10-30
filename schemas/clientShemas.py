from pydantic import BaseModel, EmailStr
from typing import Optional

class ParticipantCreate(BaseModel):
    gender: str
    first_name: str
    last_name: str
    email: EmailStr