from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def start() -> dict:
    return {"message": "Start endpoint is working!"}