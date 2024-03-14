from transformers import ViTImageProcessor, ViTModel
import torch

from painting_recognition.core.config import app_config

hf = app_config.huggingface

__device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
__processor = ViTImageProcessor.from_pretrained(hf.VISION_TRANSFORMER_MODEL, device=__device)
__model = ViTModel.from_pretrained(hf.VISION_TRANSFORMER_MODEL).to(__device)

def get_embeddings(image) -> torch.Tensor:
    inputs = __processor(images=image, return_tensors="pt").to(__device)
    embedding = __model(**inputs).last_hidden_state[:, 0, :].squeeze()
    return embedding