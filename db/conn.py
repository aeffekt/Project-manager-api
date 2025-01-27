from sqlmodel import SQLModel, create_engine, Session


# Create the SQLite database engine
engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


# Dependency: Get the session
def get_session():
    with Session(engine) as session:
        yield session