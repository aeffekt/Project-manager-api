from sqlmodel import Field, SQLModel, Column, TIMESTAMP, text, Relationship
from typing import Optional, List
from datetime import datetime
from models.task import Task


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