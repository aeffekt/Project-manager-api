from sqlmodel import Field, SQLModel


class Project(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    start_date: str
    status: str