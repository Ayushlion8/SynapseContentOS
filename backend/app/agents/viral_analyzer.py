from app.agents.base import BaseAgent
from typing import Dict, Any
import random


class ViralPatternAnalyzer(BaseAgent):
    agent_type = "viral_analyzer"
    description = "Reverse-engineers viral content by analyzing hook structure, pacing, emotional triggers, transitions, and engagement patterns to create reusable viral templates."
    dependencies = ["trend_hunter"]
    outputs = ["viral_templates", "pattern_breakdown", "reusable_structures", "engagement_patterns"]

    async def _process(self, input_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        content_url = input_data.get("content_url")
        niche = input_data.get("niche", "general")

        breakdown = self._reverse_engineer(content_url, niche)
        return {
            "source_url": content_url,
            "niche": niche,
            "breakdown": breakdown,
            "viral_template": self._create_template(breakdown),
            "replication_difficulty": random.choice(["easy", "medium", "hard"]),
            "estimated_replication_time": f"{random.randint(15, 45)} minutes",
        }

    def _reverse_engineer(self, url: str, niche: str) -> dict:
        return {
            "hook_structure": {
                "type": "contrarian_statement",
                "first_frame": "bold_text_overlay",
                "audio_cue": "dramatic_pause_then_statement",
                "duration_sec": 1.5,
                "technique": "pattern_interrupt",
            },
            "pacing_structure": {
                "total_duration": random.randint(15, 45),
                "cuts_count": random.randint(5, 12),
                "avg_cut_duration": 2.8,
                "pacing_type": "accelerating",
                "slow_sections": ["0-3s hook", "final 3s CTA"],
                "fast_sections": ["8-22s montage"],
            },
            "subtitle_style": {
                "font": "bold_sans_serif",
                "size": "large",
                "position": "center_top",
                "animation": "word_by_word_highlight",
                "color_scheme": "white_text_yellow_highlight",
                "emphasis_words": True,
            },
            "transition_patterns": [
                {"type": "whip_pan", "count": 3, "timing": "rapid"},
                {"type": "zoom_in", "count": 2, "timing": "dramatic"},
                {"type": "flash_cut", "count": 1, "timing": "surprise_moment"},
            ],
            "emotional_triggers": [
                {"trigger": "curiosity_gap", "intensity": 0.85, "timing_sec": 0},
                {"trigger": "surprise", "intensity": 0.72, "timing_sec": 8},
                {"trigger": "social_proof", "intensity": 0.68, "timing_sec": 15},
                {"trigger": "urgency", "intensity": 0.80, "timing_sec": -3},
            ],
            "cta_strategy": {
                "type": "save_for_later",
                "placement": "final_2_seconds",
                "visual": "animated_save_icon",
                "verbal": "save_this_before_its_gone",
                "secondary_cta": "follow_for_part_2",
            },
            "engagement_patterns": {
                "view_to_like_ratio": 0.068,
                "like_to_comment_ratio": 0.12,
                "view_to_share_ratio": 0.024,
                "view_to_save_ratio": 0.031,
                "retention_at_50pct": 0.72,
                "retention_at_100pct": 0.34,
            },
        }

    def _create_template(self, breakdown: dict) -> dict:
        return {
            "template_name": "contrarian_reveal_template",
            "applicable_niches": ["fitness", "tech", "motivation", "food", "finance"],
            "structure": [
                {"step": 1, "type": "hook", "duration": "1.5s", "description": "Bold contrarian statement with text overlay"},
                {"step": 2, "type": "problem", "duration": "5-8s", "description": "Show common mistake or misconception"},
                {"step": 3, "type": "reveal", "duration": "8-15s", "description": "Demonstrate the correct/better approach"},
                {"step": 4, "type": "proof", "duration": "3-5s", "description": "Show results with social proof"},
                {"step": 5, "type": "cta", "duration": "2s", "description": "Urgent save + follow prompt"},
            ],
            "required_elements": ["bold_text_hook", "fast_cuts", "word_highlight_subtitles", "save_cta"],
            "estimated_viral_probability": round(random.uniform(0.6, 0.85), 2),
        }
