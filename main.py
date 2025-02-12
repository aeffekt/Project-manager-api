"""
    This is the entry point of the FastAPI application. It sets up the API routes, 
    initializes the database session, and configures dependencies for the 
    Project Management System.

    Key Features:
    - Manages employees, projects, tasks, and assignments.
    - Provides RESTful endpoints for CRUD operations.
    - Uses SQLModel for database interaction.    
    - Can integrate with external systems via API.
    - v1 for sync API and v2 for async API.
    - alembic for database migrations.

    Author: Agustin Arnaiz
    Date: 31/01/25
"""
from fastapi import FastAPI
import importlib
from fastapi.responses import RedirectResponse
from pydantic_settings import BaseSettings, SettingsConfigDict


# Pydantic Program settings loading .env file
class Settings(BaseSettings):
    app_name: str = "Project Manager API"    
    db_url: str
    db_async_url: str    
    supabase_key: str
    model_config = SettingsConfigDict(env_file=".env")    

# Program settings instance
settings = Settings()

app = FastAPI()

# Modules for each version
versions = {
    "v1": ["projects", "employees", "tasks", "assignments", "healthcheck"],
    "v2": ["projects", "employees", "tasks", "assignments", "healthcheck"],
}

# Dynamic import for the routers
for version, modules in versions.items():
    for module in modules:
        module_name = f"api.{version}.routers.{module}"
        router_module = importlib.import_module(module_name)
        app.include_router(router_module.router)


@app.get("/")
def read_root():
    return RedirectResponse(url="v2/health")