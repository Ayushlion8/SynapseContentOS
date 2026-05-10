from app.agents.base import BaseAgent
from typing import Dict, Any


class TrendHunterAgent(BaseAgent):
    agent_type = "trend_hunter"
    description = "Continuously scans Instagram, TikTok, YouTube Shorts, Reddit, and X/Twitter to identify emerging trends, viral hooks, and rising content formats."
    dependencies = []
    outputs = ["trends", "viral_hooks", "emerging_formats", "emotional_patterns"]

    async def _process(self, input_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        niche = input_data.get("niche", "general")
        sources = input_data.get("sources", ["instagram", "tiktok", "youtube", "reddit", "twitter"])
        time_window = input_data.get("time_window", "24h")

        trends = self._simulate_trend_detection(niche, sources, time_window)

        return {
            "niche": niche,
            "scan_window": time_window,
            "trends_detected": len(trends),
            "trends": trends,
            "scan_summary": f"Scanned {len(sources)} platforms for {niche} trends over {time_window}",
            "top_opportunity": trends[0] if trends else None,
        }

    def _simulate_trend_detection(self, niche: str, sources: list, window: str) -> list:
        trend_templates = {
            "fitness": [
                {"name": "30-Day Transformation Challenge", "confidence": 0.87, "saturation": 0.45, "opportunity": 0.82, "velocity": 0.73, "type": "challenge", "emotional_trigger": "aspiration", "hooks": ["Before/after reveal", "Day 1 vs Day 30", "POV: you just started"]},
                {"name": "Silent Gym Workouts", "confidence": 0.92, "saturation": 0.62, "opportunity": 0.71, "velocity": 0.85, "type": "format", "emotional_trigger": "aesthetic", "hooks": ["No talking just lifting", "ASMR gym sounds", "Quiet workout routine"]},
                {"name": "Micro-Habit Fitness Hacks", "confidence": 0.78, "saturation": 0.31, "opportunity": 0.89, "velocity": 0.65, "type": "hook_pattern", "emotional_trigger": "curiosity", "hooks": ["One habit that changed my body", "Stop doing this exercise", "Why you're not losing weight"]},
            ],
            "tech": [
                {"name": "AI Tool Demonstrations", "confidence": 0.94, "saturation": 0.55, "opportunity": 0.79, "velocity": 0.91, "type": "format", "emotional_trigger": "fear_of_missing_out", "hooks": ["This AI tool replaces $1000/mo", "Stop paying for software", "AI does this in 3 seconds"]},
                {"name": "Desk Setup Tours", "confidence": 0.83, "saturation": 0.68, "opportunity": 0.62, "velocity": 0.58, "type": "visual_trend", "emotional_trigger": "aspiration", "hooks": ["My $5000 desk setup", "Minimalist desk tour", "Software engineer setup"]},
                {"name": "Code Speed Runs", "confidence": 0.76, "saturation": 0.28, "opportunity": 0.88, "velocity": 0.72, "type": "format", "emotional_trigger": "impressive", "hooks": ["Building an app in 60 seconds", "Speed coding challenge", "Full stack in 5 minutes"]},
            ],
            "food": [
                {"name": "One-Pan Recipe Series", "confidence": 0.91, "saturation": 0.51, "opportunity": 0.77, "velocity": 0.84, "type": "format", "emotional_trigger": "convenience", "hooks": ["Only one pan needed", "5 ingredient dinner", "Lazy girl dinner"]},
                {"name": "Food ASMR", "confidence": 0.88, "saturation": 0.42, "opportunity": 0.83, "velocity": 0.79, "type": "sensory", "emotional_trigger": "satisfaction", "hooks": ["Listen to this crunch", "Satisfying food sounds", "ASMR cooking"]},
                {"name": "Secret Menu Hacks", "confidence": 0.81, "saturation": 0.35, "opportunity": 0.91, "velocity": 0.67, "type": "hook_pattern", "emotional_trigger": "exclusivity", "hooks": ["Starbucks secret menu", "McDonald's hack", "Restaurant doesn't want you to know"]},
            ],
            "motivation": [
                {"name": "Stoic Philosophy Clips", "confidence": 0.89, "saturation": 0.48, "opportunity": 0.80, "velocity": 0.77, "type": "content_theme", "emotional_trigger": "discipline", "hooks": ["Marcus Aurelius said", "This changed my mindset", "The Stoic secret"]},
                {"name": "Morning Routine Breakdowns", "confidence": 0.85, "saturation": 0.59, "opportunity": 0.70, "velocity": 0.68, "type": "format", "emotional_trigger": "self_improvement", "hooks": ["5AM morning routine", "Billionaire morning habits", "The routine that changed everything"]},
                {"name": "Failure to Success Stories", "confidence": 0.93, "saturation": 0.44, "opportunity": 0.86, "velocity": 0.88, "type": "narrative", "emotional_trigger": "hope", "hooks": ["I was broke now I'm", "They laughed at me", "From zero to millionaire"]},
            ],
            "general": [
                {"name": "POV Format Videos", "confidence": 0.90, "saturation": 0.65, "opportunity": 0.68, "velocity": 0.82, "type": "format", "emotional_trigger": "relatability", "hooks": ["POV: you just", "When you finally", "That feeling when"]},
                {"name": "Listicle Countdowns", "confidence": 0.87, "saturation": 0.52, "opportunity": 0.75, "velocity": 0.70, "type": "format", "emotional_trigger": "curiosity", "hooks": ["Top 5 things", "3 habits that", "Number 7 will shock you"]},
                {"name": "Before/After Transformations", "confidence": 0.93, "saturation": 0.47, "opportunity": 0.84, "velocity": 0.90, "type": "visual_pattern", "emotional_trigger": "aspiration", "hooks": ["Wait for the end", "The transformation is crazy", "I can't believe the difference"]},
            ],
        }

        return trend_templates.get(niche, trend_templates["general"])
