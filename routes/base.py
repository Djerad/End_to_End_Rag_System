from fastapi import APIRouter
import os

router = APIRouter(
    prefix="/api/v1",

)
@router.get("/")
async def root():
    appname = os.getenv("APP_NAME")
    return {"message": f"Welcome to {appname}!"}

