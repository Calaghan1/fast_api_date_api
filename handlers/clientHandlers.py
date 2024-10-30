from fastapi import APIRouter, UploadFile, HTTPException, File, Form
from schemas.clientShemas import ParticipantCreate
import controller.clientcontroller as clientcontroller
router = APIRouter()


@router.post("/api/clients/create")
async def create_client(
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    gender: str = Form(...),
    avatar: UploadFile = File(...)
):
    avatar_data = await avatar.read()
    if await clientcontroller.create_client(avatar_data, gender, first_name, last_name, email):
        return {"status": "success"}
    else:
        return HTTPException(status_code=400, detail="Error creating client")
    
    
    