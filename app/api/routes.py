from fastapi import APIRouter
from app.models.user import User, UserCreate

router = APIRouter()

# In-memory mock "DB"
users_db = {}

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        return {"error": "User not found"}
    return user

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    new_id = len(users_db) + 1
    new_user = User(id=new_id, **user.dict())
    users_db[new_id] = new_user
    return new_user
