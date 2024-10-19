import os
import time

from selenium import webdriver

BASE_PATH = os.path.dirname(__file__)
driver_path = os.path.join(BASE_PATH, 'geckodriver')


# Firefox Browser
browser = webdriver.Firefox(
    executable_path=driver_path)
# browser.get("http://dscrecbijnor.com")


# Chrome Browser
# chromium_driver_path = os.path.join(BASE_PATH, "<path>")
# browser = webdriver.Chrome(executable_path=chromium_driver_path)
# browser.get("http://dscrecbijnor.com")


# Automated google search
url = "https://google.com/"
browser.get(url)
time.sleep(2)
name = 'q'
search_el = browser.find_element_by_name(name)

# print(search_el)
search_el.send_keys("selenium python")
submit_btn_el = browser.find_element_by_css_selector("input[type=submit]")
print(submit_btn_el.get_attribute('name'))
time.sleep(1)
submit_btn_el.click()

# now scrape the content using web scraping
