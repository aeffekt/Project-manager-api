from fastapi import APIRouter
from fastapi import Depends
from db.conn import get_session, Session
from models.projects import Project


router = APIRouter(
                    prefix="/projects", 
                    tags=["projects"]
                    )

# Read all projects
@router.get("/")
def read_project():
    return {"Projects": []}


# Read one project with ID
@router.get("/{id}")
def read_project():
    return {"Project": []}


# Create a project
@router.post("/")
def create_project(project: Project, session: Session = Depends(get_session)):
    session.add(project)
    session.commit()    
    session.refresh(project)    
    return project


# Update a project
@router.put("/{id}")
def update_project():
    return {"Update project": []}


# Delete a project
@router.delete("/{id}")
def delete_project():
    return {"Delete project": []}