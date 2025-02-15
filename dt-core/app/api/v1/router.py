from fastapi import APIRouter
from app.api.v1.endpoints import dt_crud

v1_router = APIRouter()
v1_router.include_router(dt_crud.router, prefix="/v1", tags = ["CRUD on DT"])