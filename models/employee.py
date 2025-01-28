from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from models.assignment import Assignment


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: Optional[str]
    position: Optional[str]

    # One to many relationship with Assignment
    assignments: List["Assignment"] = Relationship(back_populates="employee")