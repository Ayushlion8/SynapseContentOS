from typing import Dict, Any, List
import random
import uuid


class TrendEngine:
    """AI Trend Intelligence Engine — continuously discovers, clusters, and scores emerging trends."""

    def __init__(self):
        self._trends = self._seed_trends()
        self._radar_data = self._generate_radar()

    def _seed_trends(self) -> List[Dict[str, Any]]:
        trend_data = [
            {"name": "AI Voice Cloning Demos", "niche": "tech", "source": "tiktok", "type": "format", "confidence": 0.92, "saturation": 0.48, "opportunity": 0.84, "velocity": 0.89, "growth_24h": 34.2, "growth_7d": 127.5, "status": "rising"},
            {"name": "Silent Workout Routines", "niche": "fitness", "source": "instagram", "type": "sensory", "confidence": 0.88, "saturation": 0.55, "opportunity": 0.78, "velocity": 0.82, "growth_24h": 18.7, "growth_7d": 89.3, "status": "hot"},
            {"name": "30-Second Recipe Hacks", "niche": "food", "source": "tiktok", "type": "format", "confidence": 0.95, "saturation": 0.42, "opportunity": 0.87, "velocity": 0.93, "growth_24h": 42.1, "growth_7d": 156.8, "status": "viral"},
            {"name": "Stoic Morning Routines", "niche": "motivation", "source": "youtube", "type": "theme", "confidence": 0.86, "saturation": 0.51, "opportunity": 0.76, "velocity": 0.74, "growth_24h": 12.3, "growth_7d": 67.2, "status": "rising"},
            {"name": "Passive Income Breakdowns", "niche": "finance", "source": "twitter", "type": "educational", "confidence": 0.83, "saturation": 0.63, "opportunity": 0.69, "velocity": 0.68, "growth_24h": 8.9, "growth_7d": 45.1, "status": "stable"},
            {"name": "Before/After Transformations", "niche": "fitness", "source": "instagram", "type": "visual", "confidence": 0.94, "saturation": 0.61, "opportunity": 0.73, "velocity": 0.87, "growth_24h": 28.4, "growth_7d": 98.6, "status": "hot"},
            {"name": "POV Coding Challenges", "niche": "tech", "source": "tiktok", "type": "format", "confidence": 0.79, "saturation": 0.33, "opportunity": 0.91, "velocity": 0.72, "growth_24h": 56.7, "growth_7d": 203.4, "status": "emerging"},
            {"name": "Micro-Habit Stacking", "niche": "motivation", "source": "reddit", "type": "concept", "confidence": 0.81, "saturation": 0.28, "opportunity": 0.92, "velocity": 0.65, "growth_24h": 67.3, "growth_7d": 189.2, "status": "emerging"},
            {"name": "Budget Meal Prep", "niche": "food", "source": "youtube", "type": "practical", "confidence": 0.87, "saturation": 0.45, "opportunity": 0.80, "velocity": 0.77, "growth_24h": 15.6, "growth_7d": 72.3, "status": "rising"},
            {"name": "Index Fund Explainers", "niche": "finance", "source": "tiktok", "type": "educational", "confidence": 0.90, "saturation": 0.39, "opportunity": 0.85, "velocity": 0.81, "growth_24h": 22.1, "growth_7d": 95.7, "status": "rising"},
            {"name": "Contrarian Hot Takes", "niche": "general", "source": "twitter", "type": "hook_pattern", "confidence": 0.93, "saturation": 0.52, "opportunity": 0.77, "velocity": 0.88, "growth_24h": 31.2, "growth_7d": 112.4, "status": "hot"},
            {"name": "Countdown List Format", "niche": "general", "source": "instagram", "type": "format", "confidence": 0.85, "saturation": 0.58, "opportunity": 0.71, "velocity": 0.73, "growth_24h": 9.8, "growth_7d": 41.2, "status": "stable"},
        ]
        for t in trend_data:
            t["id"] = str(uuid.uuid4())[:8]
            t["viral_hooks"] = [f"Hook pattern {i+1} for {t['name']}" for i in range(3)]
            t["emotional_patterns"] = random.sample(["curiosity", "fear", "aspiration", "urgency", "surprise", "social_proof"], 3)
        return trend_data

    def _generate_radar(self) -> Dict[str, Any]:
        return {
            "axes": ["viral_potential", "saturation_risk", "opportunity_score", "velocity", "confidence", "engagement_lift"],
            "niches": {
                "fitness": [0.82, 0.55, 0.78, 0.87, 0.88, 0.75],
                "tech": [0.79, 0.48, 0.84, 0.72, 0.85, 0.69],
                "motivation": [0.86, 0.51, 0.92, 0.65, 0.81, 0.78],
                "food": [0.95, 0.42, 0.87, 0.93, 0.87, 0.84],
                "finance": [0.83, 0.63, 0.69, 0.68, 0.90, 0.72],
            },
        }

    def get_all_trends(self) -> List[Dict[str, Any]]:
        return self._trends

    def get_trends_by_niche(self, niche: str) -> List[Dict[str, Any]]:
        return [t for t in self._trends if t["niche"] == niche or t["niche"] == "general"]

    def get_trend(self, trend_id: str) -> Dict[str, Any]:
        return next((t for t in self._trends if t["id"] == trend_id), None)

    def get_radar_data(self) -> Dict[str, Any]:
        return self._radar_data

    def get_emerging_trends(self) -> List[Dict[str, Any]]:
        return [t for t in self._trends if t["status"] in ("emerging", "rising")]

    def get_viral_trends(self) -> List[Dict[str, Any]]:
        return [t for t in self._trends if t["status"] in ("viral", "hot")]

    def get_trend_heatmap(self) -> Dict[str, Any]:
        niches = ["fitness", "tech", "motivation", "food", "finance"]
        hours = list(range(24))
        heatmap = {}
        for niche in niches:
            heatmap[niche] = [
                {"hour": h, "engagement_score": round(random.uniform(0.2, 1.0), 2)} for h in hours
            ]
            for h in [6, 7, 8, 12, 18, 19, 20, 21]:
                for entry in heatmap[niche]:
                    if entry["hour"] == h:
                        entry["engagement_score"] = round(random.uniform(0.7, 1.0), 2)
        return heatmap


trend_engine = TrendEngine()
