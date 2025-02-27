"""
This file defines the FastAPI router for handling task-related API endpoints
(version 1). It uses the TaskService to interact with the database and
provides endpoints for creating, reading, updating, and deleting tasks.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from db.database import get_session
from sqlmodel import Session
from models.project_manager import Task
from api.v1.services.task_service import TaskService


# Task Router
router = APIRouter(prefix="/v1/tasks", tags=["v1", "tasks"])


@router.get("/", status_code=status.HTTP_200_OK)
def read_tasks(session: Session = Depends(get_session), offset: int = 0, limit: int = 10) -> list[dict]:
    tasks = TaskService.get_all_tasks(session, offset, limit)
    return tasks


@router.get("/{task_id}", status_code=status.HTTP_200_OK)
def read_task(task_id: int, session: Session = Depends(get_session)) -> dict:
    task = TaskService.get_task(session, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"task": task}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: Task, session: Session = Depends(get_session)) -> Task:
    return TaskService.create_task(task, session)


@router.put("/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: Task, session: Session = Depends(get_session)) -> dict[str, Task]:
    task_data = task.model_dump(exclude_unset=True)
    updated_task = TaskService.update_task(session, task_id, task_data)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"task": updated_task}


@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, session: Session = Depends(get_session)) -> dict:
    deleted_task = TaskService.delete_task(session, task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"message": f"task {task_id} deleted successfully"}
