from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic_settings import BaseSettings, SettingsConfigDict

"""
    This is the entry point of the FastAPI application. It sets up the API routes, 
    initializes the database session, and configures dependencies for the 
    Project Management System.

    Key Features:
    - Manages employees, projects, tasks, and assignments.
    - Provides RESTful endpoints for CRUD operations.
    - Uses SQLModel for database interaction.
    - Supports relationships between entities (employees, tasks, projects).
    - Can integrate with external systems via API.

    Author: Agustin Arnaiz
    Date: 31/01/25
"""

# Pydantic Program settings loading .env file
class Settings(BaseSettings):
    app_name: str = "PwC Challenge"    
    secret_key: str
    db_url: str
    db_async_url: str
    db_password: str
    supabase_key: str
    model_config = SettingsConfigDict(env_file=".env")    

# Program settings instance
settings = Settings()

# This explicit path is for the sake of the challenge, in a real world scenario the .env file should be used
settings.db_url = "postgresql://postgres.ldbzpeddtslywzbsnfqm:Calidad-10@aws-0-us-west-1.pooler.supabase.com:6543/postgres"

from routers.v1 import projects, employees, tasks, assignments, healthcheck

# Official SQLModel about a complete Async functioning is lacking, thats why this routes are not working yet
from routers.v2 import projects_async


app = FastAPI()

# ROUTERS
app.include_router(projects.router)
app.include_router(employees.router)
app.include_router(tasks.router)
app.include_router(assignments.router)
app.include_router(healthcheck.router)

app.include_router(projects_async.router)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")