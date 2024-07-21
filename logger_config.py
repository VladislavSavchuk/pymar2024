"""This module is used to configure the logger"""

import datetime
import os
from loguru import logger


def configure_logger(module_name):
    """Create logs directory if it does not exist"""
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Logs file name
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file = f'logs/{current_time}_{module_name}.log'

    # Configure logger
    logger.add(log_file,
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | "
                      "{file}:{line} | {message}",
               level="INFO")
    return logger
