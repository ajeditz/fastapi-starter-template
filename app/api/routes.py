from fastapi import APIRouter
from app.schemas.message import Message
from app.services.greeter import greet_user

router = APIRouter()

@router.get("/greet", response_model=Message)
def root():
    return greet_user("Developer")
