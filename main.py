from fastapi import FastAPI
from routers.v1 import projects

app = FastAPI()


# ROUTERS
app.include_router(projects.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}