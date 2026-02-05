from fastapi import FastAPI

app = FastAPI(
    title="Campus Marketplace API",
    description="A community marketplace for student dorm residents",
    version="0.1.0",
)


@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
