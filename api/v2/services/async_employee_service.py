from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload
from models.project_manager import Employee, Assignment
from typing import Optional


class EmployeeService:
    @staticmethod
    async def employee_with_tasks(employee: Employee) -> dict:
        """transform an Employee object in a dict with its tasks assigned"""        
        return {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "position": employee.position,
            "Assigned tasks": [
                {
                    "id": assignment.task.id,
                    "name": assignment.task.name,
                    "due_date": assignment.task.due_date,
                    "project_id": assignment.task.project_id
                }
                for assignment in employee.assignments if assignment.task
            ]
        }

    @staticmethod
    async def create_employee(employee: Employee, session: AsyncSession) -> Employee:
        session.add(employee)
        await session.commit()
        await session.refresh(employee)
        return employee

    @staticmethod
    async def get_employee(session: AsyncSession, employee_id: int) -> Optional[dict]:
        statement = (
            select(Employee)
            .options(selectinload(Employee.assignments).selectinload(Assignment.task))
            .where(Employee.id == employee_id)
        )                
        employee = await session.exec(statement)
        return await EmployeeService.employee_with_tasks(employee.first()) if employee else None            

    @staticmethod
    async def get_all_employees(session: AsyncSession, offset: int = 0, limit: int = 10) -> list[dict]:
        statement = (
            select(Employee)
            .options(selectinload(Employee.assignments).selectinload(Assignment.task))
            .offset(offset)
            .limit(limit)
        )
        employees = await session.exec(statement)
        return await [EmployeeService.employee_with_tasks(emp) for emp in employees.all()]

    @staticmethod
    async def update_employee(session: AsyncSession, employee_id: int, employee_data: Employee) -> Optional[dict]:
        statement = select(Employee).where(Employee.id == employee_id)
        employee = await session.exec(statement).first()
        if employee:
            employee.sqlmodel_update(employee_data)
            session.add(employee)
            await session.commit()
            await session.refresh(employee)
        return employee

    @staticmethod
    async def delete_employee(session: AsyncSession, employee_id: int) -> Optional[Employee]:
        statement = select(Employee).where(Employee.id == employee_id)
        employee = await session.exec(statement).first()
        if employee:
            await session.delete(employee)
            await session.commit()
        return employee
