from sqlmodel import Session, select
from models.project_manager import Assignment
from sqlalchemy.orm import selectinload
from typing import Optional


class AssignmentService:
    @staticmethod
    def transform_assignment(assignment: Assignment) -> dict:
        """Transform an Assignment Object into dict with the employeed assigned and the task."""
        return {
            "id": assignment.id,
            "employee": {
                "id": assignment.employee.id,
                "name": assignment.employee.name
            } if assignment.employee else None,
            "task": {
                "id": assignment.task.id,
                "name": assignment.task.name
            } if assignment.task else None
        }

    @staticmethod
    def create_assignment(assignment: Assignment, session: Session) -> Assignment:
        session.add(assignment)
        session.commit()
        session.refresh(assignment)
        return assignment

    @staticmethod
    def get_assignment(session: Session, assignment_id: int) -> Optional[dict]:
        statement = (
            select(Assignment)
            .options(
                selectinload(Assignment.employee),
                selectinload(Assignment.task)
            )
            .where(Assignment.id == assignment_id)
        )

        assignment = session.exec(statement).first()
        return AssignmentService.transform_assignment(assignment) if assignment else None

    @staticmethod
    def get_all_assignments(session: Session, offset: int = 0, limit: int = 10) -> list[dict]:
        statement = (
            select(Assignment)
            .options(
                selectinload(Assignment.employee),
                selectinload(Assignment.task)
            )
            .offset(offset)
            .limit(limit)
        )

        assignments = session.exec(statement).all()
        return [AssignmentService.transform_assignment(assignment) for assignment in assignments]

    @staticmethod
    def update_assignment(session: Session, assignment_id: int, assignment_data: Assignment) -> Assignment:
        statement = select(Assignment).where(Assignment.id == assignment_id)
        assignment = session.exec(statement).first()
        if assignment:
            assignment.sqlmodel_update(assignment_data)
            session.add(assignment)
            session.commit()
            session.refresh(assignment)
        return assignment

    @staticmethod
    def delete_assignment(session: Session, assignment_id: int) -> Optional[Assignment]:
        assignment = AssignmentService.get_assignment(session, assignment_id)
        if assignment:
            session.delete(assignment)
            session.commit()
        return assignment