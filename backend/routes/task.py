from fastapi import APIRouter, HTTPException
from database import get_all_tasks, create_task, get_one_task_id, update_task, delete_task, get_one_task
from models import Task, UpdateTask

task = APIRouter()

@task.get("/api/tasks")
async def get_tasks():
    tasks = await get_all_tasks()
    return tasks


@task.post("/api/tasks", response_model=Task)
async def save_tasks(task: Task):
    taskFound = await get_one_task(task.title)
    if taskFound:
        raise HTTPException(409, "Task already exists")
    response = await create_task(task.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@task.get("/api/tasks/{id}", response_model=Task)
async def get_task(id: str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f"Task with id {id} not found")


@task.put("/api/tasks/{id}", response_model=Task)
async def  put_task(id: str, task: UpdateTask):
    response = await update_task(id, Task)
    if response:
        return response
    raise HTTPException(404, f"Task with id {id} not found")


@task.delete("/api/tasks/{id}")
async def remove_task():
    response = await delete_task(id)
    if response:
        return "Successfully deleted task"
    raise HTTPException(404, f"Task with id {id} not found")