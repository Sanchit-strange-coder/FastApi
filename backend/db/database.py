from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from core.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# we create a function get_db to get a database session and close it after the request is done which prevents to open many connections to the database at the same time

def create_tables():
    import models.story  # Import all models here to register them with SQLAlchemy
    Base.metadata.create_all(bind=engine)
    # we create a function create_tables to create all tables in the database
    # we import all models here to register them with SQLAlchemy and then we create all tables in the database