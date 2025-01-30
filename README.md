"PwC Challenge: Project Manager API" by Agustin Arnaiz. 2025

## Installation
download the project's repository and run the following command:

```bash
pip install -r requirements.txt
```


## Requirements
Python 3.10+


## Usage
To run the app, run the following command:

```bash
uvicorn main:app --reload 
or 
fastapi run dev main.py
```

## Endpoints

### Swagger and ReDoc Documentation
http://localhost:8000/          (Redirects to swagger docs)
http://localhost:8000/docs      (Swagger UI)
http://localhost:8000/redoc     (ReDoc)


### Healthcheck & Version check
https://127.0.0.1/health/
https://127.0.0.1/version/


### Endpoints for projects. They replicate for: employees, tasks and assignments

#### POST /projects/
https://127.0.0.1/project/
Create new project

#### GET /projects/
https://127.0.0.1/projects
Returns a list of all projects.

#### GET /projects/id
https://127.0.0.1/project/1
Return a projects with the id.

#### PUT /projects/id
https://127.0.0.1/project/1
Update a project

#### DELETE /projects/id
https://127.0.0.1/project/1
Delete a project with the id


## DB migration with alembic

run this commands on models changes to upgrade database and aply migrations
```bash
alembic revision --autogenerate -m "description revision migration"
alembic upgrade head
```

## Mermaid Diagrams

### [ER Database](https://www.mermaidchart.com/app/projects/8327c60d-192a-473c-8061-60bf1ffbbaa9/diagrams/8b2953d5-01a9-42da-83b9-72d313e7ad5c/version/v0.1/edit)

### [Sequence diagram Integration for assigning tasks to employees](]https://www.mermaidchart.com/app/projects/8327c60d-192a-473c-8061-60bf1ffbbaa9/diagrams/eab6ebab-eab4-442c-bdec-7082544e6353/version/v0.1/edit)