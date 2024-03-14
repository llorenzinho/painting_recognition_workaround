from pydantic import BaseModel, validator
from painting_recognition.core.utils import b64utils

class ImageSimilarityDTO(BaseModel):
    """DTO for image similarity
    """
    image: bytes # base64 converted image
    threshold: float | None = None # min threshold similarity

    @validator('image')
    def validate_base64(cls, v):
        if not b64utils.is_base64(v):
            raise ValueError(f'Image must be base64 encoded. Passed {v}')
        return b64utils.base64_to_bytes(v)
    @validator('threshold')
    def validate_threshold(cls, v):
        if not (v is not None and v >= 0 and v <= 1):
            raise ValueError(f'Threshold must be in range [0, 1]. Passed {v}')
        return v
