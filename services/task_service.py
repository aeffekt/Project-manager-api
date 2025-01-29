from sqlmodel import Session, select
from models.project_manager import Task


class TaskService:
    @staticmethod
    def create_task(task: Task, session: Session):
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

    @staticmethod
    def get_task(session: Session, task_id: int):
        statement = select(Task).where(Task.id == task_id)
        return session.exec(statement).first()

    @staticmethod
    def get_all_tasks(session: Session):
        statement = select(Task)
        return session.exec(statement).all()

    @staticmethod
    def update_task(session: Session, task_id: int, task_data: Task):
        task = TaskService.get_task(session, task_id)
        if task:
            task.sqlmodel_update(task_data)
            session.add(task)
            session.commit()
            session.refresh(task)
        return task

    @staticmethod
    def delete_task(session: Session, task_id: int):
        task = TaskService.get_task(session, task_id)
        if task:
            session.delete(task)
            session.commit()
        return task