from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic_settings import BaseSettings, SettingsConfigDict


# Pydantic Program settings loading .env file
class Settings(BaseSettings):
    app_name: str = "PwC Challenge"    
    secret_key: str
    db_url: str
    model_config = SettingsConfigDict(env_file=".env")    

# Program settings instance
settings = Settings()

from routers.v1 import projects, employees, tasks, assignments, healthcheck

app = FastAPI()


# ROUTERS
app.include_router(projects.router)
app.include_router(employees.router)
app.include_router(tasks.router)
app.include_router(assignments.router)
app.include_router(healthcheck.router)


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")