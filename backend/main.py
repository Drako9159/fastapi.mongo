from fastapi import FastAPI
from routes.task import task

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the my FasApi app"}


app.include_router(task)
  