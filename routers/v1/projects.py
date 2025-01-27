from fastapi import APIRouter


router = APIRouter(prefix="/projects", 
                           tags=["projects"]
                           )

@router.get("/")
async def read_projects():
    return {"projects": []}