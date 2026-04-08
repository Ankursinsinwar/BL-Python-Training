from fastapi import FastAPI
from route import route

app = FastAPI()

@app.get("/")
def home():
    return {"message": "running... "}

app.include_router(route, prefix='/get-data',  tags=['json data'])
