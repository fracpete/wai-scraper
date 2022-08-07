from wai.scraper import driver_get, wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


def sso(driver, user, pw, delay=10):
    """
    Performs the single-sign-on login.

    :param driver: the driver instance to use
    :type driver: webdriver.Firefox
    :param user: the user to use for SSO
    :type user: str
    :param pw: the password to use for SSO
    :type pw: str
    """

    # gets redirected to login page
    driver_get(driver, "sso login", "https://www.waikato.ac.nz/cgi-bin/landing/index.cgi")

    # Login page
    # Fill the login form and submit it
    driver.find_element_by_id('userNameInput').send_keys("waikato.ac.nz\\" + user)
    driver.find_element_by_id('passwordInput').send_keys(pw)
    driver.find_element_by_id('submitButton').send_keys(Keys.RETURN)

    # give 2FA some time to work its magic
    wait("let 2FA finish", delay)


def panopto(driver, delay=5):
    """
    Performs the login to Panopto.

    :param driver: the driver instance to use
    :type driver: webdriver.Firefox
    """

    # log into coursecast
    # TODO this has changed
    driver_get(driver, "panopto login", "https://coursecast.its.waikato.ac.nz/Panopto/Pages/Auth/Login.aspx")
    select = Select(driver.find_element_by_id("providerDropdown"))
    select.select_by_visible_text('elearn')
    submit = driver.find_element_by_id("PageContentPlaceholder_loginControl_externalLoginButton")
    submit.click()

    # give panopto some time
    wait("let panopto finish", delay)
