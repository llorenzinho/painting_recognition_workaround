from pydantic_settings import BaseSettings, SettingsConfigDict

import painting_recognition.core.config as config
import os.path as osp

class HuggingfaceConfig(BaseSettings):
    """
    Settings for huggingface.
    """
    VISION_TRANSFORMER_MODEL: str = 'facebook/dino-vits16'
    API_KEY: str | None = None
    
    model_config = SettingsConfigDict(
        env_file=osp.join(config.base_config, 'huggingface.conf'), env_file_encoding='utf-8', env_prefix='HF_', case_sensitive=True) 