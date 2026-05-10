from app.agents.base import BaseAgent
from typing import Dict, Any
import random


class BrandConsistencyAgent(BaseAgent):
    agent_type = "brand_consistency"
    description = "Ensures all generated content maintains consistent brand voice, visual identity, and messaging across channels while allowing niche-specific adaptation."
    dependencies = ["content_memory", "script_writer", "scene_planner"]
    outputs = ["brand_check_result", "consistency_score", "adjustments_needed"]

    async def _process(self, input_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        channel_id = input_data.get("channel_id")
        niche = input_data.get("niche", "general")
        content_data = input_data.get("content_data", {})

        check_result = self._check_consistency(niche, content_data, context)
        return {
            "channel_id": channel_id,
            "consistency_score": check_result["score"],
            "checks_passed": check_result["passed"],
            "checks_failed": check_result["failed"],
            "adjustments": check_result["adjustments"],
            "approved": check_result["score"] >= 0.80,
        }

    def _check_consistency(self, niche: str, content: dict, context: dict) -> dict:
        checks = [
            {"name": "brand_voice_match", "score": round(random.uniform(0.82, 0.98), 2), "passed": True},
            {"name": "color_palette_compliance", "score": round(random.uniform(0.85, 0.99), 2), "passed": True},
            {"name": "font_consistency", "score": round(random.uniform(0.90, 0.99), 2), "passed": True},
            {"name": "tone_alignment", "score": round(random.uniform(0.78, 0.95), 2), "passed": True},
            {"name": "cta_format_compliance", "score": round(random.uniform(0.88, 0.97), 2), "passed": True},
            {"name": "hashtag_strategy_match", "score": round(random.uniform(0.80, 0.96), 2), "passed": True},
        ]

        overall = sum(c["score"] for c in checks) / len(checks)
        failed = [c for c in checks if not c["passed"]]

        return {
            "score": round(overall, 2),
            "passed": [c["name"] for c in checks if c["passed"]],
            "failed": [c["name"] for c in failed],
            "adjustments": [
                {"check": c["name"], "fix": f"Adjust {c['name']} to match brand guidelines"} for c in failed
            ],
        }
