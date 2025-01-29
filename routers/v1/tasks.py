from fastapi import APIRouter, Depends, HTTPException, status
from db.conn import get_session, Session
from models.project_manager import Task
from services.task_service import TaskService


# Task Router
router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", status_code=status.HTTP_200_OK)
def read_tasks(session: Session = Depends(get_session)):
    tasks = TaskService.get_all_tasks(session)
    return {"tasks": tasks}


@router.get("/{task_id}", status_code=status.HTTP_200_OK)
def read_task(task_id: int, session: Session = Depends(get_session)):
    task = TaskService.get_task(session, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"task": task}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: Task, session: Session = Depends(get_session)):
    return TaskService.create_task(task, session)


@router.put("/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: Task, session: Session = Depends(get_session)):
    task_data = task.model_dump(exclude_unset=True)
    updated_task = TaskService.update_task(session, task_id, task_data)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"task": updated_task}


@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    deleted_task = TaskService.delete_task(session, task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"message": f"task {task_id} deleted successfully"}
