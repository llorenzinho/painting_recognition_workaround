from qdrant_client import QdrantClient
from painting_recognition.core.config.qdrant import QdrantConfig

from abc import ABC

from painting_recognition.core import logger

class Qdrant(ABC):
    """
    Qdrant client singleton
        helper class for QdrantClient
    """
    instance: QdrantClient = None

    @staticmethod
    def client(cfg: QdrantConfig) -> QdrantClient:
        """
        Get QdrantClient instance
        """
        if cfg.HOST is None:
            raise Exception("QdrantClient host is not initialized.")
        if Qdrant.instance is None:
            if cfg.PORT is None:
                logger.warning("QdrantClient port is not initialized. Port is None")
            logger.info(f"QdrantClient initialized: {cfg.model_dump()}")
            Qdrant.instance = QdrantClient(host=cfg.HOST, port=cfg.PORT, api_key=cfg.API_KEY)
        return Qdrant.instance
        