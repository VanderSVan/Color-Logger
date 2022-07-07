from pathlib import Path
import logging.config

from settings import logger_config

# create 'logs' folder
current_folder = Path(__file__).parent.absolute()
log_folder = current_folder.joinpath('logs')
log_folder.mkdir(parents=True, exist_ok=True)

logging.config.dictConfig(logger_config)
logger = logging.getLogger('full')

if __name__ == '__main__':
    logger.debug(f"Debug message with level number is {logging.DEBUG}")
    logger.success(f"Success message with level number is {logging.SUCCESS}")
    logger.info(f"Info message with level number is {logging.INFO}")
    logger.warning(f"Warning message with level number is {logging.WARNING}")
    logger.error(f"Error message with level number is {logging.ERROR}")
    logger.exception(f"Exception message with level number is {logging.ERROR}")
    logger.critical(f"Critical message with level number is {logging.CRITICAL}")
