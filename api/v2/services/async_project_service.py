from sqlmodel import select, func
from sqlmodel.ext.asyncio.session import AsyncSession
from models.project_manager import Project, Task
from typing import Optional, List


class ProjectService:
    async def add_tasks_to_project(project: Project, task_count: int) -> dict:
        """Transform a Project Object to a dict with amount of tasks assigned."""        
        return {
            "id": project.id,
            "name of project": project.name,
            "description": project.description,
            "start_date": project.start_date,
            "task_count": task_count
        }

    @staticmethod
    async def create_project(project: Project, session: AsyncSession) -> Project:
        session.add(project)
        await session.commit()
        await session.refresh(project)
        return project

    @staticmethod
    async def get_project(session: AsyncSession, project_id: int) -> Optional[dict]:
        statement = (
            select(Project, func.count(Task.id).label("task_count"))
            .outerjoin(Task, Project.id == Task.project_id)
            .where(Project.id == project_id)
            .group_by(Project.id)
        )
        result = await session.exec(statement)
        if not result:
            return None
        project, task_count = result.first()
        return ProjectService.add_tasks_to_project(project, task_count)


    @staticmethod
    async def get_all_projects(session: AsyncSession, offset: int = 0, limit: int = 10) -> List[dict]:
        statement = (
            select(Project, func.count(Task.id).label("task_count"))
            .outerjoin(Task, Project.id == Task.project_id)
            .group_by(Project.id)
            .offset(offset)
            .limit(limit)
        )
        projects = await session.exec(statement)
        return [ProjectService.add_tasks_to_project(proj, task_count) for proj, task_count in projects.all()]

    @staticmethod
    async def update_project(session: AsyncSession, project_id: int, project_data: Project) -> Optional[Project]:
        # first we obtain the existing project        
        statement = select(Project).where(Project.id == project_id)
        project = await session.exec(statement).first()
        if project:
            # Update fields with new data
            project.sqlmodel_update(project_data)
            session.add(project)
            await session.commit()
            await session.refresh(project)
        return project

    @staticmethod
    async def delete_project(session: AsyncSession, project_id: int) -> Optional[Project]:
        # Find object first, then delete
        statement = select(Project).where(Project.id == project_id)
        project = await session.exec(statement).first()
        if project:
            await session.delete(project)
            await session.commit()
        return project