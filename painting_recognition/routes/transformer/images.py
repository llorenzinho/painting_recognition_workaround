from painting_recognition.core.DTO import image_dto as dto

from painting_recognition.core.clients import CustomQdrant
from painting_recognition.core.utils import transformers
from painting_recognition.core import logger

import numpy
import io
from PIL import Image

def find_similar(body: dto.ImageSimilarityDTO):
    array = Image.open(io.BytesIO(body.image)).convert('RGB')
    array = numpy.array(array)
    array = transformers.get_embeddings(array)
    db = CustomQdrant()
    return db.search(array, threshold=body.threshold)
    