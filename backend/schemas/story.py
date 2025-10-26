from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from datetime import datetime


# we create Pydantic schemas to validate and serialize the data for Story and StoryNode
# these schemas will be used in the API endpoints to ensure that the data being sent and received is in the correct format
# Like: { "id": 1, "title": "My Story", "session_id": "abc123", "created_at": "2023-10-01T12:00:00Z", "nodes": [...] } should match the StorySchema the type and structure by Pydantic 
class StoryOptionsSchema(BaseModel):
    text: str
    node_id: Optional[int] = None  # ID of the node this option leads to, if applicable'

class StoryNodeBase(BaseModel):
    content: str
    is_ending: bool = False
    is_winning_ending: bool = False

class CompleteStoryNodeResponse(StoryNodeBase):
    id : int
    options: List[StoryOptionsSchema] = []

    class Config:
        from_attributes = True

class StoryBase(BaseModel):
    title: str
    session_id: Optional[str] = None

    class Config:
        from_attributes = True

class CreateStoryRequest(BaseModel):
    theme: str

class CompleteStoryResponse(StoryBase):
    id :int
    created_at: datetime
    root_node: CompleteStoryNodeResponse
    all_nodes : Dict[int, CompleteStoryNodeResponse]

    class Config:
        from_attributes = True