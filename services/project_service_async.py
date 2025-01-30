# services/project_service.py
from typing import List, Optional

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from models.project_manager import Project


class ProjectService:
    async def create_project(self, session: AsyncSession, project: Project) -> Project:
        session.add(project)
        await session.commit()
        await session.refresh(project)
        return project

    async def get_project(self, session: AsyncSession, project_id: int) -> Optional[Project]:
        result = await session.exec(select(Project).where(Project.id == project_id))
        return result.first()

    async def get_all_projects(self, session: AsyncSession) -> List[Project]:
        result = await session.exec(select(Project))
        return result.all()

    async def update_project(self, session: AsyncSession, project_id: int, project_update: Project) -> Optional[Project]:

        project = await self.get_project(session, project_id)
        if project:
            for key, value in project_update.dict(exclude_unset=True).items():
                setattr(project, key, value)
            session.add(project)
            await session.commit()
            await session.refresh(project)
            return project
        return None

    async def delete_project(self, session: AsyncSession, project_id: int) -> bool:
        project = await self.get_project(session, project_id)
        if project:
            await session.delete(project)
            await session.commit()
            return True
        return False