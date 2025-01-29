from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def start() -> dict:
    """
    Start endpoint to verify the application is running correctly.
    :return: A simple message confirming the start endpoint.
    """
    return {"message": "Start endpoint is working!"}