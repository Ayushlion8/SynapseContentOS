from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from datetime import datetime
import uuid
import time
import json


class BaseAgent(ABC):
    """Base class for all AI agents in the Matiks Content OS."""

    agent_type: str = "base"
    description: str = ""
    dependencies: list[str] = []
    outputs: list[str] = []

    def __init__(self):
        self.run_id = None
        self.model_used = None
        self.tokens_used = 0
        self.start_time = None

    async def execute(self, input_data: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.run_id = str(uuid.uuid4())
        self.start_time = time.time()
        self.model_used = self._select_model(input_data)

        try:
            result = await self._process(input_data, context or {})
            latency_ms = int((time.time() - self.start_time) * 1000)

            return {
                "run_id": self.run_id,
                "agent_type": self.agent_type,
                "status": "completed",
                "output": result,
                "model_used": self.model_used,
                "tokens_used": self.tokens_used,
                "latency_ms": latency_ms,
                "completed_at": datetime.utcnow().isoformat(),
            }
        except Exception as e:
            latency_ms = int((time.time() - self.start_time) * 1000)
            return {
                "run_id": self.run_id,
                "agent_type": self.agent_type,
                "status": "failed",
                "error": str(e),
                "model_used": self.model_used,
                "tokens_used": self.tokens_used,
                "latency_ms": latency_ms,
                "completed_at": datetime.utcnow().isoformat(),
            }

    @abstractmethod
    async def _process(self, input_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def _select_model(self, input_data: Dict[str, Any]) -> str:
        return "gpt-4-turbo"

    def _estimate_tokens(self, text: str) -> int:
        return int(len(text.split()) * 1.3)

    def _build_prompt(self, system: str, user: str) -> str:
        return json.dumps({"system": system, "user": user})
