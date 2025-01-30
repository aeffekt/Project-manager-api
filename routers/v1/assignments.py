from fastapi import APIRouter, Depends, HTTPException, status
from db.database import get_session, Session
from models.project_manager import Assignment
from services.assignment_service import AssignmentService


# assignment Router
router = APIRouter(prefix="/assignments", tags=["assignments"])


@router.get("/", status_code=status.HTTP_200_OK)
def read_assignments(session: Session = Depends(get_session)) -> list[dict]:
    assignments = AssignmentService.get_all_assignments(session)
    return assignments


@router.get("/{assignment_id}", status_code=status.HTTP_200_OK)
def read_assignment(assignment_id: int, session: Session = Depends(get_session)) -> dict:
    assignment = AssignmentService.get_assignment(session, assignment_id)
    if assignment is None:
        raise HTTPException(status_code=404, detail="assignment not found")
    return {"assignment": assignment}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_assignment(assignment: Assignment, session: Session = Depends(get_session)) -> Assignment:
    return AssignmentService.create_assignment(assignment, session)


@router.put("/{assignment_id}", status_code=status.HTTP_200_OK)
def update_assignment(assignment_id: int, assignment: Assignment, session: Session = Depends(get_session)) -> dict[str, Assignment]:
    assignment_data = assignment.model_dump(exclude_unset=True)
    updated_assignment = AssignmentService.update_assignment(session, assignment_id, assignment_data)
    if updated_assignment is None:
        raise HTTPException(status_code=404, detail="assignment not found")
    return {"assignment": updated_assignment}


@router.delete("/{assignment_id}", status_code=status.HTTP_200_OK)
def delete_assignment(assignment_id: int, session: Session = Depends(get_session)) -> dict:
    deleted_assignment = AssignmentService.delete_assignment(session, assignment_id)
    if deleted_assignment is None:
        raise HTTPException(status_code=404, detail="assignment not found")
    return {"message": f"assignment {assignment_id} deleted successfully"}
