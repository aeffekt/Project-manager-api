"""
This file defines the EmployeeService class, which provides methods for
performing CRUD (Create, Read, Update, Delete) operations on Employee objects
using a synchronous database session. It also includes a method for
transforming Employee objects into dictionaries, including related Task data
from assigned Assignments.
"""
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from models.project_manager import Employee, Assignment
from typing import Optional


class EmployeeService:
    @staticmethod
    def employee_with_tasks(employee: Employee) -> dict:
        """transform an Employee object in a dict with its tasks assigned"""        
        return {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "position": employee.position,
            "Assigned tasks": [
                {                    
                    "name": assignment.task.name,
                    "due_date": assignment.task.due_date,
                    "project_id": assignment.task.project_id
                }
                for assignment in employee.assignments if assignment.task
            ]
        }

    @staticmethod
    def create_employee(employee: Employee, session: Session) -> Employee:
        session.add(employee)
        session.commit()
        session.refresh(employee)
        return employee

    @staticmethod
    def get_employee(session: Session, employee_id: int) -> Optional[dict]:
        statement = (
            select(Employee)
            .options(selectinload(Employee.assignments).selectinload(Assignment.task))
            .where(Employee.id == employee_id)
        )                
        employee = session.exec(statement).first()        
        return EmployeeService.employee_with_tasks(employee) if employee else None            

    @staticmethod
    def get_all_employees(session: Session, offset: int = 0, limit: int = 10) -> list[dict]:
        statement = (
            select(Employee)
            .options(selectinload(Employee.assignments).selectinload(Assignment.task))
            .offset(offset)
            .limit(limit)
        )
        employees = session.exec(statement).all()
        return [EmployeeService.employee_with_tasks(emp) for emp in employees]

    @staticmethod
    def update_employee(session: Session, employee_id: int, employee_data: Employee) -> Optional[dict]:
        statement = select(Employee).where(Employee.id == employee_id)
        employee = session.exec(statement).first()
        if employee:
            employee.sqlmodel_update(employee_data)
            session.add(employee)
            session.commit()
            session.refresh(employee)
        return employee

    @staticmethod
    def delete_employee(session: Session, employee_id: int) -> Optional[Employee]:
        statement = select(Employee).where(Employee.id == employee_id)
        employee = session.exec(statement).first()
        if employee:
            session.delete(employee)
            session.commit()
        return employee
