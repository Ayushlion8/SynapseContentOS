from fastapi import APIRouter
from app.agents.orchestrator import orchestrator
from app.services.channel_manager import channel_manager
import random

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/dashboard")
async def get_analytics_dashboard():
    stats = channel_manager.get_dashboard_stats()
    channels = channel_manager.get_all_channels()

    engagement_over_time = [
        {"date": f"2025-05-{d:02d}", "rate": round(random.uniform(3.5, 7.5), 2)}
        for d in range(1, 11)
    ]

    retention_distribution = [
        {"bucket": "0-2s", "retention": 0.95},
        {"bucket": "2-5s", "retention": 0.72},
        {"bucket": "5-10s", "retention": 0.58},
        {"bucket": "10-20s", "retention": 0.45},
        {"bucket": "20-30s", "retention": 0.35},
        {"bucket": "30s+", "retention": 0.22},
    ]

    feedback_signals = [
        {
            "id": f"fs_{i}",
            "type": random.choice(["retention_drop", "engagement_spike", "audience_shift", "timing_change", "format_shift"]),
            "channel": random.choice(channels)["name"],
            "metric": random.choice(["hook_retention", "completion_rate", "share_rate", "save_rate", "engagement_rate"]),
            "delta": f"+{random.uniform(5, 25):.1f}%" if random.random() > 0.4 else f"-{random.uniform(3, 18):.1f}%",
            "severity": random.choice(["critical", "warning", "info"]),
            "action": random.choice(["auto_adjusted", "pending_review", "escalated"]),
            "time": f"{random.randint(1, 48)}h ago",
        }
        for i in range(15)
    ]

    return {
        **stats,
        "engagement_over_time": engagement_over_time,
        "retention_distribution": retention_distribution,
        "feedback_signals": feedback_signals,
        "ab_experiments": [
            {"id": "exp_1", "name": "Hook Style: Question vs Statement", "status": "running", "winner": "statement", "confidence": 0.87, "sample_size": 240},
            {"id": "exp_2", "name": "Posting Time: 6PM vs 7PM", "status": "running", "winner": "7PM", "confidence": 0.72, "sample_size": 180},
            {"id": "exp_3", "name": "CTA: Save vs Follow", "status": "completed", "winner": "save", "confidence": 0.94, "sample_size": 500},
        ],
    }


@router.get("/feedback-log")
async def get_feedback_log():
    channels = channel_manager.get_all_channels()
    return {
        "recent_adjustments": [
            {
                "id": f"adj_{i}",
                "agent": random.choice(["hook_generator", "script_writer", "scene_planner", "posting_scheduler", "voiceover"]),
                "parameter": random.choice(["hook_duration", "pacing_speed", "tone_strength", "posting_time", "voice_speed"]),
                "old_value": random.choice(["2.0s", "moderate", "6PM", "1.0x"]),
                "new_value": random.choice(["1.0s", "strong", "7PM", "1.1x"]),
                "reason": random.choice([
                    "Retention data shows 23% improvement with shorter hooks",
                    "Opinionated tone drives 89% more shares",
                    "Audience peak shifted 1 hour later",
                    "Faster narration improves completion by 15%",
                ]),
                "auto_applied": True,
                "channel": random.choice(channels)["name"],
                "timestamp": f"2025-05-10T{random.randint(0,23):02d}:{random.randint(0,59):02d}:00Z",
                "confidence": round(random.uniform(0.7, 0.98), 2),
            }
            for i in range(10)
        ]
    }
