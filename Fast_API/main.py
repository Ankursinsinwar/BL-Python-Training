from fastapi import FastAPI
from routers import users, notes

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(notes.router, prefix="/notes", tags=["Notes"])

