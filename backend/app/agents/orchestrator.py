from typing import Dict, Any, Optional, List
from datetime import datetime
import uuid
import asyncio

from app.agents.trend_hunter import TrendHunterAgent
from app.agents.competitor_intel import CompetitorIntelligenceAgent
from app.agents.hook_generator import HookGeneratorAgent
from app.agents.script_writer import ScriptWriterAgent
from app.agents.viral_analyzer import ViralPatternAnalyzer
from app.agents.voiceover import VoiceoverAgent
from app.agents.scene_planner import ScenePlannerAgent
from app.agents.video_generator import VideoGenerationAgent
from app.agents.thumbnail_optimizer import ThumbnailOptimizer
from app.agents.caption_generator import CaptionGenerator
from app.agents.posting_scheduler import PostingScheduler
from app.agents.analytics_feedback import AnalyticsFeedbackAgent
from app.agents.content_memory import ContentMemoryAgent
from app.agents.brand_consistency import BrandConsistencyAgent


AGENT_REGISTRY = {
    "trend_hunter": TrendHunterAgent,
    "competitor_intel": CompetitorIntelligenceAgent,
    "hook_generator": HookGeneratorAgent,
    "script_writer": ScriptWriterAgent,
    "viral_analyzer": ViralPatternAnalyzer,
    "voiceover": VoiceoverAgent,
    "scene_planner": ScenePlannerAgent,
    "video_generator": VideoGenerationAgent,
    "thumbnail_optimizer": ThumbnailOptimizer,
    "caption_generator": CaptionGenerator,
    "posting_scheduler": PostingScheduler,
    "analytics_feedback": AnalyticsFeedbackAgent,
    "content_memory": ContentMemoryAgent,
    "brand_consistency": BrandConsistencyAgent,
}

REEL_PIPELINE_STAGES = [
    {
        "stage": 1,
        "name": "Trend Discovery",
        "agents": ["trend_hunter", "competitor_intel", "content_memory"],
        "parallel": True,
    },
    {
        "stage": 2,
        "name": "Content Strategy",
        "agents": ["analytics_feedback", "viral_analyzer"],
        "parallel": True,
    },
    {
        "stage": 3,
        "name": "Creative Generation",
        "agents": ["hook_generator", "script_writer"],
        "parallel": False,
    },
    {
        "stage": 4,
        "name": "Production",
        "agents": ["scene_planner", "voiceover", "brand_consistency"],
        "parallel": True,
    },
    {
        "stage": 5,
        "name": "Video Assembly",
        "agents": ["video_generator", "thumbnail_optimizer"],
        "parallel": False,
    },
    {
        "stage": 6,
        "name": "Publishing",
        "agents": ["caption_generator", "posting_scheduler"],
        "parallel": True,
    },
]


class AgentOrchestrator:
    """Orchestrates multi-agent pipelines for the Matiks Content OS."""

    def __init__(self):
        self.agents = {name: cls() for name, cls in AGENT_REGISTRY.items()}
        self.active_pipelines: Dict[str, Dict] = {}

    def get_agent(self, agent_type: str):
        return self.agents.get(agent_type)

    def get_all_agents(self) -> List[Dict[str, Any]]:
        return [
            {
                "type": name,
                "description": agent.description,
                "dependencies": agent.dependencies,
                "outputs": agent.outputs,
                "status": "idle",
            }
            for name, agent in self.agents.items()
        ]

    async def run_single_agent(self, agent_type: str, input_data: Dict[str, Any], context: Optional[Dict] = None) -> Dict[str, Any]:
        agent = self.agents.get(agent_type)
        if not agent:
            return {"error": f"Agent {agent_type} not found"}
        return await agent.execute(input_data, context or {})

    async def run_reel_pipeline(self, channel_id: str, niche: str, topic: Optional[str] = None, trend_id: Optional[str] = None) -> Dict[str, Any]:
        pipeline_id = str(uuid.uuid4())
        pipeline_context = {}
        pipeline_log = []
        pipeline_start = datetime.utcnow()

        self.active_pipelines[pipeline_id] = {
            "id": pipeline_id,
            "channel_id": channel_id,
            "niche": niche,
            "status": "running",
            "current_stage": 0,
            "stages": [],
            "started_at": pipeline_start.isoformat(),
        }

        base_input = {
            "channel_id": channel_id,
            "niche": niche,
            "topic": topic or niche,
            "trend_id": trend_id,
        }

        for stage_config in REEL_PIPELINE_STAGES:
            stage_num = stage_config["stage"]
            stage_name = stage_config["name"]
            agent_names = stage_config["agents"]
            parallel = stage_config["parallel"]

            stage_start = datetime.utcnow()
            stage_results = {}

            if parallel:
                tasks = []
                for agent_name in agent_names:
                    agent_input = {**base_input, **pipeline_context.get(agent_name, {})}
                    tasks.append(self.run_single_agent(agent_name, agent_input, pipeline_context))
                results = await asyncio.gather(*tasks, return_exceptions=True)
                for agent_name, result in zip(agent_names, results):
                    if isinstance(result, Exception):
                        stage_results[agent_name] = {"status": "failed", "error": str(result)}
                    else:
                        stage_results[agent_name] = result
                        pipeline_context[agent_name] = result.get("output", {})
            else:
                for agent_name in agent_names:
                    agent_input = {**base_input, **pipeline_context.get(agent_name, {})}
                    result = await self.run_single_agent(agent_name, agent_input, pipeline_context)
                    stage_results[agent_name] = result
                    pipeline_context[agent_name] = result.get("output", {})

            stage_duration = (datetime.utcnow() - stage_start).total_seconds()
            pipeline_log.append({
                "stage": stage_num,
                "name": stage_name,
                "agents": agent_names,
                "results": stage_results,
                "duration_sec": stage_duration,
                "completed_at": datetime.utcnow().isoformat(),
            })

            self.active_pipelines[pipeline_id]["current_stage"] = stage_num
            self.active_pipelines[pipeline_id]["stages"].append({
                "stage": stage_num,
                "name": stage_name,
                "status": "completed",
                "duration_sec": stage_duration,
            })

        total_duration = (datetime.utcnow() - pipeline_start).total_seconds()
        self.active_pipelines[pipeline_id]["status"] = "completed"
        self.active_pipelines[pipeline_id]["completed_at"] = datetime.utcnow().isoformat()

        return {
            "pipeline_id": pipeline_id,
            "channel_id": channel_id,
            "niche": niche,
            "status": "completed",
            "stages_completed": len(REEL_PIPELINE_STAGES),
            "total_duration_sec": total_duration,
            "pipeline_log": pipeline_log,
            "context": pipeline_context,
            "generated_content": {
                "hook": pipeline_context.get("hook_generator", {}).get("best_hook"),
                "script": pipeline_context.get("script_writer", {}),
                "scene_plan": pipeline_context.get("scene_planner", {}),
                "voiceover": pipeline_context.get("voiceover", {}),
                "video": pipeline_context.get("video_generator", {}),
                "thumbnail": pipeline_context.get("thumbnail_optimizer", {}),
                "caption": pipeline_context.get("caption_generator", {}),
                "schedule": pipeline_context.get("posting_scheduler", {}),
                "feedback": pipeline_context.get("analytics_feedback", {}),
            },
        }

    def get_pipeline_status(self, pipeline_id: str) -> Optional[Dict]:
        return self.active_pipelines.get(pipeline_id)

    def get_active_pipelines(self) -> List[Dict]:
        return list(self.active_pipelines.values())

    async def run_feedback_loop(self, channel_id: str, niche: str) -> Dict[str, Any]:
        feedback_agent = self.agents["analytics_feedback"]
        memory_agent = self.agents["content_memory"]

        feedback_result = await feedback_agent.execute({"channel_id": channel_id, "niche": niche, "lookback_days": 30})
        memory_result = await memory_agent.execute({"channel_id": channel_id, "niche": niche})

        return {
            "channel_id": channel_id,
            "feedback_signals": feedback_result.get("output", {}),
            "memory_state": memory_result.get("output", {}),
            "adjustments_applied": feedback_result.get("output", {}).get("strategy_adjustments", []),
            "self_improvement_summary": feedback_result.get("output", {}).get("self_improvement_summary", ""),
        }


orchestrator = AgentOrchestrator()
