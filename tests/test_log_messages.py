"""
This test is used to test the log messages.
"""
from logger.logger import log


def test_log_messages():
    """
    This test is used to test the log messages.
    """
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.critical("This is a critical message")
    assert True
