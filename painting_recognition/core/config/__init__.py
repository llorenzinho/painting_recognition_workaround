import os
base_config = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "config"))

from painting_recognition.core.config import log, qdrant
from pydantic_settings import BaseSettings

class AppConfig:
    """
    Settings for application.
    """
    log = log.LogConfig()
    qdrant = qdrant.QdrantConfig()


app_config = AppConfig()