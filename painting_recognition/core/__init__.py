import logging
import painting_recognition.core.config as cfg

logging.basicConfig(**cfg.app_config.log.to_dict())
logger = logging.getLogger(__name__)
logger.info('Application config loaded')