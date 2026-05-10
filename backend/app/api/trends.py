from fastapi import APIRouter
from app.services.trend_engine import trend_engine

router = APIRouter(prefix="/trends", tags=["trends"])


@router.get("/")
async def list_trends():
    trends = trend_engine.get_all_trends()
    return {"trends": trends, "total": len(trends)}


@router.get("/emerging")
async def get_emerging_trends():
    trends = trend_engine.get_emerging_trends()
    return {"trends": trends, "total": len(trends)}


@router.get("/viral")
async def get_viral_trends():
    trends = trend_engine.get_viral_trends()
    return {"trends": trends, "total": len(trends)}


@router.get("/niche/{niche}")
async def get_trends_by_niche(niche: str):
    trends = trend_engine.get_trends_by_niche(niche)
    return {"trends": trends, "niche": niche, "total": len(trends)}


@router.get("/radar")
async def get_trend_radar():
    return trend_engine.get_radar_data()


@router.get("/heatmap")
async def get_trend_heatmap():
    return trend_engine.get_trend_heatmap()


@router.get("/{trend_id}")
async def get_trend(trend_id: str):
    trend = trend_engine.get_trend(trend_id)
    if not trend:
        return {"error": "Trend not found"}
    return trend
