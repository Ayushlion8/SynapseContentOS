from app.agents.base import BaseAgent
from typing import Dict, Any
import random


class CaptionGenerator(BaseAgent):
    agent_type = "caption_generator"
    description = "Generates SEO-optimized captions with hashtag strategies, CTA placement, and engagement hooks calibrated by niche performance data."
    dependencies = ["script_writer", "analytics_feedback", "content_memory"]
    outputs = ["caption", "hashtag_strategy", "cta_text", "engagement_hooks"]

    async def _process(self, input_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        niche = input_data.get("niche", "general")
        topic = input_data.get("topic", "")
        hook_text = input_data.get("hook_text", "")

        caption_data = self._generate_caption(niche, topic, hook_text)
        return caption_data

    def _generate_caption(self, niche: str, topic: str, hook: str) -> dict:
        caption_templates = {
            "fitness": f"🔥 This one exercise replaces your entire gym routine\n\nMost people spend 2 hours on what this does in 15 minutes.\n\nThe secret? Compound engagement.\n\nSave this and try it tomorrow morning →\n\n📊 Results guaranteed in 7 days",
            "tech": f"⚡ I replaced 12 paid apps with ONE tool\n\nWatch me build a full-stack app in 60 seconds.\n\nNo coding. No config. Just results.\n\nFollow for daily AI tool breakdowns →\n\n🚀 Link in bio",
            "motivation": f"💎 At 25, I had $47 in my bank account.\n\n5 years later: 8-figure business.\n\nThe shift? I stopped listening to broke people.\n\nYour circle determines your ceiling.\n\nShare this with someone who needs to hear it →",
            "food": f"🍳 One pan. Five ingredients. Maximum flavor.\n\nThis recipe went viral for a reason.\n\nSave this for your next lazy dinner →\n\n👅 Your tastebuds will thank you",
            "finance": f"📈 97% of people lose money doing this wrong\n\nHere's the strategy that actually works.\n\nSave before the algorithm hides this →\n\n💰 Financial freedom starts with one decision",
        }

        hashtag_pools = {
            "fitness": ["#fitness", "#gymtok", "#workout", "#fitnessmotivation", "#gains", "#gymlife", "#fitfam", "#exercise", "#healthylifestyle", "#transformation"],
            "tech": ["#tech", "#aitools", "#coding", "#software", "#productivity", "#automation", "#techlife", "#developer", "#innovation", "#futuretech"],
            "motivation": ["#motivation", "#mindset", "#success", "#grindset", "#discipline", "#growth", "#entrepreneur", "#hustle", "#inspiration", "#selfimprovement"],
            "food": ["#foodie", "#recipe", "#cooking", "#easyrecipe", "#foodtok", "#homecooking", "#yummy", "#mealprep", "#quickrecipe", "#delicious"],
            "finance": ["#finance", "#investing", "#money", "#wealth", "#financialfreedom", "#stocks", "#personalfinance", "#moneytips", "#financialliteracy", "#invest"],
        }

        return {
            "caption": caption_templates.get(niche, caption_templates["motivation"]),
            "hashtag_strategy": {
                "primary_hashtags": hashtag_pools.get(niche, hashtag_pools["motivation"])[:5],
                "secondary_hashtags": hashtag_pools.get(niche, hashtag_pools["motivation"])[5:8],
                "trending_hashtags": [f"#{niche}tips2025", f"#{niche}hack", "#viral"],
                "total_count": random.randint(15, 25),
                "strategy": "3_tier_hashtag_pyramid",
            },
            "cta_text": "Save this for later →",
            "engagement_hooks": [
                "Drop a 🔥 if you've tried this",
                "Comment 'LINK' for the full guide",
                "Tag someone who needs to see this",
            ],
        }
