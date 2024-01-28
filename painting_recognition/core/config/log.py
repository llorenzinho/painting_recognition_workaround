import logging

from pydantic_settings import BaseSettings, SettingsConfigDict

import painting_recognition.core.config as config
import os.path as osp

class LogConfig(BaseSettings):
    """
    Settings for logging.
    """
    LEVEL: int = logging.INFO # using logging module constants
    FORMAT: str = '%(asctime)s %(name)s %(levelname)s %(message)s'
    DATE_FORMAT: str = '%Y-%m-%d %H:%M:%S'

    model_config = SettingsConfigDict(
        env_file=osp.join(config.base_config, 'log.env'), env_file_encoding='utf-8', env_prefix='LOG', case_sensitive=True)

    def to_dict(self):
        return {
            'format': self.FORMAT,
            'datefmt': self.DATE_FORMAT,
            'level': self.LEVEL,
        }

