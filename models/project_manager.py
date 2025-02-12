"""
This file defines the SQLModel models for the project manager API,
including Project, Employee, Task, and Assignment.
"""
from sqlmodel import Field, SQLModel, Column, TIMESTAMP, text, Relationship
from typing import Optional, List
from datetime import datetime, date


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    start_date: Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ))

    # One to many relationship with Task
    tasks: List["Task"] = Relationship(back_populates="project")


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: Optional[str]
    position: Optional[str]

    # One to many relationship with Assignment
    assignments: List["Assignment"] = Relationship(back_populates="employee")


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str    
    due_date: Optional[date] = Field(default=None)
    project_id: int = Field(default=None, foreign_key="project.id")

    # many to one relationchip with  Project
    project: Optional["Project"] = Relationship(back_populates="tasks")

    # one to many relationchip with Assignment
    assignments: List["Assignment"] = Relationship(back_populates="task")


class Assignment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int = Field(default=None, foreign_key="task.id")
    employee_id: int = Field(default=None, foreign_key="employee.id")

    # many to one relationchip with Task
    task: Optional["Task"] = Relationship(back_populates="assignments")

    # many to one relationchip with Employee
    employee: Optional["Employee"] = Relationship(back_populates="assignments")