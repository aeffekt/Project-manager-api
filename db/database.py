"""
This file initializes the SQLModel database and provides a dependency function
to get a database session.  It uses settings from the 'main' module to
configure the database connection path.
"""
from sqlmodel import SQLModel, create_engine, Session
from main import settings


# Create the database engine
engine = create_engine(settings.db_url)

def init_db():
    SQLModel.metadata.create_all(engine)

init_db()

# Dependency: Get the session
def get_session() -> Session:
    with Session(engine) as session:
        yield session
        