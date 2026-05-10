from fastapi import APIRouter
from app.agents.orchestrator import orchestrator
from app.schemas.channel import PipelineRequest

router = APIRouter(prefix="/pipeline", tags=["pipeline"])


@router.post("/generate-reel")
async def generate_reel(request: PipelineRequest):
    result = await orchestrator.run_reel_pipeline(
        channel_id=request.channel_id,
        niche=request.niche or "fitness",
        topic=request.custom_prompt,
        trend_id=request.trend_id,
    )
    return result


@router.get("/active")
async def get_active_pipelines():
    pipelines = orchestrator.get_active_pipelines()
    return {"pipelines": pipelines, "active_count": len(pipelines)}


@router.get("/{pipeline_id}/status")
async def get_pipeline_status(pipeline_id: str):
    status = orchestrator.get_pipeline_status(pipeline_id)
    if not status:
        return {"error": "Pipeline not found"}
    return status


@router.post("/feedback-loop")
async def run_feedback_loop(request: dict):
    result = await orchestrator.run_feedback_loop(
        channel_id=request.get("channel_id", "default"),
        niche=request.get("niche", "fitness"),
    )
    return result
