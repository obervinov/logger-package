"""
This is an additional implementation over the logging module.
This module is designed for fast initialization and configuration of readable and structured logging.
"""
import os
import logging


# Get environment variables values
logger_format = os.environ.get(
    'LOGGER_FORMAT',
    '[%(asctime)s] %(levelname)s [%(logger_name)s:%(funcName)s:%(lineno)d] %(message)s'
)
logger_level = os.environ.get(
    'LOGGER_LEVEL',
    'INFO'
)
logger_date_format = os.environ.get(
    'LOGGER_DATE_FORMAT',
    '%d/%b/%Y %H:%M:%S'
)


# pylint: disable=too-few-public-methods
class ClassNameFilter(logging.Filter):
    """
    This class is used to add the class name and method name to the log output.
    """
    def filter(self, record):
        record.class_name = record.name
        record.method_name = record.funcName
        return True


class CustomFormatter(logging.Formatter):
    """
    This class is an implementation on top of the logging module.
    Contains methods for customizing the log output format and the ability to configure the logger via a yaml file.
    """
    grey = "\x1b[38;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    fmt = logger_format

    FORMATS = {
        logging.DEBUG: grey + fmt + reset,
        logging.INFO: green + fmt + reset,
        logging.WARNING: yellow + fmt + reset,
        logging.ERROR: red + fmt + reset,
        logging.CRITICAL: bold_red + fmt + reset
    }

    def __init__(self, logger_name):
        super().__init__(logger_format, logger_date_format)
        self.logger_name = logger_name

    def format(self, record):
        record.logger_name = self.logger_name
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        formatter.class_name = record.class_name
        formatter.method_name = record.method_name

        return formatter.format(record)


def create_logger(logger_name):
    """
    This function is used to create a logger with a custom format.
    """
    # pylint: disable=redefined-outer-name
    log = logging.getLogger(logger_name)
    log.setLevel(logger_level)
    log.handlers = []
    log.addFilter(ClassNameFilter())
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(CustomFormatter(logger_name))
    log.addHandler(stream_handler)
    return log


log = create_logger(__name__)
