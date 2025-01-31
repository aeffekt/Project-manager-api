from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from db.database_async import get_async_session
from models.project_manager import Assignment
from api.v2.services.async_assignment_service import AssignmentService


# assignment Router
router = APIRouter(prefix="/v2/assignments", tags=["v2", "assignments"])


@router.get("/", status_code=status.HTTP_200_OK)
async def read_assignments(session: AsyncSession = Depends(get_async_session), offset: int = 0, limit: int = 10) -> list[dict]:
    assignments = await AssignmentService.get_all_assignments(session, offset, limit)
    return assignments


@router.get("/{assignment_id}", status_code=status.HTTP_200_OK)
async def read_assignment(assignment_id: int, session: AsyncSession = Depends(get_async_session)) -> dict:
    assignment = await AssignmentService.get_assignment(session, assignment_id)
    if assignment is None:
        raise HTTPException(status_code=404, detail="assignment not found")
    return {"assignment": assignment}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_assignment(assignment: Assignment, session: AsyncSession = Depends(get_async_session)) -> Assignment:
    return await AssignmentService.create_assignment(assignment, session)


@router.put("/{assignment_id}", status_code=status.HTTP_200_OK)
async def update_assignment(assignment_id: int, assignment: Assignment, session: AsyncSession = Depends(get_async_session)) -> dict[str, Assignment]:
    assignment_data = assignment.model_dump(exclude_unset=True)
    updated_assignment = await AssignmentService.update_assignment(session, assignment_id, assignment_data)
    if updated_assignment is None:
        raise HTTPException(status_code=404, detail="assignment not found")
    return {"assignment": updated_assignment}


@router.delete("/{assignment_id}", status_code=status.HTTP_200_OK)
async def delete_assignment(assignment_id: int, session: AsyncSession = Depends(get_async_session)) -> dict:
    deleted_assignment = await AssignmentService.delete_assignment(session, assignment_id)
    if deleted_assignment is None:
        raise HTTPException(status_code=404, detail="assignment not found")
    return {"message": f"assignment {assignment_id} deleted successfully"}
