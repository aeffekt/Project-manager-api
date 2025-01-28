from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


# uso de settings en fastapi con dotenv: pip install pydantic-settings
class Settings(BaseSettings):
    app_name: str = "PwC Challenge"    
    secret_key: str
    db_url: str
    model_config = SettingsConfigDict(env_file=".env")    

# Program settings instance
settings = Settings()

from routers.v1 import projects

app = FastAPI()


# ROUTERS
app.include_router(projects.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}