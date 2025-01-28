from sqlmodel import SQLModel, create_engine, Session
from main import settings


# Create the SQLite database engine
engine = create_engine(settings.db_url)
SQLModel.metadata.create_all(engine)


# Dependency: Get the session
def get_session():
    with Session(engine) as session:
        yield session