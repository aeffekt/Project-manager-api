from fastapi import APIRouter, status
from main import settings

router = APIRouter(prefix="/v1", tags=["v1", "healthcheck", "version"])


@router.get("/health", status_code=status.HTTP_200_OK)
def healthcheck() -> dict:
    return {
            "name": settings.app_name,            
            "description": "API developed for a PwC Challenge by Agustin Arnaiz",
            "status": "ok"
       }


@router.get("/version", status_code=status.HTTP_200_OK)
def get_version() -> dict:
    return {
                "version": "1.0.0"
            }
