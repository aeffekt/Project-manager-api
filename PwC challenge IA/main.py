from fastapi import FastAPI
from routes import projects

app = FastAPI(tags=["Home"])

# ROUTERS
app.include_router(projects.router)


# HOME
@app.get("/")
async def home():
    return f"Proyect Manager API"