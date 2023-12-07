from wai.scraper import driver_get, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def sso(driver, user, pw, delay=10):
    """
    Performs the single-sign-on login via DUO.

    :param driver: the driver instance to use
    :type driver: selenium.webdriver.Firefox
    :param user: the user to use for SSO
    :type user: str
    :param pw: the password to use for SSO
    :type pw: str
    :param delay: the number of seconds to wait
    :type delay: int
    """

    # gets redirected to login page
    driver_get(driver, "sso login", "https://elearn.waikato.ac.nz/")

    # Login page
    # Fill the login form and submit it
    driver.find_element(By.ID, 'userNameInput').send_keys("waikato.ac.nz\\" + user)
    driver.find_element(By.ID, 'passwordInput').send_keys(pw)
    driver.find_element(By.ID, 'submitButton').send_keys(Keys.RETURN)

    # give 2FA some time to work its magic
    wait("let 2FA finish", delay)
