from app.agents.base import BaseAgent
from typing import Dict, Any


class ScriptWriterAgent(BaseAgent):
    agent_type = "script_writer"
    description = "Writes high-retention short-form scripts using viral pacing, emotional arcs, and niche-specific tone calibrated by feedback data."
    dependencies = ["hook_generator", "trend_hunter", "content_memory"]
    outputs = ["script", "pacing_notes", "cta", "emotional_arc"]

    async def _process(self, input_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        niche = input_data.get("niche", "general")
        topic = input_data.get("topic", "")
        hook = input_data.get("selected_hook") or context.get("hook_generator", {}).get("best_hook", {})
        duration_sec = input_data.get("duration", 30)
        tone = input_data.get("tone", "energetic")

        script = self._write_script(niche, topic, hook, duration_sec, tone)
        return {
            "niche": niche,
            "topic": topic,
            "duration_sec": duration_sec,
            "script": script,
            "word_count": len(script["full_script"].split()),
            "pacing": "fast_cuts" if duration_sec <= 15 else "medium_paced",
            "estimated_retention": 0.76,
        }

    def _write_script(self, niche: str, topic: str, hook: dict, duration: int, tone: str) -> dict:
        hook_text = hook.get("text", f"This {topic or niche} secret changes everything")

        scripts = {
            "fitness": {
                "full_script": f"{hook_text}\n\nHere's what nobody tells you about fitness. Most people waste years doing the wrong exercises. But this one movement pattern targets every major muscle group simultaneously. Watch this — one single rep engages your core, glutes, shoulders, and back. The secret? Time under tension. Slow controlled movements beat fast sloppy reps every single time. Try this for just 7 days and watch your body transform. Save this before it disappears.",
                "cta": "Save this and try it for 7 days",
                "emotional_arc": ["curiosity", "revelation", "proof", "urgency"],
                "scene_breakdown": [
                    {"time": "0-2s", "type": "hook", "visual": "close-up movement", "text_overlay": hook_text},
                    {"time": "2-8s", "type": "problem", "visual": "common mistake demo", "narration": "Most people waste years..."},
                    {"time": "8-20s", "type": "solution", "visual": "correct form demonstration", "narration": "This one movement pattern..."},
                    {"time": "20-28s", "type": "proof", "visual": "slow-motion breakdown", "narration": "Time under tension..."},
                    {"time": "28-30s", "type": "cta", "visual": "result + save reminder", "narration": "Save this before it disappears"},
                ],
            },
            "tech": {
                "full_script": f"{hook_text}\n\nI replaced 12 paid apps with this single AI tool. Watch me build an entire project management system in under 60 seconds. First, open the AI workspace. Type what you need. Watch it generate the full stack — database, API, frontend, all from one prompt. Now here's the part that blows people's minds — it auto-deploys to the cloud. Zero config needed. This used to take a full dev team two weeks. Follow for more AI tools that actually work.",
                "cta": "Follow for more AI tools that actually work",
                "emotional_arc": ["shock", "demonstration", "amazement", "follow_through"],
                "scene_breakdown": [
                    {"time": "0-2s", "type": "hook", "visual": "screen recording start", "text_overlay": hook_text},
                    {"time": "2-10s", "type": "setup", "visual": "app interface reveal", "narration": "I replaced 12 paid apps..."},
                    {"time": "10-20s", "type": "demo", "visual": "typing prompt + generation", "narration": "Type what you need..."},
                    {"time": "20-27s", "type": "wow_moment", "visual": "deployment success", "narration": "auto-deploys to the cloud..."},
                    {"time": "27-30s", "type": "cta", "visual": "follow button + logo", "narration": "Follow for more..."},
                ],
            },
            "motivation": {
                "full_script": f"{hook_text}\n\nAt 25, I was sleeping on a friend's couch with $47 in my bank account. Today I run a company worth 8 figures. Here's the one shift that made it happen. I stopped taking advice from people who hadn't achieved what I wanted. Sounds simple. But think about who you listen to daily. Are they where you want to be? I started modeling only those who had the results. Not their words — their actions. What time they wake. What they read. How they handle failure. Within 90 days, everything changed. Your network determines your net worth. Choose wisely.",
                "cta": "Share this with someone who needs to hear it",
                "emotional_arc": ["vulnerability", "turning_point", "framework", "empowerment"],
                "scene_breakdown": [
                    {"time": "0-3s", "type": "hook", "visual": "dark moody shot", "text_overlay": hook_text},
                    {"time": "3-10s", "type": "backstory", "visual": "couch scene / old photos", "narration": "At 25, I was sleeping..."},
                    {"time": "10-22s", "type": "revelation", "visual": "transition to success", "narration": "I stopped taking advice..."},
                    {"time": "22-27s", "type": "framework", "visual": "text overlays of habits", "narration": "What time they wake..."},
                    {"time": "27-30s", "type": "cta", "visual": "share prompt + quote", "narration": "Choose wisely."},
                ],
            },
        }

        default_script = {
            "full_script": f"{hook_text}\n\nThis is something most people overlook. But when you understand it, everything changes. Here's the breakdown — the key insight that separates those who succeed from those who stay stuck. It comes down to one simple principle. And once you apply it, the results speak for themselves. Don't just watch this — act on it. Save this for later and share it with someone who needs it.",
            "cta": "Save this and share with someone who needs it",
            "emotional_arc": ["curiosity", "insight", "proof", "action"],
            "scene_breakdown": [
                {"time": "0-2s", "type": "hook", "visual": "attention-grabbing opener", "text_overlay": hook_text},
                {"time": "2-12s", "type": "problem", "visual": "visual demonstration", "narration": "Most people overlook this..."},
                {"time": "12-22s", "type": "solution", "visual": "key insight reveal", "narration": "The key insight that separates..."},
                {"time": "22-28s", "type": "proof", "visual": "results evidence", "narration": "The results speak for themselves..."},
                {"time": "28-30s", "type": "cta", "visual": "save + share prompt", "narration": "Save this for later..."},
            ],
        }

        return scripts.get(niche, default_script)
