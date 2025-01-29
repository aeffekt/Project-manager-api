from fastapi import APIRouter, Depends, HTTPException, status
from db.conn import get_session, Session
from models.project_manager import Project
from services.project_service import ProjectService


router = APIRouter(prefix="/projects", tags=["projects"])


# Read all projects
@router.get("/", status_code=status.HTTP_200_OK)
def read_projects(session: Session = Depends(get_session)):
    projects = ProjectService.get_all_projects(session)
    return {"projects": projects}


# Read one project with ID
@router.get("/{project_id}", status_code=status.HTTP_200_OK)
def read_project(project_id: int, session: Session = Depends(get_session)):
    project = ProjectService.get_project(session, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"project": project}


# Create a project
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_project(project: Project, session: Session = Depends(get_session)):
    return ProjectService.create_project(project, session)


# Update a project
@router.put("/{project_id}", status_code=status.HTTP_200_OK)
def update_project(project_id: int, project: Project, session: Session = Depends(get_session)):
    project_data = project.model_dump(exclude_unset=True)
    updated_project = ProjectService.update_project(session, project_id, project_data)
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"project": updated_project}


# Delete a project
@router.delete("/{project_id}", status_code=status.HTTP_200_OK)
def delete_project(project_id: int, session: Session = Depends(get_session)):
    deleted_project = ProjectService.delete_project(session, project_id)
    if deleted_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": f"Project {project_id} deleted successfully"}