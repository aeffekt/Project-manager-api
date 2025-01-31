from sqlmodel import Session, select, func
from models.project_manager import Project, Task
from typing import Optional, List


class ProjectService:
    def add_tasks_to_project(project: Project, task_count: int) -> dict:
        """Transform a Project Object to a dict with amount of tasks assigned."""        
        return {
            "id": project.id,
            "name of project": project.name,
            "description": project.description,
            "start_date": project.start_date,
            "task_count": task_count
        }

    @staticmethod
    def create_project(project: Project, session: Session) -> Project:
        session.add(project)
        session.commit()
        session.refresh(project)
        return project

    @staticmethod
    def get_project(session: Session, project_id: int) -> Optional[dict]:
        statement = (
            select(Project, func.count(Task.id).label("task_count"))
            .outerjoin(Task, Project.id == Task.project_id)
            .where(Project.id == project_id)
            .group_by(Project.id)
        )
        result = session.exec(statement).first()        
        if not result:
            return None
        project, task_count = result        
        return ProjectService.add_tasks_to_project(project, task_count)


    @staticmethod
    def get_all_projects(session: Session, offset: int = 0, limit: int = 10) -> List[dict]:
        statement = (
            select(Project, func.count(Task.id).label("task_count"))
            .outerjoin(Task, Project.id == Task.project_id)
            .group_by(Project.id)
            .offset(offset)
            .limit(limit)
        )
        projects = session.exec(statement).all()
        return [ProjectService.add_tasks_to_project(proj, task_count) for proj, task_count in projects]

    @staticmethod
    def update_project(session: Session, project_id: int, project_data: Project) -> Optional[Project]:
        # first we obtain the existing project        
        statement = select(Project).where(Project.id == project_id)
        project = session.exec(statement).first()
        if project:
            # Update fields with new data
            project.sqlmodel_update(project_data)
            session.add(project)
            session.commit()
            session.refresh(project)
        return project

    @staticmethod
    def delete_project(session: Session, project_id: int) -> Optional[Project]:
        # Find object first, then delete
        project = ProjectService.get_project(session, project_id)
        if project:
            session.delete(project)
            session.commit()
        return project