from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database.db import create_db
import asyncio
from handlers.clientHandlers import router
app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    asyncio.run(create_db())
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
