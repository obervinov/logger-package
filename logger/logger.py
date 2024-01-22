"""
This is an additional implementation over the logging module.
This module is designed for fast initialization and configuration of readable and structured logging.
"""
import os
import logging


# Get environment variables values
logger_format = os.environ.get(
    'LOGGER_FORMAT',
    '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s'
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
    This сlass is used to add the class name and method name to the log output.
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

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        formatter.class_name = record.class_name
        formatter.method_name = record.method_name

        return formatter.format(record)


logging.basicConfig(
    level=logger_level,
    format=logger_format,
    datefmt=logger_date_format
)

log = logging.getLogger(__name__)
log.handlers = []

log.addFilter(ClassNameFilter())

ch = logging.StreamHandler()
ch.setLevel(logger_level)
ch.setFormatter(CustomFormatter())
log.addHandler(ch)
