"Project Maneger API" with FastAPI by Agustin Arnaiz

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