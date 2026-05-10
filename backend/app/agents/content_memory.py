from app.agents.base import BaseAgent
from typing import Dict, Any
import random


class ContentMemoryAgent(BaseAgent):
    agent_type = "content_memory"
    description = "Maintains niche-specific memory banks of high-performing hooks, audience psychology, successful formats, and content lineage for cross-channel learning."
    dependencies = ["analytics_feedback"]
    outputs = ["memory_bank", "successful_patterns", "content_lineage", "cross_channel_insights"]

    async def _process(self, input_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        niche = input_data.get("niche", "general")
        channel_id = input_data.get("channel_id")

        memory = self._recall_memory(niche, channel_id)
        return {
            "niche": niche,
            "channel_id": channel_id,
            "memory_bank": memory,
            "cross_channel_insights": self._cross_channel_learn(niche),
            "top_performing_patterns": self._top_patterns(niche),
        }

    def _recall_memory(self, niche: str, channel_id: str) -> dict:
        return {
            "niche_identity": {
                "tone": "confident_and_authoritative",
                "visual_style": "high_contrast_cinematic",
                "narration_pacing": "medium_fast_with_pauses",
                "audience_language": "casual_professional",
                "emotional_profile": "aspirational_with_urgency",
            },
            "top_hooks": [
                {"hook": "Stop doing X like this", "avg_retention": 0.82, "usage_count": 12},
                {"hook": "This one thing changed everything", "avg_retention": 0.78, "usage_count": 8},
                {"hook": "Nobody tells you this about X", "avg_retention": 0.76, "usage_count": 15},
            ],
            "winning_formats": [
                {"format": "contrarian_reveal", "avg_viral_score": 0.71, "success_rate": 0.68},
                {"format": "step_by_step_tutorial", "avg_viral_score": 0.63, "success_rate": 0.72},
                {"format": "before_after_transformation", "avg_viral_score": 0.81, "success_rate": 0.59},
            ],
            "audience_psychology": {
                "primary_motivation": "self_improvement",
                "pain_points": ["lack_of_time", "information_overload", "fear_of_failure"],
                "engagement_triggers": ["social_proof", "expertise_signaling", "exclusivity"],
                "optimal_emotional_arc": "curiosity → problem → revelation → proof → urgency",
            },
            "performance_history": {
                "last_30_days": {"avg_engagement_rate": 5.2, "avg_viral_score": 0.67, "top_content_viral_score": 0.89},
                "trending_up": ["save_rate", "share_rate", "completion_rate"],
                "trending_down": ["hook_retention", "comment_rate"],
            },
        }

    def _cross_channel_learn(self, niche: str) -> list:
        return [
            "Fitness niche hooks work well in motivation niche (67% overlap)",
            "Tech tutorial format adaptable for finance explainers",
            "Food ASMR pacing increases watch time in fitness content by 12%",
        ]

    def _top_patterns(self, niche: str) -> list:
        return [
            {"pattern": "question_hook + visual_proof + save_cta", "success_rate": 0.73},
            {"pattern": "shocking_stat + step_reveal + follow_cta", "success_rate": 0.68},
            {"pattern": "contrarian_open + demo + share_cta", "success_rate": 0.71},
        ]
