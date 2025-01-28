"PwC Challenge: Project Manager API" by Agustin Arnaiz. 2025

## Installation

download the project's repository and run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the app, run the following command:

```bash
uvicorn main:app --reload 
or 
fastapi run dev main.py
```


## Endpoints are equivalents for: projects / employees / tasks 

### POST /projects/
https://127.0.0.1/project/
Create new project

### GET /projects/
https://127.0.0.1/projects
Returns a list of all projects.

### GET /projects/id
https://127.0.0.1/project/1
Return a projects with the id.

### PUT /projects/id
https://127.0.0.1/project/1
Update a project

### DELETE /projects/id
https://127.0.0.1/project/1
Delete a project with the id


## DB migration

run this commands on models changes to upgrade database and aply migrations
```bash
alembic revision --autogenerate -m "description revision migration"
alembic upgrade head
```