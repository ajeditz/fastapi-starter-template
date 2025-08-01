from fastapi import FastAPI
from app.routes import users


from app.core.config import settings
print(settings.app_name)


app = FastAPI()

# Include the users router under "/users"
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI app!"}
