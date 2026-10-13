from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import router

# Generates the 'tasks.db' table structure automatically when Uvicorn boots
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

FRONTEND_FILE = Path(__file__).resolve().parent.parent / "frontend" / "index.html"

@app.get("/", include_in_schema=False)
def get_frontend():
    return FileResponse(FRONTEND_FILE)

# Configure CORS Middleware so your frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any frontend domain to access the API during development
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allows all headers
)

# Connects all endpoints isolated in routes.py
app.include_router(router)
