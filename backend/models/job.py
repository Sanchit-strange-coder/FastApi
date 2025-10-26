# Job is going to make an intent to make a story generation task and store it in the database
# Like : inprogress or failed or completed
# frontend -> ask if job is done
# backend -> check job status and return the status to the frontend
# if job is completed then backend return the story to the frontend
from sqlalchemy import JSON, Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.sql import func

from db.database import Base
class StoryJob(Base):
    __tablename__ = "story_jobs"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, unique=True, index=True)
    session_id = Column(String, index=True)
    theme = Column(String)
    status = Column(String, index=True)  # e.g., 'in_progress', 'failed', 'completed'
    story_id = Column(Integer, nullable=True)  # Link to the generated story, if completed
    error = Column(Text, nullable=True)  # Store error message if any
    result = Column(JSON, nullable=True)  # Store the generated story or error message
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    completed_job = Column(DateTime(timezone=True), nullable=True)
    # we use onupdate to update the updated_at field whenever the job is updated