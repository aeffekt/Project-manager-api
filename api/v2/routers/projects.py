"""
This file defines the FastAPI router for handling project-related API endpoints
(version 2). It uses the ProjectService to interact with the database and
provides endpoints for creating, reading, updating, and deleting projects.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from db.database_async import get_async_session
from models.project_manager import Project
from api.v2.services.project_service import ProjectService


# Project Router
router = APIRouter(prefix="/v2/projects", tags=["v2", "projects"])

project_service_async = ProjectService()

# Create a project
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_project(project: Project, session: AsyncSession = Depends(get_async_session)) -> Project:
    return await project_service_async.create_project(project, session)


# Read all projects
@router.get("/", status_code=status.HTTP_200_OK)
async def read_projects(session: AsyncSession = Depends(get_async_session), offset: int = 0, limit: int = 10) -> list[dict]:
    projects = await project_service_async.get_all_projects(session, offset, limit)
    return projects


# Read one project with ID
@router.get("/{project_id}", status_code=status.HTTP_200_OK)
async def read_project(project_id: int, session: AsyncSession = Depends(get_async_session)) -> dict:
    project = await project_service_async.get_project(session, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"project": project}


# Update a project
@router.put("/{project_id}", status_code=status.HTTP_200_OK)
async def update_project(project_id: int, project: Project, session: AsyncSession = Depends(get_async_session)) ->  dict[str, Project]:
    project_data = project.model_dump(exclude_unset=True)
    updated_project = await project_service_async.update_project(session, project_id, project_data)
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"project": updated_project}


# Delete a project
@router.delete("/{project_id}", status_code=status.HTTP_200_OK)
async def delete_project(project_id: int, session: AsyncSession = Depends(get_async_session)) -> dict:
    deleted_project = await project_service_async.delete_project(session, project_id)
    if deleted_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": f"Project {project_id} deleted successfully"}