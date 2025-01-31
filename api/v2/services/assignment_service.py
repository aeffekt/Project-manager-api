"""
This file defines the AssignmentService class, which provides methods for
performing CRUD (Create, Read, Update, Delete) operations on Assignment objects
using an asynchronous database session. It also includes a method for
transforming Assignment objects into dictionaries, including related Employee
and Task data.
"""
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from models.project_manager import Assignment
from sqlalchemy.orm import selectinload
from typing import Optional


class AssignmentService:
    @staticmethod
    async def transform_assignment(assignment: Assignment) -> dict:
        """Transform an Assignment Object into dict with the employeed assigned and the task."""
        return {
            "assignment id": assignment.id,
            "employee assigned": {                
                "name": assignment.employee.name
            } if assignment.employee else None,
            "task": {
                "id": assignment.task.id,
                "name": assignment.task.name
            } if assignment.task else None
        }

    @staticmethod
    async def create_assignment(assignment: Assignment, session: AsyncSession) -> Assignment:
        session.add(assignment)
        await session.commit()
        await session.refresh(assignment)
        return assignment

    @staticmethod
    async def get_assignment(session: AsyncSession, assignment_id: int) -> Optional[dict]:
        statement = (
            select(Assignment)
            .options(
                selectinload(Assignment.employee),
                selectinload(Assignment.task)
            )
            .where(Assignment.id == assignment_id)
        )

        assignment = await session.exec(statement).first()
        return AssignmentService.transform_assignment(assignment) if assignment else None

    @staticmethod
    async def get_all_assignments(session: AsyncSession, offset: int = 0, limit: int = 10) -> list[dict]:
        statement = (
            select(Assignment)
            .options(
                selectinload(Assignment.employee),
                selectinload(Assignment.task)
            )
            .offset(offset)
            .limit(limit)
        )

        assignments = await session.exec(statement)
        return [await AssignmentService.transform_assignment(assignment) for assignment in assignments.all()]

    @staticmethod
    async def update_assignment(session: AsyncSession, assignment_id: int, assignment_data: Assignment) -> Assignment:
        statement = select(Assignment).where(Assignment.id == assignment_id)
        assignment = await session.exec(statement).first()
        if assignment:
            assignment.sqlmodel_update(assignment_data)
            session.add(assignment)
            await session.commit()
            await session.refresh(assignment)
        return assignment

    @staticmethod
    async def delete_assignment(session: AsyncSession, assignment_id: int) -> Optional[Assignment]:
        statement = select(Assignment).where(Assignment.id == assignment_id)
        assignment = await session.exec(statement).first()
        if assignment:
            await session.delete(assignment)
            await session.commit()
        return assignment