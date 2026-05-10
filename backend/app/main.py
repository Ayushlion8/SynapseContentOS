from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api import channels, trends, agents, pipeline, knowledge, analytics

app = FastAPI(
    title="Matiks Content OS",
    description="AI-native Content Operating System for multi-channel Instagram management",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(channels.router, prefix="/api")
app.include_router(trends.router, prefix="/api")
app.include_router(agents.router, prefix="/api")
app.include_router(pipeline.router, prefix="/api")
app.include_router(knowledge.router, prefix="/api")
app.include_router(analytics.router, prefix="/api")


@app.get("/")
async def root():
    return {
        "name": settings.app_name,
        "version": "1.0.0",
        "status": "operational",
        "agents_active": 14,
        "endpoints": {
            "channels": "/api/channels",
            "trends": "/api/trends",
            "agents": "/api/agents",
            "pipeline": "/api/pipeline",
            "knowledge": "/api/knowledge",
            "analytics": "/api/analytics",
        },
    }


@app.get("/health")
async def health():
    return {"status": "healthy", "environment": settings.app_env}
