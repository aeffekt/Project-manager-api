from sqlmodel import Session, select
from models.project_manager import Project
from typing import Optional, List


class ProjectService:
    @staticmethod
    def create_project(project: Project, session: Session) -> Project:
        session.add(project)
        session.commit()
        session.refresh(project)
        return project

    @staticmethod
    def get_project(session: Session, project_id: int) -> Optional[Project]:
        project = select(Project).where(Project.id == project_id)
        result = session.exec(project).first()
        return result

    @staticmethod
    def get_all_projects(session: Session) -> List[Project]:
        statement = select(Project)
        results = session.exec(statement).all()
        return results

    @staticmethod
    def update_project(session: Session, project_id: int, project_data: Project) -> Optional[Project]:
        # first we obtain the existing project
        project = ProjectService.get_project(session, project_id)
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