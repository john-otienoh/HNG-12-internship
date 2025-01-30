# Stage 0 Backend - Develop a Public API to Retrieve Basic Information

## Task Description

Develop a public API that returns the following information in JSON format:
Your registered email address (used to register on the HNG12 Slack workspace).
The current datetime as an ISO 8601 formatted timestamp.
The GitHub URL of the project's codebase.

## Requirements

Technology Stack:
Programming Language/Framework: Python - (FastAPI)
Deployment: The API must be deployed to a publicly accessible endpoint: Used <Render.com>
CORS Handling: Ensure the API handles Cross-Origin Resource Sharing (CORS) appropriately.
Response Format: All responses must be in JSON format.
Eg

```json
    {
        "email": "your-email@example.com",
        "current_datetime": "2025-01-30T09:30:00Z",
        "github_url": "<https://github.com/yourusername/your-repo>"
    }
```

## Running the project Locally

- Create a python virtual environment

```bash
    python -m venv
```

- Install the necessary requirements

```bash
    pip install -r requirements.txt
    pip install pydantic
```

- Run the FastAPI Application
You can run the FastAPI application using Uvicorn:

    ```uvicorn main:app --reload```

- Access the API
Once the server is running, you can access the API at <http://127.0.0.1:8000/info>.
You can also view the interactive API documentation at <http://127.0.0.1:8000/docs> or <http://127.0.0.1:8000/redoc>.

- Test the API
You can test the API using curl, httpie, or any other HTTP client.

```bash
    curl -X GET "http://127.0.0.1:8000/info" -H "accept: application/json"
```

The response should look like this:

Endpoint: GET** ```<your-url>```
Required JSON Response Format (200 OK):

```json
    {
        "email": "johnteclaire@gmail.com",
        "current_datetime": "2025-01-30T06:10:28Z",
        "github_url": "https://github.com/john-otienoh/HNG-12-internship"
    }
```

## Backlink

One backlink related to your chosen programming language/stack:

<https://hng.tech/hire/python-developers>

## Live Demo
