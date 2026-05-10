from typing import Dict, Any, List, Optional
import uuid
import random


class ChannelManager:
    """Manages channel data, health scores, and viral probability calculations."""

    def __init__(self):
        self._channels = self._seed_channels()

    def _seed_channels(self) -> List[Dict[str, Any]]:
        niches = [
            ("fitness", "FitMastery", "@fitmastery", "💪"),
            ("tech", "TechVault", "@techvault", "⚡"),
            ("motivation", "MindsetEngine", "@mindsetengine", "🧠"),
            ("food", "FoodLabDaily", "@foodlabdaily", "🍳"),
            ("finance", "WealthArchitect", "@wealtharchitect", "📈"),
            ("fitness", "GymSecrets", "@gymsecrets", "🏋️"),
            ("tech", "AI_Toolbox", "@ai_toolbox", "🤖"),
            ("motivation", "RiseAndGrind", "@riseandgrind", "🔥"),
            ("food", "QuickBites", "@quickbites", "🥘"),
            ("finance", "MoneyMinds", "@moneyminds", "💰"),
            ("lifestyle", "DailyAesthetic", "@dailyaesthetic", "✨"),
            ("fitness", "HomeFitPro", "@homefitpro", "🏃"),
        ]

        channels = []
        for niche, name, handle, emoji in niches:
            ch_id = str(uuid.uuid4())[:8]
            followers = random.randint(5000, 800000)
            channels.append({
                "id": ch_id,
                "name": name,
                "handle": handle,
                "niche": niche,
                "avatar_url": f"/avatars/{ch_id}.png",
                "status": random.choice(["active", "active", "active", "growing", "active"]),
                "emoji": emoji,
                "followers": followers,
                "following": random.randint(100, 2000),
                "posts_count": random.randint(50, 500),
                "avg_engagement_rate": round(random.uniform(2.5, 9.5), 2),
                "avg_reach": random.randint(1000, 500000),
                "avg_likes": random.randint(200, 80000),
                "avg_comments": random.randint(10, 5000),
                "avg_shares": random.randint(5, 2000),
                "avg_saves": random.randint(20, 10000),
                "target_reels_per_day": random.choice([2, 3, 4, 5]),
                "content_style": {"tone": random.choice(["energetic", "calm", "authoritative", "casual"]), "pacing": "fast"},
                "brand_voice": f"Confident {niche} expert with actionable insights",
                "visual_identity": {"color_scheme": "dark_cinematic", "font": "impact"},
                "audience_demographics": {
                    "primary_age": random.choice(["18-24", "25-34", "25-34", "35-44"]),
                    "gender_split": {"male": random.randint(35, 65), "female": random.randint(35, 65)},
                    "top_regions": ["US", "UK", "Canada", "Australia"],
                },
                "best_posting_times": ["6:00 AM", "12:30 PM", "7:00 PM"],
                "viral_probability_score": round(random.uniform(0.3, 0.95), 2),
                "channel_health_score": round(random.uniform(40, 95), 2),
                "growth_velocity": round(random.uniform(-2, 15), 2),
                "momentum_score": round(random.uniform(0.2, 0.95), 2),
                "ai_strategy": {
                    "hook_style": "contrarian",
                    "pacing": "fast_cuts",
                    "cta_type": "save_prompt",
                    "narration_tone": "confident",
                },
                "feedback_history": [],
                "content_memory": {},
                "performance_benchmarks": {
                    "engagement_rate_target": 5.0,
                    "viral_score_target": 0.70,
                    "completion_rate_target": 0.35,
                },
                "created_at": "2025-01-15T08:00:00Z",
                "updated_at": "2025-05-10T12:00:00Z",
            })
        return channels

    def get_all_channels(self) -> List[Dict[str, Any]]:
        return self._channels

    def get_channel(self, channel_id: str) -> Optional[Dict[str, Any]]:
        return next((c for c in self._channels if c["id"] == channel_id), None)

    def get_channels_by_niche(self, niche: str) -> List[Dict[str, Any]]:
        return [c for c in self._channels if c["niche"] == niche]

    def get_channel_health(self, channel_id: str) -> Dict[str, Any]:
        channel = self.get_channel(channel_id)
        if not channel:
            return {"error": "Channel not found"}

        return {
            "channel_id": channel["id"],
            "name": channel["name"],
            "niche": channel["niche"],
            "health_score": channel["channel_health_score"],
            "viral_probability": channel["viral_probability_score"],
            "growth_velocity": channel["growth_velocity"],
            "momentum": channel["momentum_score"],
            "engagement_trend": "up" if channel["growth_velocity"] > 0 else "down",
            "recommendations": self._generate_recommendations(channel),
            "risk_factors": self._identify_risks(channel),
        }

    def _generate_recommendations(self, channel: Dict) -> List[str]:
        recs = []
        if channel["avg_engagement_rate"] < 4.0:
            recs.append("Engagement rate below niche average — strengthen hooks and CTAs")
        if channel["viral_probability_score"] < 0.5:
            recs.append("Low viral probability — incorporate trending formats and audio")
        if channel["growth_velocity"] < 1:
            recs.append("Stagnant growth — increase posting frequency and test new content formats")
        if channel["target_reels_per_day"] < 3:
            recs.append("Increase reels per day to at least 3 for optimal algorithm exposure")
        return recs or ["Channel performing well — maintain current strategy and iterate"]

    def _identify_risks(self, channel: Dict) -> List[str]:
        risks = []
        if channel["channel_health_score"] < 50:
            risks.append("Critical health score — immediate strategy overhaul recommended")
        if channel["growth_velocity"] < -1:
            risks.append("Negative growth velocity — audience churn detected")
        return risks

    def get_dashboard_stats(self) -> Dict[str, Any]:
        channels = self._channels
        return {
            "total_channels": len(channels),
            "active_channels": len([c for c in channels if c["status"] == "active"]),
            "total_followers": sum(c["followers"] for c in channels),
            "avg_engagement_rate": round(sum(c["avg_engagement_rate"] for c in channels) / len(channels), 2),
            "avg_viral_score": round(sum(c["viral_probability_score"] for c in channels) / len(channels), 2),
            "avg_health_score": round(sum(c["channel_health_score"] for c in channels) / len(channels), 2),
            "total_target_reels_daily": sum(c["target_reels_per_day"] for c in channels),
            "niches_active": len(set(c["niche"] for c in channels)),
            "top_performing_niche": max(set(c["niche"] for c in channels), key=lambda n: sum(ch["avg_engagement_rate"] for ch in channels if ch["niche"] == n) / len([ch for ch in channels if ch["niche"] == n])),
        }


channel_manager = ChannelManager()
