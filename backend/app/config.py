from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    app_name: str = "Matiks Content OS"
    app_env: str = "development"
    app_port: int = 8000
    app_host: str = "0.0.0.0"
    debug: bool = True

    database_url: str = "sqlite+aiosqlite:///./matiks.db"
    database_pool_size: int = 20
    database_max_overflow: int = 10

    redis_url: str = "redis://localhost:6379/0"
    celery_broker_url: str = "redis://localhost:6379/1"
    celery_result_backend: str = "redis://localhost:6379/2"

    pinecone_api_key: Optional[str] = None
    pinecone_environment: str = "us-east-1"
    pinecone_index: str = "matiks-content-embeddings"
    weaviate_url: str = "http://localhost:8080"

    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4-turbo"
    anthropic_api_key: Optional[str] = None
    anthropic_model: str = "claude-3-opus-20240229"
    google_api_key: Optional[str] = None
    gemini_model: str = "gemini-1.5-pro"

    elevenlabs_api_key: Optional[str] = None
    elevenlabs_default_voice: str = "rachel"
    elevenlabs_model: str = "eleven_multilingual_v2"

    runway_api_key: Optional[str] = None
    pika_api_key: Optional[str] = None
    replicate_api_token: Optional[str] = None

    analytics_refresh_interval: int = 300
    retention_tracking_enabled: bool = True
    hook_drop_off_tracking: bool = True

    ffmpeg_path: str = "ffmpeg"
    whisper_model: str = "base"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
