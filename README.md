# AI Service

AI service for the Children's Mental Health
and Behavior Modification Graduation Project.

## Technologies
- Python
- FastAPI
- Uvicorn

## Installation

pip install -r requirements.txt

## Run the Server

uvicorn app.main:app --reload

## Health Check

GET /health

Response:
{
    "status": "ok"
}
