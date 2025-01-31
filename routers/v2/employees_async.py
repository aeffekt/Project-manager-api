from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from db.database_async import get_async_session
from models.project_manager import Employee
from services.async_employee_service import EmployeeService


# Employee Router
router = APIRouter(prefix="/v2/employees", tags=["v2", "employees"])


@router.get("/", status_code=status.HTTP_200_OK)
async def read_employees(session: AsyncSession = Depends(get_async_session), offset: int = 0, limit: int = 10) -> list[dict]:
    employees = await EmployeeService.get_all_employees(session, offset, limit)
    return employees


@router.get("/{employee_id}", status_code=status.HTTP_200_OK)
async def read_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)) -> dict:
    employee = await EmployeeService.get_employee(session, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"employee": employee}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_employee(employee: Employee, session: AsyncSession = Depends(get_async_session)) -> Employee:
    return await EmployeeService.create_employee(employee, session)


@router.put("/{employee_id}", status_code=status.HTTP_200_OK)
async def update_employee(employee_id: int, employee: Employee, session: AsyncSession = Depends(get_async_session)) -> dict:
    employee_data = employee.model_dump(exclude_unset=True)
    updated_employee = await EmployeeService.update_employee(session, employee_id, employee_data)
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"employee": updated_employee}


@router.delete("/{employee_id}", status_code=status.HTTP_200_OK)
async def delete_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)) -> dict:
    deleted_employee = await EmployeeService.delete_employee(session, employee_id)
    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": f"Employee {employee_id} deleted successfully"}

