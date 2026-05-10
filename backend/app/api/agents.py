from fastapi import APIRouter
from app.agents.orchestrator import orchestrator

router = APIRouter(prefix="/agents", tags=["agents"])


@router.get("/")
async def list_agents():
    agents = orchestrator.get_all_agents()
    return {"agents": agents, "total": len(agents)}


@router.post("/{agent_type}/run")
async def run_agent(agent_type: str, input_data: dict = None):
    if input_data is None:
        input_data = {}
    result = await orchestrator.run_single_agent(agent_type, input_data)
    return result


@router.get("/activity")
async def get_agent_activity():
    agents = orchestrator.get_all_agents()
    activity_log = []
    for agent in agents:
        activity_log.append({
            "agent_type": agent["type"],
            "status": "idle",
            "last_run": "2 minutes ago",
            "runs_today": 12,
            "success_rate": 0.94,
        })
    return {"activity": activity_log}
