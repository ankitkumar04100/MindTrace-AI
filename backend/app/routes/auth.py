from fastapi import APIRouter, HTTPException
from app.security import hash_password, verify_password

router = APIRouter()

fake_users_db = {}

@router.post("/register")
def register(username: str, password: str):
    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users_db[username] = hash_password(password)
    return {"message": "User registered successfully"}

@router.post("/login")
def login(username: str, password: str):
    stored_password = fake_users_db.get(username)
    if not stored_password or not verify_password(password, stored_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}
