# wai-scraper
Python webscraping library for the [University of Waikato](https://www.waikato.ac.nz/).

Uses [selenium](https://pypi.org/project/selenium/) and 
[selenium-requests](https://pypi.org/project/selenium-requests/) under the hood.

While on campus, the [DUO](https://duo.com/) two-factor authentication does not
prompt the user, which allows using the library in non-interactive mode (`init_driver(False)`).
However, when off-campus, it is necessary to run it in interactive mode (`init_driver(True)`), 
in order to tick the *Remember me for 30 days* box and click on the *Send me a push* button to 
accept the authentication on your mobile device. 

The use of selenium was inspired by:
https://stackoverflow.com/a/23929939/4698227


## Installation

Prepare *npm*

```bash
# create "global" npm installation in home dir
mkdir ~/.npm-global
# add folowing to your ~/.profile
# https://stackoverflow.com/a/49714908/4698227
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
source . ~/.profile
```

Install *npm* and the *Firefox* driver for selenium:

```bash
# install npm:
sudo apt-get install npm
# install firefox driver
npm install -g "geckodriver@<2.0.0"
```

Create a virtual environment:
```bash
virtualenv -p /usr/bin/python3 venv
```

Install *wai.scraper* in the virtual environment: 
```commandline
./venv/bin/pip install git+https://github.com/fracpete/wai-scraper.git
```


## Example

The following example logs into the university website via [SSO](https://en.wikipedia.org/wiki/Single_sign-on) 
and outputs the HTML content of the staff landing page.

```python
import getpass
import wai.scraper as ws

# initialize logger with debugging output
ws.init_logger(True)

# run Firefox in interactive mode (eg when off-campus, for interacting with 2FA) 
driver = ws.init_driver(True)

# perform logins
user = input("Enter user: ")
pw = getpass.getpass("Enter password: ")
ws.sso(driver, user, pw, delay=15)

url = 'https://www.waikato.ac.nz/landing/staff.shtml'

# obtain staff landing page via selenium
ws.driver_get(driver, "staff landing page", url)
print("--> selenium")
print(driver.page_source)

# close the session
ws.close_driver(driver)
```
