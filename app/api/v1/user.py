# user.py
import json
from fastapi import APIRouter, HTTPException

router = APIRouter()

# Chemin vers le fichier JSON des utilisateurs
USERS_FILE_PATH = "./app/database/data.json"

def read_users():
    with open(USERS_FILE_PATH, "r") as file:
        users = json.load(file)
    return users

def write_users(users):
    with open(USERS_FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)

@router.get("/users")
async def get_users():
    return read_users()

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    users = read_users()
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

@router.post("/users")
async def create_user(name: str):
    users = read_users()
    new_user_id = max(user["id"] for user in users) + 1
    new_user = {"id": new_user_id, "name": name}
    users.append(new_user)
    write_users(users)
    return new_user

@router.put("/users/{user_id}")
async def update_user(user_id: int, name: str):
    users = read_users()
    for user in users:
        if user["id"] == user_id:
            user["name"] = name
            write_users(users)
            return user
    raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    users = read_users()
    new_users = [user for user in users if user["id"] != user_id]
    if len(new_users) < len(users):
        write_users(new_users)
        return {"message": "Utilisateur supprimé avec succès"}
    raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
