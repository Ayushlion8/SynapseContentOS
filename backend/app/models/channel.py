from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, JSON, Text, Enum as SAEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class ChannelStatus(str, enum.Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    GROWING = "growing"
    DECLINING = "declining"
    NEW = "new"


class Channel(Base):
    __tablename__ = "channels"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    handle = Column(String, unique=True, nullable=False)
    niche = Column(String, nullable=False)
    avatar_url = Column(String)
    status = Column(String, default=ChannelStatus.ACTIVE)

    followers = Column(Integer, default=0)
    following = Column(Integer, default=0)
    posts_count = Column(Integer, default=0)
    avg_engagement_rate = Column(Float, default=0.0)
    avg_reach = Column(Integer, default=0)
    avg_likes = Column(Integer, default=0)
    avg_comments = Column(Integer, default=0)
    avg_shares = Column(Integer, default=0)
    avg_saves = Column(Integer, default=0)

    target_reels_per_day = Column(Integer, default=3)
    content_style = Column(JSON, default=dict)
    brand_voice = Column(Text)
    visual_identity = Column(JSON, default=dict)
    audience_demographics = Column(JSON, default=dict)
    best_posting_times = Column(JSON, default=list)

    viral_probability_score = Column(Float, default=0.0)
    channel_health_score = Column(Float, default=50.0)
    growth_velocity = Column(Float, default=0.0)
    momentum_score = Column(Float, default=0.0)

    ai_strategy = Column(JSON, default=dict)
    feedback_history = Column(JSON, default=list)
    content_memory = Column(JSON, default=dict)
    performance_benchmarks = Column(JSON, default=dict)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    contents = relationship("Content", back_populates="channel", lazy="selectin")
    analytics = relationship("AnalyticsSnapshot", back_populates="channel", lazy="selectin")


class Content(Base):
    __tablename__ = "contents"

    id = Column(String, primary_key=True)
    channel_id = Column(String, nullable=False, index=True)
    content_type = Column(String, default="reel")
    niche = Column(String)
    status = Column(String, default="draft")

    hook_text = Column(Text)
    script = Column(Text)
    caption = Column(Text)
    hashtags = Column(JSON, default=list)
    cta_type = Column(String)
    cta_text = Column(Text)

    video_url = Column(String)
    thumbnail_url = Column(String)
    voiceover_url = Column(String)
    subtitles_url = Column(String)

    scene_plan = Column(JSON, default=list)
    visual_style = Column(JSON, default=dict)
    narration_tone = Column(String)
    pacing_type = Column(String)
    emotional_trigger = Column(String)

    trend_source = Column(String)
    trend_id = Column(String)
    viral_template_id = Column(String)
    ab_test_group = Column(String)

    scheduled_at = Column(DateTime)
    published_at = Column(DateTime)

    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    shares = Column(Integer, default=0)
    saves = Column(Integer, default=0)
    reach = Column(Integer, default=0)

    retention_curve = Column(JSON, default=list)
    avg_watch_time = Column(Float, default=0.0)
    hook_retention = Column(Float, default=0.0)
    completion_rate = Column(Float, default=0.0)
    viral_score = Column(Float, default=0.0)
    engagement_score = Column(Float, default=0.0)

    agent_pipeline_log = Column(JSON, default=list)
    generation_params = Column(JSON, default=dict)
    feedback_applied = Column(JSON, default=list)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    channel = relationship("Channel", back_populates="contents", lazy="selectin")


class AnalyticsSnapshot(Base):
    __tablename__ = "analytics_snapshots"

    id = Column(String, primary_key=True)
    channel_id = Column(String, nullable=False, index=True)
    content_id = Column(String, index=True)

    snapshot_type = Column(String, default="hourly")
    timestamp = Column(DateTime, server_default=func.now())

    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    shares = Column(Integer, default=0)
    saves = Column(Integer, default=0)
    reach = Column(Integer, default=0)
    profile_visits = Column(Integer, default=0)
    website_clicks = Column(Integer, default=0)

    retention_curve = Column(JSON, default=list)
    avg_watch_time = Column(Float, default=0.0)
    hook_drop_off = Column(Float, default=0.0)
    completion_rate = Column(Float, default=0.0)
    audience_retention_by_segment = Column(JSON, default=dict)

    engagement_rate = Column(Float, default=0.0)
    viral_coefficient = Column(Float, default=0.0)
    share_to_view_ratio = Column(Float, default=0.0)
    save_to_view_ratio = Column(Float, default=0.0)

    demographics_snapshot = Column(JSON, default=dict)
    top_regions = Column(JSON, default=list)
    age_distribution = Column(JSON, default=dict)
    gender_split = Column(JSON, default=dict)

    channel = relationship("Channel", back_populates="analytics", lazy="selectin")
