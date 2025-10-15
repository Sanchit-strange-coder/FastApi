from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.database import Base

class Story(Base):
    __tablename__ = "stories"
    id = Column(Integer, primary_key=True, index=True)
    # Column is just a piece of data that we will store for any individual story
    title = Column(String, index=True)
    session_id = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    nodes = relationship("StoryNode", back_populates="story", cascade="all, delete-orphan")
    # we use relationship to create a one-to-many relationship between Story and StoryNode
    # back_populates is used to specify the attribute on the related class that will be used to access this relationship
    # cascade is used to specify that when a story is deleted, all its related nodes should also be deleted
    
class StoryNode(Base):
    __tablename__ = "story_nodes"
    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id"), index =True)
    content = Column(Text)
    choices = Column(JSON)  # List of choices leading to other nodes
    is_root = Column(Boolean, default=False)
    is_ending = Column(Boolean, default=False)
    is_winning_ending = Column(Boolean, default=False)
    options = Column(JSON, default=list)  # Additional options for the node
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    story = relationship("Story", back_populates="nodes")
    # we use relationship to create a many-to-one relationship between StoryNode and Story
    # back_populates is used to specify the attribute on the related class that will be used to access this relationship
