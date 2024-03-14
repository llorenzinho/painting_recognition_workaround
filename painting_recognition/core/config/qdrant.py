from pydantic_settings import BaseSettings, SettingsConfigDict

import painting_recognition.core.config as config
import os.path as osp

class QdrantConfig(BaseSettings):
    """
    Settings for qdrant.
    """
    HOST: str = 'localhost'
    PORT: int = 6333
    API_KEY: str | None = None
    INDEX_NAME: str | None = None
    VECTOR_SIZE: int = 384

    
    model_config = SettingsConfigDict(
        env_file=osp.join(config.base_config, 'qdrant.conf'), env_file_encoding='utf-8', env_prefix='QDRANT_', case_sensitive=True) 