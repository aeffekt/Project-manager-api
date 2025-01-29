from fastapi import APIRouter, Depends, HTTPException, status
from db.conn import get_session, Session
from models.project_manager import task
from services.task_service import TaskService


router_task = APIRouter(prefix="/tasks", tags=["tasks"])


# Task Router
@router_task.get("/", status_code=status.HTTP_200_OK)
def read_tasks(session: Session = Depends(get_session)):
    tasks = TaskService.get_all_tasks(session)
    return {"tasks": tasks}


@router_task.get("/{task_id}", status_code=status.HTTP_200_OK)
def read_task(task_id: int, session: Session = Depends(get_session)):
    task = TaskService.get_task(session, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"task": task}


@router_task.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: task, session: Session = Depends(get_session)):
    return TaskService.create_task(task, session)


@router_task.put("/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: task, session: Session = Depends(get_session)):
    task_data = task.model_dump(exclude_unset=True)
    updated_task = TaskService.update_task(session, task_id, task_data)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"task": updated_task}


@router_task.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    deleted_task = TaskService.delete_task(session, task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"message": f"task {task_id} deleted successfully"}
