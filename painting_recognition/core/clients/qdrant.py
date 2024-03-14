from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, VectorParams, Distance
from qdrant_client.http.exceptions import UnexpectedResponse

from painting_recognition.core.config import app_config

from abc import ABC

from painting_recognition.core import logger

cfg = app_config.qdrant

class Qdrant(ABC):
    """
    Qdrant client singleton
        helper class for QdrantClient
    """
    __instance: QdrantClient = None

    @staticmethod
    def client() -> QdrantClient:
        """
        Get QdrantClient instance
        """
        if cfg.HOST is None:
            raise Exception("QdrantClient host is not initialized.")
        if Qdrant.__instance is None:
            if cfg.PORT is None:
                logger.warning("QdrantClient port is not initialized. Port is None")
            logger.debug(f"QdrantClient initialized: {cfg.model_dump()}")
            Qdrant.__instance = QdrantClient(host=cfg.HOST, port=cfg.PORT, api_key=cfg.API_KEY)
        return Qdrant.__instance
    
class CustomQdrant:
    
    def __init__(self,
        host: str = cfg.HOST,
        port: int = cfg.PORT,
        api_key: str = cfg.API_KEY,
        collection: str = cfg.INDEX_NAME
    ):
        self.client = Qdrant.client()
        self.host = host
        self.port = port
        self.api_key = api_key
        self.collection = collection
    
    async def init_collection(self):
        try:
            self.client.create_collection(
                collection_name=cfg.INDEX_NAME,
                vectors_config=VectorParams(size=cfg.VECTOR_SIZE, distance=Distance.COSINE)
            )
        except UnexpectedResponse as e:
            logger.info('Collection already exists, not created')

    def search(self, query_vector: list, limit: int = 1, threshold: float | None = None, query_filter: Filter | None = None):
        return self.client.search(
            collection_name=self.collection,
            query_vector=query_vector,
            limit=limit,
            score_threshold=threshold,
            query_filter=query_filter
        )
        
    

        