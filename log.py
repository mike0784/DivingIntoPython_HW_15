import logging

logger = logging.getLogger(__name__)

def log_all():
    logger.debug("Подробная информация")
    logger.info("Информация системы")
    logger.warning("Опастность")
    logger.error("Ошибка")
    logger.critical("Критическая ошибка")