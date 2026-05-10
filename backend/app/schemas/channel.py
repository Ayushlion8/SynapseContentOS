from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ChannelCreate(BaseModel):
    name: str
    handle: str
    niche: str
    avatar_url: Optional[str] = None
    target_reels_per_day: int = 3
    brand_voice: Optional[str] = None
    content_style: Dict[str, Any] = {}
    visual_identity: Dict[str, Any] = {}


class ChannelResponse(BaseModel):
    id: str
    name: str
    handle: str
    niche: str
    avatar_url: Optional[str]
    status: str
    followers: int
    avg_engagement_rate: float
    target_reels_per_day: int
    viral_probability_score: float
    channel_health_score: float
    growth_velocity: float
    momentum_score: float
    ai_strategy: Dict[str, Any]
    best_posting_times: List[Any]
    audience_demographics: Dict[str, Any]
    created_at: datetime

    class Config:
        from_attributes = True


class ChannelHealthResponse(BaseModel):
    channel_id: str
    name: str
    niche: str
    health_score: float
    viral_probability: float
    growth_velocity: float
    momentum: float
    engagement_trend: str
    recommendations: List[str]
    risk_factors: List[str]


class ContentResponse(BaseModel):
    id: str
    channel_id: str
    content_type: str
    niche: str
    status: str
    hook_text: Optional[str]
    script: Optional[str]
    caption: Optional[str]
    hashtags: List[str]
    cta_type: Optional[str]
    video_url: Optional[str]
    thumbnail_url: Optional[str]
    views: int
    likes: int
    comments: int
    shares: int
    saves: int
    avg_watch_time: float
    hook_retention: float
    completion_rate: float
    viral_score: float
    engagement_score: float
    scheduled_at: Optional[datetime]
    published_at: Optional[datetime]
    agent_pipeline_log: List[Dict[str, Any]]
    created_at: datetime

    class Config:
        from_attributes = True


class TrendResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    source: str
    niche: Optional[str]
    trend_type: Optional[str]
    confidence_score: float
    saturation_score: float
    opportunity_score: float
    velocity_score: float
    viral_hooks: List[Any]
    emotional_patterns: List[Any]
    status: str
    growth_rate_24h: float
    growth_rate_7d: float
    detected_at: datetime

    class Config:
        from_attributes = True


class AgentRunResponse(BaseModel):
    id: str
    agent_type: str
    status: str
    channel_id: Optional[str]
    content_id: Optional[str]
    pipeline_id: Optional[str]
    model_used: Optional[str]
    tokens_used: int
    latency_ms: int
    cost_usd: float
    input_data: Dict[str, Any]
    output_data: Dict[str, Any]
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True


class FeedbackSignalResponse(BaseModel):
    id: str
    signal_type: str
    channel_id: str
    content_id: Optional[str]
    metric_name: str
    current_value: float
    previous_value: float
    delta: float
    is_significant: bool
    action_required: bool
    strategy_adjustment: Dict[str, Any]
    affected_agents: List[str]
    adjustment_applied: bool
    detected_at: datetime

    class Config:
        from_attributes = True


class PipelineRequest(BaseModel):
    channel_id: str
    niche: Optional[str] = None
    trend_id: Optional[str] = None
    custom_prompt: Optional[str] = None
    priority: str = "normal"


class PipelineResponse(BaseModel):
    pipeline_id: str
    channel_id: str
    status: str
    stages: List[Dict[str, Any]]
    current_stage: str
    estimated_completion: Optional[datetime]
    created_at: datetime


class KnowledgeGraphResponse(BaseModel):
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]
    clusters: List[Dict[str, Any]]
    stats: Dict[str, Any]


class DashboardStats(BaseModel):
    total_channels: int
    active_channels: int
    total_content_generated: int
    total_content_published: int
    avg_engagement_rate: float
    avg_viral_score: float
    avg_health_score: float
    active_pipelines: int
    active_agents: int
    feedback_signals_24h: int
    trends_detected_24h: int
    total_reach_7d: int
