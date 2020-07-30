import time
import logging

_logger = None
""" the global logger instance to use. """


def init_logger(debug):
    """
    Initializes the logging.

    :param debug: whether to use debug level or just info
    :type debug: bool
    """

    global _logger
    logging.basicConfig()
    _logger = logging.getLogger("wai.scraper")
    if debug:
        _logger.setLevel(logging.DEBUG)
    else:
        _logger.setLevel(logging.INFO)


def logger():
    """
    Returns the logger instance.

    :return: the logger
    :rtype: logging.Logger
    """

    if _logger is None:
        init_logger(False)
    return _logger


def wait(msg, seconds):
    """
    Waits for X seconds. Outputs this with a logging message

    :param msg: the message to output
    :type str: str
    :param seconds: the number of seconds to wait
    :type seconds: int
    """

    logger().info("waiting for " + str(seconds) + " seconds:" + msg)
    time.sleep(seconds)
