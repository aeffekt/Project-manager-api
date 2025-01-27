from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from data.db_connection import Base

# PROJECT table
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="project")

# EMPLOYEE table
class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    position = Column(String, nullable=False)

    assignments = relationship("Assignment", back_populates="employee")

# TASK table
class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)

    project = relationship("Project", back_populates="tasks")
    assignments = relationship("Assignment", back_populates="task")

# ASSIGNMENT table
class Assignment(Base):
    __tablename__ = "assignment"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("task.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)

    task = relationship("Task", back_populates="assignments")
    employee = relationship("Employee", back_populates="assignments")
