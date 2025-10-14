# we have to select the interpreter too by entering interpreter path as uv astral creates a virtual environment and we have to select that interpreter path -> venv/Scripts/python.exe
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #CORS is Cross-Origin Resource Sharing
from core.config import settings
app = FastAPI(
    title="Choose Your Own Adventure API",
    description="An API for a choose your own adventure game.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)
#  we use doc_url and redoc_url to set the paths for the documentation as the fastapi by default sets it to /docs and /redoc but we can change it to anything we want
#  we use title, description and version to set the metadata for the API
#  we use middleware to allow cross-origin requests from the frontend

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],  # Allows all origins
    allow_origins=settings.ALLOWED_ORIGINS
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
# we use allow_origins to allow requests from any origin, we can also specify a list of origins to allow only specific origins as frontend will be running on a different port let suppose 3000 and backend on 8000 so we have to allow requests from frontend port only like allow_origins=["http://localhost:3000"] 
# def main():
#     print("Hello from backend!")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

