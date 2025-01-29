from fastapi import APIRouter, Depends, HTTPException, status
from db.conn import get_session, Session
from models.project_manager import assignment
from services.assignment_service import AssignmentService


router_assignment = APIRouter(prefix="/assignments", tags=["assignments"])


# assignment Router
@router_assignment.get("/", status_code=status.HTTP_200_OK)
def read_assignments(session: Session = Depends(get_session)):
    assignments = AssignmentService.get_all_assignments(session)
    return {"assignments": assignments}


@router_assignment.get("/{assignment_id}", status_code=status.HTTP_200_OK)
def read_assignment(assignment_id: int, session: Session = Depends(get_session)):
    assignment = AssignmentService.get_assignment(session, assignment_id)
    if assignment is None:
        raise HTTPException(status_code=404, detail="assignment not found")
    return {"assignment": assignment}


@router_assignment.post("/", status_code=status.HTTP_201_CREATED)
def create_assignment(assignment: assignment, session: Session = Depends(get_session)):
    return AssignmentService.create_assignment(assignment, session)


@router_assignment.put("/{assignment_id}", status_code=status.HTTP_200_OK)
def update_assignment(assignment_id: int, assignment: assignment, session: Session = Depends(get_session)):
    assignment_data = assignment.model_dump(exclude_unset=True)
    updated_assignment = AssignmentService.update_assignment(session, assignment_id, assignment_data)
    if updated_assignment is None:
        raise HTTPException(status_code=404, detail="assignment not found")
    return {"assignment": updated_assignment}


@router_assignment.delete("/{assignment_id}", status_code=status.HTTP_200_OK)
def delete_assignment(assignment_id: int, session: Session = Depends(get_session)):
    deleted_assignment = AssignmentService.delete_assignment(session, assignment_id)
    if deleted_assignment is None:
        raise HTTPException(status_code=404, detail="assignment not found")
    return {"message": f"assignment {assignment_id} deleted successfully"}
