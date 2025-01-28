from sqlmodel import Session, select
from models.project_manager import Project


class ProjectService:
    @staticmethod
    def create_project(project: Project, session: Session):
        session.add(project)
        session.commit()
        session.refresh(project)
        return project

    @staticmethod
    def get_project(session: Session, project_id: int):        
        project = select(Project).where(Project.id == project_id)
        result = session.exec(project).first()
        return result

    @staticmethod
    def get_all_projects(session: Session):        
        statement = select(Project)
        results = session.exec(statement).all()
        return results

    @staticmethod
    def update_project(session: Session, project_id: int, project_data: Project):
        # first we obtain the existing project
        project = ProjectService.get_project(session, project_id)
        if project:
            # Update fields with new data
            for key, value in project_data.model_dump(exclude_unset=True).items():
                setattr(project, key, value)
            session.add(project)
            session.commit()
            session.refresh(project)
        return project

    @staticmethod
    def delete_project(session: Session, project_id: int):
        # Find object first, then delete
        project = ProjectService.get_project(session, project_id)
        if project:
            session.delete(project)
            session.commit()
        return project