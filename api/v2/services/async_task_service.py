from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from models.project_manager import Task, Project, Assignment
from sqlalchemy.orm import selectinload
from typing import Optional
from datetime import datetime, date


class TaskService:
    @staticmethod
    async def transform_task(task: Task) -> dict:
        """Transform a Task Object into dict with the employeed assigned."""
        return {
            "task id": task.id,
            "name": task.name,
            "due_date": task.due_date,
            "project_id": task.project_id,
            "employees assigned": [
                {
                    "id": assignment.employee.id,
                    "name": assignment.employee.name,
                    "email": assignment.employee.email,
                    "position": assignment.employee.position
                }
                for assignment in task.assignments if assignment.employee
            ]
        }
    
    @staticmethod
    async def adjust_due_date_based_on_project(task_data: dict, session: AsyncSession) -> date:
        # Convert due_date to a date object if it's a string
        if isinstance(task_data.get("due_date"), str):
            task_data["due_date"] = datetime.strptime(task_data["due_date"], "%Y-%m-%d").date()

        # Get project start_date
        project = session.get(Project, task_data["project_id"])
        if project and task_data["due_date"] and task_data["due_date"] < project.start_date.date():
            task_data["due_date"] = project.start_date.date()  # Adjust due_date
        return task_data
    
    @staticmethod
    async def create_task(task: Task, session: AsyncSession) -> Task:
        task_data = task.model_dump()
        # Adjust due_date based on the project's start_date
        task_data = TaskService.adjust_due_date_based_on_project(task_data, session)
        task = Task(**task_data)
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task

    @staticmethod
    async def get_task(session: AsyncSession, task_id: int) -> Optional[dict]:
        statement = (
            select(Task)
            .options(selectinload(Task.assignments).selectinload(Assignment.employee))
            .where(Task.id == task_id)
        )

        task = await session.exec(statement).first()
        return await TaskService.transform_task(task) if task else None

    @staticmethod
    async def get_all_tasks(session: AsyncSession, offset: int = 0, limit: int = 10) -> list[dict]:
        statement = (
            select(Task)
            .options(selectinload(Task.assignments).selectinload(Assignment.employee))
            .offset(offset)
            .limit(limit)
        )

        tasks = await session.exec(statement)
        return [await TaskService.transform_task(task) for task in tasks.all()]

    @staticmethod
    async def update_task(session: AsyncSession, task_id: int, task_data: Task) -> Optional[Task]:
        statement = select(Task).where(Task.id == task_id)
        task = await session.exec(statement).first()        
        if task:
            # Adjust due_date based on the project's start_date
            task_data = TaskService.adjust_due_date_based_on_project(task_data, session)

            task.sqlmodel_update(task_data)
            session.add(task)
            await session.commit()
            await session.refresh(task)
        return task

    @staticmethod
    async def delete_task(session: AsyncSession, task_id: int) -> Optional[Task]:
        statement = select(Task).where(Task.id == task_id)
        task = await session.exec(statement).first() 
        if task:
            await session.delete(task)
            await session.commit()
        return task