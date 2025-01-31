"""
This file defines the FastAPI router for health check and version endpoints
(version 2). It provides basic information about the API, including its name,
description, status, and version.
"""
from fastapi import APIRouter, status
from main import settings

router = APIRouter(prefix="/v2", tags=["v2", "healthcheck", "version"])


@router.get("/health", status_code=status.HTTP_200_OK)
async def healthcheck() -> dict:
    return {
            "name": settings.app_name,            
            "description": "ASYNC API developed for a PwC Challenge by Agustin Arnaiz",
            "status": "ok"
       }


@router.get("/version", status_code=status.HTTP_200_OK)
async def get_version() -> dict:
    return {
                "version": "2.0.0"
            }
