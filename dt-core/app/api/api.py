from app.api.v1 import router
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware


api_router = APIRouter()
api_router.include_router(router.v1_router)

app = FastAPI(title= "ADT CRUD API",
              description= "Perform CRUD operations on Azure Digital Twin")

app.include_router(api_router)

# CORS middleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
