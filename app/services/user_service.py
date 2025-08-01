from app.schemas.user import UserCreate, UserResponse

def create_user(user: UserCreate) -> UserResponse:
    # Simulate DB operation
    return UserResponse(id=1, username=user.username, email=user.email)
