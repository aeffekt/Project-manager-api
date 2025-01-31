from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from db.database_async import get_async_session
from models.project_manager import Task
from api.v2.services.task_service import TaskService


# Task Router
router = APIRouter(prefix="/v2/tasks", tags=["v2", "tasks"])


@router.get("/", status_code=status.HTTP_200_OK)
async def read_tasks(session: AsyncSession = Depends(get_async_session), offset: int = 0, limit: int = 10) -> list[dict]:
    tasks = await TaskService.get_all_tasks(session, offset, limit)
    return tasks


@router.get("/{task_id}", status_code=status.HTTP_200_OK)
async def read_task(task_id: int, session: AsyncSession = Depends(get_async_session)) -> dict:
    task = await TaskService.get_task(session, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"task": task}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task, session: AsyncSession = Depends(get_async_session)) -> Task:
    return await TaskService.create_task(task, session)


@router.put("/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task: Task, session: AsyncSession = Depends(get_async_session)) -> dict[str, Task]:
    task_data = task.model_dump(exclude_unset=True)
    updated_task = await TaskService.update_task(session, task_id, task_data)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"task": updated_task}


@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
async def delete_task(task_id: int, session: AsyncSession = Depends(get_async_session)) -> dict:
    deleted_task = await TaskService.delete_task(session, task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return {"message": f"task {task_id} deleted successfully"}
