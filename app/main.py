from fastapi import FastAPI

app = FastAPI(
    title="AI Service",
    description="AI service for the graduation project",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }