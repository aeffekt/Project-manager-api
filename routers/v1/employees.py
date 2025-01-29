from fastapi import APIRouter, Depends, HTTPException, status
from db.conn import get_session, Session
from models.project_manager import Employee
from services.employee_service import EmployeeService


# Employee Router
router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/", status_code=status.HTTP_200_OK)
def read_employees(session: Session = Depends(get_session)):
    employees = EmployeeService.get_all_employees(session)
    return {"employees": employees}


@router.get("/{employee_id}", status_code=status.HTTP_200_OK)
def read_employee(employee_id: int, session: Session = Depends(get_session)):
    employee = EmployeeService.get_employee(session, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"employee": employee}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_employee(employee: Employee, session: Session = Depends(get_session)):
    return EmployeeService.create_employee(employee, session)


@router.put("/{employee_id}", status_code=status.HTTP_200_OK)
def update_employee(employee_id: int, employee: Employee, session: Session = Depends(get_session)):
    employee_data = employee.model_dump(exclude_unset=True)
    updated_employee = EmployeeService.update_employee(session, employee_id, employee_data)
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"employee": updated_employee}


@router.delete("/{employee_id}", status_code=status.HTTP_200_OK)
def delete_employee(employee_id: int, session: Session = Depends(get_session)):
    deleted_employee = EmployeeService.delete_employee(session, employee_id)
    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": f"Employee {employee_id} deleted successfully"}

