"""
This file initializes the SQLModel database and provides a dependency function
to get a database session.  It uses settings from the 'main' module to
configure the database connection path.
"""
from sqlmodel import SQLModel, create_engine, Session
from main import settings


# Create the database engine
engine = create_engine(settings.db_url)
SQLModel.metadata.create_all(engine)


# Dependency: Get the session
def get_session():
    with Session(engine) as session:
        yield session
        