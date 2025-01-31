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
http://localhost:8000/          (Redirects to Healthcheck)
http://localhost:8000/docs      (Swagger UI)
http://localhost:8000/redoc     (ReDoc)


### Healthcheck & Version check
https://127.0.0.1/health/
https://127.0.0.1/version/


### Endpoints for V1 "projects". They replicate for: /employees, /tasks and /assignments

#### POST /v1/projects/
https://127.0.0.1/v1/project/
Create new project

#### GET /v1/projects/
https://127.0.0.1/projects?offset=0&limit=10
Returns a list of all projects with query parameter offset and limit for pagination.

#### GET /v1/projects/id
https://127.0.0.1/v1/project/1
Return a projects with the id.

#### PUT /v1/projects/id
https://127.0.0.1/v1/project/1
Update a project

#### DELETE /v1/projects/id
https://127.0.0.1/v1/project/1
Delete a project with the id

### ASYNC Endpoints for V2 "projects". They replicate for: /employees, /tasks and /assignments

#### POST /v2/projects/
https://127.0.0.1/v2/project/
Create new project

#### GET /v2/projects/
https://127.0.0.1/projects?offset=0&limit=10
Returns a list of all projects with query parameter offset and limit for pagination.

#### GET /v2/projects/id
https://127.0.0.1/v2/project/1
Return a projects with the id.

#### PUT /v2/projects/id
https://127.0.0.1/v2/project/1
Update a project

#### DELETE /v2/projects/id
https://127.0.0.1/v2/project/1
Delete a project with the id


## DB migration with alembic
run this commands on models changes to upgrade database and aply migrations
```bash
alembic revision --autogenerate -m "description revision migration"
alembic upgrade head
```

## Dataset online
#### [Link Database in Supabase](https://supabase.com/dashboard/project/ldbzpeddtslywzbsnfqm)


## Mermaid Diagrams

### [ER Database](https://www.mermaidchart.com/raw/8b2953d5-01a9-42da-83b9-72d313e7ad5c?theme=light&version=v0.1&format=svg)

### [Sequence diagram Integration for assigning tasks to employees](https://www.mermaidchart.com/raw/eab6ebab-eab4-442c-bdec-7082544e6353?theme=light&version=v0.1&format=svg)