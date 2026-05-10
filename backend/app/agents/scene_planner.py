from app.agents.base import BaseAgent
from typing import Dict, Any
import random


class ScenePlannerAgent(BaseAgent):
    agent_type = "scene_planner"
    description = "Plans visual scenes and shot compositions based on script emotional arc, generating detailed storyboard with timing, camera angles, and visual references."
    dependencies = ["script_writer", "trend_hunter"]
    outputs = ["scene_plan", "shot_list", "visual_references", "storyboard"]

    async def _process(self, input_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        script_data = context.get("script_writer", {})
        niche = input_data.get("niche", "general")
        duration = input_data.get("duration", 30)

        scene_plan = self._plan_scenes(niche, duration, script_data)
        return {
            "niche": niche,
            "total_scenes": len(scene_plan["scenes"]),
            "scene_plan": scene_plan,
            "visual_style": scene_plan["visual_style"],
            "estimated_visual_complexity": random.choice(["low", "medium", "high"]),
        }

    def _plan_scenes(self, niche: str, duration: int, script_data: dict) -> dict:
        visual_styles = {
            "fitness": {"color_grade": "warm_contrast", "aspect_ratio": "9:16", "text_style": "bold_impact", "transition_style": "whip_cut"},
            "tech": {"color_grade": "cool_blue", "aspect_ratio": "9:16", "text_style": "modern_sleek", "transition_style": "smooth_zoom"},
            "motivation": {"color_grade": "cinematic_moody", "aspect_ratio": "9:16", "text_style": "elegant_serif", "transition_style": "fade_through_black"},
            "food": {"color_grade": "warm_saturated", "aspect_ratio": "9:16", "text_style": "playful_round", "transition_style": "slide_in"},
            "finance": {"color_grade": "dark_professional", "aspect_ratio": "9:16", "text_style": "clean_minimal", "transition_style": "data_transition"},
        }

        scenes = [
            {
                "scene_id": 1,
                "time_range": "0-2s",
                "type": "hook",
                "camera": "extreme_close_up",
                "movement": "slow_push_in",
                "visual_description": "Bold text overlay on dramatic background",
                "duration_sec": 2,
                "overlay_text": "[HOOK TEXT]",
                "emotion": "curiosity",
            },
            {
                "scene_id": 2,
                "time_range": "2-8s",
                "type": "problem_setup",
                "camera": "medium_shot",
                "movement": "static_with_zoom_bump",
                "visual_description": "Show the common mistake or problem",
                "duration_sec": 6,
                "overlay_text": "Most people do THIS...",
                "emotion": "recognition",
            },
            {
                "scene_id": 3,
                "time_range": "8-18s",
                "type": "solution_reveal",
                "camera": "medium_close_up",
                "movement": "dynamic_panning",
                "visual_description": "Demonstrate the correct approach step by step",
                "duration_sec": 10,
                "overlay_text": "Instead, do THIS →",
                "emotion": "revelation",
            },
            {
                "scene_id": 4,
                "time_range": "18-25s",
                "type": "proof_section",
                "camera": "close_up_to_wide",
                "movement": "pull_back_reveal",
                "visual_description": "Show results, testimonials, or data visualization",
                "duration_sec": 7,
                "overlay_text": "The results speak for themselves",
                "emotion": "confidence",
            },
            {
                "scene_id": 5,
                "time_range": "25-30s",
                "type": "cta",
                "camera": "medium_shot",
                "movement": "subtle_ken_burns",
                "visual_description": "Call to action with save/follow prompt",
                "duration_sec": 5,
                "overlay_text": "SAVE THIS + FOLLOW for more",
                "emotion": "urgency",
            },
        ]

        return {
            "visual_style": visual_styles.get(niche, visual_styles["fitness"]),
            "scenes": scenes,
            "total_duration": sum(s["duration_sec"] for s in scenes),
        }
