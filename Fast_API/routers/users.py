from fastapi import APIRouter, HTTPException
from models.users import User

router = APIRouter()

users = []


@router.post("/")
def create_user(user: User):
    for u in users:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User already exists")
    users.append(user)
    return {"message": "User created", "data": user}
@router.get("/")
def get_users():
    return users


@router.get("/{user_id}")
def get_users_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
def delete_user(user_id: int):
    user_to_delete = None
    for user in users:
        if user.id == user_id:
            user_to_delete = user
    if user_to_delete is None:
        raise HTTPException(status_code=404, detail="User not found")
    users.remove(user_to_delete)
    return {"message": f"User {user_id} deleted successfully"}



@router.put("/{user_id}")
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "User updated", "data": updated_user}
    
    raise HTTPException(status_code=404, detail="User not found")