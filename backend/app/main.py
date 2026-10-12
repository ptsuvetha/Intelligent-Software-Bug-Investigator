from fastapi import FastAPI
from app.api.routes import investigation

app = FastAPI(
    title="AI Engineering Investigator",
    description="An AI-powered software debugging and investigation system",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "AI Engineering Investigator API is running"
    }


app.include_router(
    investigation.router,
    prefix="/api"
)
