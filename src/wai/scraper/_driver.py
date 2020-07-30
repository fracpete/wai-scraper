from seleniumrequests import Firefox
from selenium import webdriver
from wai.scraper import logger


def init_driver(debug):
    """
    Initializes the (Firefox) driver.

    :param debug: whether to run in debug mode (ie displaying the browser)
    :type debug: bool
    :return: the driver instance
    :rtype: webdriver.Firefox
    """

    logger().debug("initializing driver (debug=%s)" % str(debug))
    options = webdriver.FirefoxOptions()
    options.headless = not debug
    return Firefox(options=options)


def close_driver(driver):
    """
    Closes the driver.

    :param driver: the driver instance to close
    :type driver: webdriver.Firefox
    """

    logger().debug("closing driver")
    driver.close()


def driver_get(driver, msg, url):
    """
    Uses the driver to access the URL.

    :param driver: the driver instance to use
    :type driver: webdriver.Firefox
    :param msg: the message prefix to use before printing the URL
    :type msg: str
    :param url: the URL to access
    :type url: str
    """

    logger().info(msg + ": " + url)
    driver.get(url)


def requests_get(driver, msg, url):
    """
    Uses requests to access the URL.

    :param driver: the driver instance to use
    :type driver: webdriver.Firefox
    :param msg: the message prefix to use before printing the URL
    :type msg: str
    :param url: the URL to access
    :type url: str
    :return: the requests response
    :rtype: requests.Response
    """

    logger().info(msg + ": " + url)
    return driver.request('GET', url)
