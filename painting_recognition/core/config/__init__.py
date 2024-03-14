import os
base_config = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "config_files"))

from painting_recognition.core.config import log, qdrant, huggingface
from pydantic import BaseModel

class AppConfig(BaseModel):
    """
    Settings for application.
    """
    __log = log.LogConfig()
    __huggingface = huggingface.HuggingfaceConfig()
    __qdrant = qdrant.QdrantConfig()

    @property
    def log(self):
        return self.__log
    @property
    def qdrant(self):
        return self.__qdrant
    @property
    def huggingface(self):
        return self.__huggingface


app_config = AppConfig()