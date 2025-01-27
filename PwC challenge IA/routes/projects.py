from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from data.schemas.project_schema import ProjectCreate, ProjectUpdate
from services.project_services import (
    get_project, get_projects, create_project, update_project, delete_project
)
from data.db_connection import get_db

router = APIRouter(prefix="/projects", 
                   tags=["projects"],    # in docs groups this view tag
                   responses={404: {"message": "Not found"}})

@router.get("/projects", response_model=list[ProjectCreate])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_projects(db, skip, limit)

@router.get("/projects/{project_id}", response_model=ProjectCreate)
def read_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/projects", response_model=ProjectCreate)
def create_project_endpoint(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project(db, project)

@router.put("/projects/{project_id}", response_model=ProjectCreate)
def update_project_endpoint(project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)):
    return update_project(db, project_id, project)

@router.delete("/projects/{project_id}", response_model=dict)
def delete_project_endpoint(project_id: int, db: Session = Depends(get_db)):
    delete_project(db, project_id)
    return {"message": "Project deleted successfully"}