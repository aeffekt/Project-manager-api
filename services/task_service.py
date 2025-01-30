from sqlmodel import Session, select
from models.project_manager import Task, Project
from typing import Optional
from datetime import datetime, date


class TaskService:
    @staticmethod
    def adjust_due_date_based_on_project(task_data: dict, session: Session) -> date:
        # Convert due_date to a date object if it's a string
        if isinstance(task_data.get("due_date"), str):
            task_data["due_date"] = datetime.strptime(task_data["due_date"], "%Y-%m-%d").date()

        # Get project start_date
        project = session.get(Project, task_data["project_id"])
        if project and task_data["due_date"] and task_data["due_date"] < project.start_date.date():
            task_data["due_date"] = project.start_date.date()  # Adjust due_date
        return task_data
    
    @staticmethod
    def create_task(task: Task, session: Session) -> Task:
        task_data = task.model_dump()
        # Adjust due_date based on the project's start_date
        task_data = TaskService.adjust_due_date_based_on_project(task_data, session)
        task = Task(**task_data)
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

    @staticmethod
    def get_task(session: Session, task_id: int) -> Optional[Task]:
        statement = select(Task).where(Task.id == task_id)
        return session.exec(statement).first()

    @staticmethod
    def get_all_tasks(session: Session) -> list[Task]:
        statement = select(Task)
        return session.exec(statement).all()

    @staticmethod
    def update_task(session: Session, task_id: int, task_data: Task) -> Optional[Task]:
        task = TaskService.get_task(session, task_id)
        if task:
            # Adjust due_date based on the project's start_date
            task_data = TaskService.adjust_due_date_based_on_project(task_data, session)

            task.sqlmodel_update(task_data)
            session.add(task)
            session.commit()
            session.refresh(task)
        return task

    @staticmethod
    def delete_task(session: Session, task_id: int) -> Optional[Task]:
        task = TaskService.get_task(session, task_id)
        if task:
            session.delete(task)
            session.commit()
        return task