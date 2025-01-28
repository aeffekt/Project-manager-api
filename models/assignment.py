from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from models.task import Task
from models.employee import Employee


class Assignment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    task_id: int = Field(default=None, foreign_key="task.id")
    employee_id: int = Field(default=None, foreign_key="employee.id")

    # many to one relationchip with Task
    task: Optional["Task"] = Relationship(back_populates="assignments")

    # many to one relationchip with Employee
    employee: Optional["Employee"] = Relationship(back_populates="assignments")