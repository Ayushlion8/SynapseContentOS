from fastapi import APIRouter
from app.services.channel_manager import channel_manager

router = APIRouter(prefix="/channels", tags=["channels"])


@router.get("/")
async def list_channels():
    channels = channel_manager.get_all_channels()
    return {"channels": channels, "total": len(channels)}


@router.get("/{channel_id}")
async def get_channel(channel_id: str):
    channel = channel_manager.get_channel(channel_id)
    if not channel:
        return {"error": "Channel not found"}
    return channel


@router.get("/{channel_id}/health")
async def get_channel_health(channel_id: str):
    return channel_manager.get_channel_health(channel_id)


@router.get("/niche/{niche}")
async def get_channels_by_niche(niche: str):
    channels = channel_manager.get_channels_by_niche(niche)
    return {"channels": channels, "niche": niche, "total": len(channels)}


@router.get("/stats/dashboard")
async def get_dashboard_stats():
    return channel_manager.get_dashboard_stats()
