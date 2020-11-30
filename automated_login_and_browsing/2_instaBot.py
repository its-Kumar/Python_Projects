# Import Libraries
import os
import time
from getpass import getpass
from urllib.parse import urlparse

import requests
from selenium import webdriver

# Set Path for files
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(BASE_PATH, 'geckodriver')

# credientials
username = 'its_yours_kumar'
my_pass = getpass("What is your password?")


# Firefox Browser
browser = webdriver.Firefox(executable_path=driver_path)
url = "https://instagram.com/"
browser.get(url)

# Login
time.sleep(2)
username_el = browser.find_element_by_name("username")
username_el.send_keys(username)

password_el = browser.find_element_by_name("password")
password_el.send_keys(my_pass)

time.sleep(1.5)
submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
submit_btn_el.click()


body_el = browser.find_element_by_css_selector("body")
html_text = body_el.get_attribute("innerHTML")
# print(html_text)
# use webscraping here to scrape html


# Automatic Follow
# follow = browser.find_element_by_css_selector("button")

# xpath
# my_button_xpath = "//button"
# browser.find_element_by_xpath(my_button_xpath)


def click_to_follow(browser):
    my_follow_btn_xpath = "//button[contains(text(), 'Follow')][not (contains(text(), 'Following'))]"
    follow_btn_elements = browser.find_elements_by_xpath(my_follow_btn_xpath)
    for btn in follow_btn_elements:
        time.sleep(2)
        try:
            btn.click()
        except Exception:
            pass


new_user = "https://instagram.com/ted/"
browser.get(new_user)
click_to_follow(browser)


# Scraping content from any post
time.sleep(50)
user_profile_url = "https://www.instagram.com/dscrecbijnor/"
browser.get(user_profile_url)

post_url_pattern = "https://www.instagram.com/p/<post-slug-id>"
post_xpath_str = "//a[contains(@href, '/p/')]"
post_links = browser.find_elements_by_xpath(post_xpath_str)
post_link_el = None

if len(post_links) > 0:
    post_link_el = post_links[0]

if post_link_el is not None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)

video_els = browser.find_elements_by_xpath("//video")
image_els = browser.find_elements_by_xpath("//img")

"""
img_dir = os.path.join(BASE_PATH, "images")
os.makedirs(img_dir, exist_ok=True)
for img in image_els:
    # print(img.get_attribute('src'))
    url = img.get_attribute('src')
    base_url = urlparse(url).path
    filename = os.path.basename(base_url)
    filepath = os.path.join(img_dir, filename)
    with requests.get(url, stream=True) as r:
        try:
            r.raise_for_status()
        except Exception:
            continue
        with open(filepath, "w") as f:
            for chunk in r.iter_content():
                if chunk:
                    f.write(chunk) """


def scrape_and_save(elements):
    data_dir = os.path.join(BASE_PATH, "data")
    os.makedirs(data_dir, exist_ok=True)
    for el in elements:

        url = el.get_attribute('src')
        base_url = urlparse(url).path
        filename = os.path.basename(base_url)
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except Exception:
                continue
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)


scrape_and_save(image_els)
# scrape_and_save(video_els)


# Automatic like and coments on posts
"""
LONG TERM GOAL
Use Machine Learning to classify the post's
image or videos
and then comment in a relative fashion
"""

# automate comment


def automated_comment(browser, content="that's cool!"):
    time.sleep(3)
    comment_xpath_str = "//textarea[contains(@placeholder,  'Add a comment')]"
    comment_el = browser.find_element_by_xpath(comment_xpath_str)
    # print(comment_el)
    comment_el.send_keys(content)
    submit_btns = "button[type='submit']"
    submit_btn_els = browser.find_elements_by_css_selector(submit_btns)
    time.sleep(2)
    for btn in submit_btn_els:
        try:
            btn.click()
        except Exception:
            pass


automated_comment(browser)

# automate like
"""
Like button is actually not a button it's a svg.
"""


def automated_like(browser):
    like_heart_svg_xpath = "//*[contains(@aria-label, 'Like')]"
    all_like_heart_els = browser.find_elements_by_xpath(like_heart_svg_xpath)

    max_heart_h = -1
    for heart_el in all_like_heart_els:
        h = heart_el.get_attribute("height")
        max_heart_h = max(max_heart_h, int(h))

    all_like_heart_els = browser.find_elements_by_xpath(
        like_heart_svg_xpath)
    for heart_el in all_like_heart_els:
        h = heart_el.get_attribute("height")
        # print(h)
        if h == max_heart_h or h == f"{max_heart_h}":
            parent_button = heart_el.find_element_by_xpath('..')
            time.sleep(2)
            try:
                parent_button.click()
            except Exception:
                pass


automated_like(browser)
