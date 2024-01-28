import logging
import painting_recognition.core.config as cfg

logging.basicConfig(**cfg.app_config.log.to_dict())
logger = logging.getLogger(__name__)
logger.info('Application config loaded')
logger.info(cfg.app_config.qdrant.API_KEY)
logger.info(cfg.base_config)