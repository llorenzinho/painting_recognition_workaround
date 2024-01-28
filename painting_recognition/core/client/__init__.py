from painting_recognition.core.client.qdrant import Qdrant
from painting_recognition.core.config import app_config

from qdrant_client import QdrantClient

qdrantdb: QdrantClient = Qdrant.client(app_config.qdrant)