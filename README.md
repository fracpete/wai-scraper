# wai-scraper
Python webscraping library for the [University of Waikato](https://www.waikato.ac.nz/).

Uses [selenium](https://pypi.org/project/selenium/) and 
[selenium-requests](https://pypi.org/project/selenium-requests/) under the hood.

While on campus, the [DUO](https://duo.com/) two-factor authentication does not
prompt the user, which allows using the library in non-interactive mode (`init_driver(False)`).
However, when off-campus, it is necessary to run it in interactive mode (`init_driver(True)`), 
in order to tick the *Remember me for 30 days* box and click on the *Send me a push* button to 
accept the authentication on your mobile device. 


## Installation

```commandline
pip install git+https://github.com/fracpete/wai-scraper.git
```


## Example

The following example logs into the university website via [SSO](https://en.wikipedia.org/wiki/Single_sign-on) 
and into [Panopto](https://en.wikipedia.org/wiki/Panopto).
It then retrieves the same URL twice, once via the selenium webdriver and once via 
selenium-requests.

```python
import wai.scraper as ws

# initialize logger with debugging output
ws.init_logger(True)

# run Firefox in interactive mode (eg when off-campus, for interacting with 2FA) 
driver = ws.init_driver(True)

# perform logins
ws.sso(driver, "USER", "PASSWORD", delay=15)
ws.panopto(driver)

url = 'https://coursecast.its.waikato.ac.nz/Panopto/Pages/Sessions/List.aspx#folderID="5ff7fc2a-8b1d-4a37-b222-bc14e92a480f"'

# obtain panopto webpage via selenium
ws.driver_get(driver, "panopto sessions list (driver)", url)
print("--> selenium")
print(driver.page_source)

# obtain panopto webpage via selenium-requests
r = ws.requests_get(driver, "panopto sessions list (requests)", url)
print("--> requests")
print(r.text)

# close the session
ws.close_driver(driver)
```
