from sqlalchemy import Column, String, Float, DateTime, JSON, Text, Integer
from sqlalchemy.sql import func
from app.database import Base


class Trend(Base):
    __tablename__ = "trends"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    source = Column(String)
    source_url = Column(String)
    niche = Column(String)

    trend_type = Column(String)
    confidence_score = Column(Float, default=0.0)
    saturation_score = Column(Float, default=0.0)
    opportunity_score = Column(Float, default=0.0)
    velocity_score = Column(Float, default=0.0)

    viral_hooks = Column(JSON, default=list)
    emotional_patterns = Column(JSON, default=list)
    audience_psychology = Column(JSON, default=dict)
    format_patterns = Column(JSON, default=list)

    related_content_ids = Column(JSON, default=list)
    competitor_usage = Column(JSON, default=list)
    embedding_vector_id = Column(String)

    mentions_count = Column(Integer, default=0)
    growth_rate_24h = Column(Float, default=0.0)
    growth_rate_7d = Column(Float, default=0.0)

    status = Column(String, default="emerging")

    detected_at = Column(DateTime, server_default=func.now())
    peak_at = Column(DateTime)
    expires_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class ViralTemplate(Base):
    __tablename__ = "viral_templates"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    source_url = Column(String)
    source_platform = Column(String)

    hook_structure = Column(JSON, default=dict)
    pacing_structure = Column(JSON, default=dict)
    subtitle_style = Column(JSON, default=dict)
    transition_patterns = Column(JSON, default=list)
    emotional_triggers = Column(JSON, default=list)
    cta_strategy = Column(JSON, default=dict)
    scene_breakdown = Column(JSON, default=list)
    engagement_patterns = Column(JSON, default=dict)

    performance_benchmark = Column(JSON, default=dict)
    reuse_count = Column(Integer, default=0)
    avg_viral_score = Column(Float, default=0.0)

    applicable_niches = Column(JSON, default=list)
    embedding_vector_id = Column(String)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class KnowledgeNode(Base):
    __tablename__ = "knowledge_nodes"

    id = Column(String, primary_key=True)
    node_type = Column(String, nullable=False)
    label = Column(String, nullable=False)
    data = Column(JSON, default=dict)

    embedding_vector_id = Column(String)
    cluster_id = Column(String)

    weight = Column(Float, default=1.0)
    access_count = Column(Integer, default=0)
    performance_score = Column(Float, default=0.0)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class KnowledgeEdge(Base):
    __tablename__ = "knowledge_edges"

    id = Column(String, primary_key=True)
    source_id = Column(String, nullable=False, index=True)
    target_id = Column(String, nullable=False, index=True)
    relationship = Column(String, nullable=False)
    weight = Column(Float, default=1.0)
    metadata = Column(JSON, default=dict)

    created_at = Column(DateTime, server_default=func.now())
