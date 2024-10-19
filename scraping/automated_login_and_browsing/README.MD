# automated_login_and_browsing

This project is all about automating login to account and browsing the internet, searching the content, scraping the content and saving it to local machine.


## Automated google search and scrape

The file [1_google_bot.py](1_google_bot.py) contains the code for automated google web seaarch

## Intagram Bot

This is a [intagram bot](2_instaBot.py), which will automatically login in to your instagram account and open user's profile and download thier posts. It also provides automated follow, automated like and automated comments

### Setup

1. This project uses the requirements from `requirements.txt` file like - *selenium* , *requests*, etc. install them
2. After installing requirements download the webdriver for your browser
<table><thead><tr><th>Browser</th><th>Supported OS</th><th>Maintained by</th><th>Download</th><th>Issue Tracker</th></tr></thead><tbody><tr><td>Chromium/Chrome</td><td>Windows/macOS/Linux</td><td>Google</td><td><a href="https://chromedriver.storage.googleapis.com/index.html" class="highlight">Downloads</a></td><td><a href="https://bugs.chromium.org/p/chromedriver/issues/list" class="highlight">Issues</a></td></tr><tr><td>Firefox</td><td>Windows/macOS/Linux</td><td>Mozilla</td><td><a href="https://github.com/mozilla/geckodriver/releases" class="highlight">Downloads</a></td><td><a href="https://github.com/mozilla/geckodriver/issues" class="highlight">Issues</a></td></tr><tr><td>Edge</td><td>Windows 10</td><td>Microsoft</td><td><a href="https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/" class="highlight">Downloads</a></td><td><a href="https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/?page=1&amp;q=webdriver" class="highlight">Issues</a></td></tr><tr><td>Internet Explorer</td><td>Windows</td><td>Selenium Project</td><td><a href="https://selenium-release.storage.googleapis.com/index.html" class="highlight">Downloads</a></td><td><a href="https://github.com/SeleniumHQ/selenium/labels/D-IE" class="highlight">Issues</a></td></tr><tr><td>Safari</td><td>macOS El Capitan and newer</td><td>Apple</td><td>Built in</td><td><a href="https://bugreport.apple.com/logon" class="highlight">Issues</a></td></tr><tr><td>Opera</td><td>Windows/macOS/Linux</td><td>Opera</td><td><a href="https://github.com/operasoftware/operachromiumdriver/releases" class="highlight">Downloads</a></td><td><a href="https://github.com/operasoftware/operachromiumdriver/issues" class="highlight">Issues</a></td></tr></tbody></table>


3. Now import webdriver from selenuim package and enjoy

```python
from selenium import webdriver

# if firefox browser
browser = webdriver.Firefox(executable_path=driver_path)

# if chrome browser
browser = webdriver.Chrome(executable_path=chromium_driver_path)

url = "https:https://google.com/"
browser.get(url)
```


### Author

[Kumar Shanu](https:https://its-kumar.herokuapp.com/)
