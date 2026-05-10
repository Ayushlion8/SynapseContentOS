from sqlalchemy import Column, String, Float, DateTime, JSON, Text, Integer, Boolean
from sqlalchemy.sql import func
from app.database import Base


class AgentRun(Base):
    __tablename__ = "agent_runs"

    id = Column(String, primary_key=True)
    agent_type = Column(String, nullable=False, index=True)
    status = Column(String, default="pending")

    input_data = Column(JSON, default=dict)
    output_data = Column(JSON, default=dict)
    error_message = Column(Text)

    channel_id = Column(String, index=True)
    content_id = Column(String, index=True)
    pipeline_id = Column(String, index=True)

    model_used = Column(String)
    tokens_used = Column(Integer, default=0)
    latency_ms = Column(Integer, default=0)
    cost_usd = Column(Float, default=0.0)

    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())


class FeedbackSignal(Base):
    __tablename__ = "feedback_signals"

    id = Column(String, primary_key=True)
    signal_type = Column(String, nullable=False)
    channel_id = Column(String, index=True)
    content_id = Column(String, index=True)

    metric_name = Column(String, nullable=False)
    current_value = Column(Float)
    previous_value = Column(Float)
    delta = Column(Float)
    threshold = Column(Float)

    is_significant = Column(Boolean, default=False)
    action_required = Column(Boolean, default=False)
    strategy_adjustment = Column(JSON, default=dict)

    affected_agents = Column(JSON, default=list)
    adjustment_applied = Column(Boolean, default=False)
    adjustment_result = Column(JSON, default=dict)

    detected_at = Column(DateTime, server_default=func.now())
    resolved_at = Column(DateTime)


class ABExperiment(Base):
    __tablename__ = "ab_experiments"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    experiment_type = Column(String, nullable=False)
    channel_id = Column(String, index=True)

    variants = Column(JSON, default=list)
    metric_to_optimize = Column(String, default="engagement_rate")
    status = Column(String, default="running")

    variant_a_results = Column(JSON, default=dict)
    variant_b_results = Column(JSON, default=dict)
    winner = Column(String)
    confidence_level = Column(Float, default=0.0)

    content_ids = Column(JSON, default=list)
    sample_size = Column(Integer, default=0)

    started_at = Column(DateTime, server_default=func.now())
    ended_at = Column(DateTime)
