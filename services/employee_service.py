from sqlmodel import Session, select
from models.project_manager import Employee
from typing import Optional


class EmployeeService:
    @staticmethod
    def create_employee(employee: Employee, session: Session) -> Employee:
        session.add(employee)
        session.commit()
        session.refresh(employee)
        return employee

    @staticmethod
    def get_employee(session: Session, employee_id: int) -> Optional[Employee]:
        statement = select(Employee).where(Employee.id == employee_id)
        return session.exec(statement).first()

    @staticmethod
    def get_all_employees(session: Session) -> list[Employee]:
        statement = select(Employee)
        return session.exec(statement).all()

    @staticmethod
    def update_employee(session: Session, employee_id: int, employee_data: Employee) -> Optional[Employee]:
        employee = EmployeeService.get_employee(session, employee_id)
        if employee:
            employee.sqlmodel_update(employee_data)
            session.add(employee)
            session.commit()
            session.refresh(employee)
        return employee

    @staticmethod
    def delete_employee(session: Session, employee_id: int) -> Optional[Employee]:
        employee = EmployeeService.get_employee(session, employee_id)
        if employee:
            session.delete(employee)
            session.commit()
        return employee
