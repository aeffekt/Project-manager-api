from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional, List
from models.project import Project
from models.assignment import Assignment


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str    
    due_date: Optional[date] = Field(default=None)
    project_id: int = Field(default=None, foreign_key="project.id")

    # many to one relationchip with  Project
    project: Optional["Project"] = Relationship(back_populates="tasks")

    # one to many relationchip with Assignment
    assignments: List["Assignment"] = Relationship(back_populates="task")