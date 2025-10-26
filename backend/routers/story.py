import uuid
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Cookie, Response
from sqlalchemy.orm import Session
from db.database import get_db,SessionLocal
from models.job import StoryJob
from models.story import Story, StoryNode
from schemas.job import StoryJobCreate, StoryJobResponse
from schemas.story import CompleteStoryResponse, CreateStoryRequest, CompleteStoryNodeResponse

router= APIRouter(
    prefix="/story",
    tags=["story"],
)
# we create an APIRouter for story-related endpoints with the prefix /story and tag it as story 
# this helps to organize the endpoints and group them together in the API documentation and routing
# we use the prefix /story so that all endpoints related to story will start with /story
# example: /story/create, /story/{story_id}, etc.


def get_session_id(session_id: Optional[str] = Cookie(None)) -> str:
    if session_id is None:
        session_id = str(uuid.uuid4())
    return session_id
# Session will identify in your browser when we are interacting with the website
# we create a function get_session_id to get the session_id from the cookie
# if the session_id is not present in the cookie, we generate a new UUID and return it

@router.post("/create", response_model=StoryJobResponse)
def create_story(
    request: CreateStoryRequest,
    background_tasks: BackgroundTasks,
    response: Response,
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db),
):
    response.set_cookie(key= "session_id", value=session_id, httponly=True)

    job_id = str(uuid.uuid4())

    job = StoryJob(
        job_id=job_id,
        session_id =session_id,
        theme=request.theme,
        status="pending",
    )
    db.add(job)
    db.commit()
    # we create a new StoryJob with the provided theme and session_id
    # we set the status of the job to pending and add it to the database    

    # TODO: Add background task to generate the story
    return job



