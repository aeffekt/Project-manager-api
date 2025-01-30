from sqlmodel import Session, select
from models.project_manager import Assignment
from typing import Optional


class AssignmentService:
    @staticmethod
    def create_assignment(assignment: Assignment, session: Session) -> Assignment:
        session.add(assignment)
        session.commit()
        session.refresh(assignment)
        return assignment

    @staticmethod
    def get_assignment(session: Session, assignment_id: int) -> Optional[Assignment]:
        statement = select(Assignment).where(Assignment.id == assignment_id)
        return session.exec(statement).first()

    @staticmethod
    def get_all_assignments(session: Session):
        statement = select(Assignment)
        return session.exec(statement).all()

    @staticmethod
    def update_assignment(session: Session, assignment_id: int, assignment_data: Assignment) -> list[Assignment]:
        assignment = AssignmentService.get_assignment(session, assignment_id)
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