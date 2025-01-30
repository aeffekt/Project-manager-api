
# routers/projects.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from db.database_async import get_async_session
from models.project_manager import Project
from services.project_service_async import ProjectService

router = APIRouter(prefix="/projects_async", tags=["projects_async"])
project_service = ProjectService()



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_project(project: Project, session: AsyncSession = Depends(get_async_session)):
    return await project_service.create_project(session, project)


@router.get("/", response_model=List[Project])
async def read_projects(session: AsyncSession = Depends(get_async_session)):    
    return await project_service.get_all_projects(session)


@router.get("/{project_id}", response_model=Project)
async def read_project(project_id: int, session: AsyncSession = Depends(get_async_session)):
    project = await project_service.get_project(session, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.patch("/{project_id}", response_model=Project)
async def update_project(project_id: int, project: Project, session: AsyncSession = Depends(get_async_session)):
    updated_project = await project_service.update_project(session, project_id, project)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: int, session: AsyncSession = Depends(get_async_session)):
    if not await project_service.delete_project(session, project_id):
        raise HTTPException(status_code=404, detail="Project not found")
    return None
