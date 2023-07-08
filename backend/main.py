from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the my FasApi"}

@app.get("/api/tasks")
async def get_tasks():
    return "all tasks"


