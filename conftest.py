"""This module is used to configure the logger"""

import datetime


def pytest_configure(config):
    """Configure the logger"""
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file = f'logs/pytest_logs_{current_time}.log'
    config.option.log_file = log_file
    config.option.log_file_level = 'DEBUG'
    config.option.log_file_format = \
        '%(asctime)s - %(name)s:%(lineno)s - [%(levelname)s] - %(message)s'
    config.option.log_file_date_format = '%Y-%m-%d %H:%M:%S'
