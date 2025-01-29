from fastapi import APIRouter, status

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
def healthcheck() -> dict:
    return {"status": "ok"}


@router.get("/version", status_code=status.HTTP_200_OK)
def get_version() -> dict:
    return {"version": "1.0.0"}
