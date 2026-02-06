from fastapi import FastAPI
from app.routes import auth, assessment, insights

app = FastAPI(
    title="MindTrace AI Backend",
    description="Early Cognitive Stress & Burnout Indicator API",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(assessment.router, prefix="/assessment", tags=["Assessment"])
app.include_router(insights.router, prefix="/insights", tags=["Insights"])

@app.get("/")
def health_check():
    return {"status": "MindTrace AI Backend is running"}
