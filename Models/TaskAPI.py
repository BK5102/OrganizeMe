"""
    methods: createTask(), removeTask()
"""
from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from .Task import Tasks
from .DBBase import DBBase
from typing import List

router = APIRouter()


class Task_SerializerReq(BaseModel):
    stuIDT: str
    task: str

    class Config:
        orm_mode = True

class Task_Serializer(BaseModel):
    taskID: int
    stuIDT: int
    task: str

    class Config:
        orm_mode = True

db= DBBase.session

@router.get("/tasks", response_model=List[Task_Serializer], status_code=200)
def get_all_Tasks():
    tasks = db.query(Tasks).all()
    return tasks

@router.post("/task", response_model=Task_Serializer, status_code=status.HTTP_201_CREATED)
def create_new_Task(task:Task_SerializerReq):
    db_task = db.query(Tasks).filter(Tasks.task == task.task).first()

    if db_task is not None:
        raise HTTPException(status_code=400, detail="Task already exists.")
    
    new_task = Tasks(int(task.stuIDT),task.task)

    try:
        db.add(new_task)
    except:
        db.rollback()
        raise
    else:
        db.commit()

    return new_task

@router.delete("/task/{taskID}")
def remove_Task(taskID: int):
    task_to_del = db.query(Tasks).filter(Tasks.taskID == taskID).first()

    if task_to_del is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")
    
    try:
        db.delete(task_to_del)
    except:
        db.rollback()
        raise
    else:
        db.commit()

    return task_to_del