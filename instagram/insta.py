import os
import time
import requests
from selenium import webdriver
from conf import INSTA_USERNAME, INSTA_PASSWORD
from urllib.parse import urlparse


browser = webdriver.Chrome()

time.sleep(2)
browser.get("https://instagram.com")

time.sleep(3)
username_el = browser.find_element_by_name('username')
password_el = browser.find_element_by_name('password')

submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")

time.sleep(2)
username_el.send_keys(INSTA_USERNAME)
password_el.send_keys(INSTA_PASSWORD)

time.sleep(2)
submit_btn_el.submit()

time.sleep(5)
not_now_xpath = "//button[contains(text(), 'Not Now')]"
not_now_btn_1 = browser.find_element_by_xpath(not_now_xpath)
browser.execute_script("arguments[0].click();", not_now_btn_1)

time.sleep(5)
not_now_btn_2 = browser.find_element_by_xpath(not_now_xpath)
browser.execute_script("arguments[0].click();", not_now_btn_2)

# my_button_xpath = "//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
# my_button_xpath = "//*[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"

def click_to_follow(browser, url):
  browser.get(url)
  time.sleep(3)
  my_button_xpath = "//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
  follow_btns = browser.find_elements_by_xpath(my_button_xpath)
  for btn in follow_btns:
    time.sleep(2)
    try:
      browser.execute_script("arguments[0].click();", btn)
    except:
      pass


new_user_url = 'https://instagram.com/kallehallden'
time.sleep(3)
click_to_follow(browser, new_user_url)


post_url_pattern = "https://instagram.com/p/<post-slug-id>"
post_xpath_str = "//a[contains(@href, '/p/')]"
time.sleep(3)
post_links = browser.find_elements_by_xpath(post_xpath_str)

post_link = None

if len(post_links) > 0:
  post_link = post_links[0]

if post_link != None:
  time.sleep(2)
  post_href = post_link.get_attribute('href')
  browser.get(post_href)

time.sleep(3)
video_els = browser.find_elements_by_xpath("//video")
image_els = browser.find_elements_by_xpath("//img")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, 'data')
os.makedirs(data_dir, exist_ok=True)


def scrape_and_save(elements):
  if len(elements) > 0:
    for element in elements:
      time.sleep(2)
      url = element.get_attribute('src')
      base_url = urlparse(url).path
      filename = os.path.basename(base_url)
      filepath = os.path.join(data_dir, filename)
      if os.path.exists(filepath):
        continue
      with requests.get(url, stream=True) as r:
        try:
          r.raise_for_status()
        except:
          continue
        with open(filepath, 'wb') as f:
          for chunk in r.iter_content():
            if chunk:
              f.write(chunk)
  
# scrape_and_save(image_els)
# time.sleep(5)
# scrape_and_save(video_els)

def automate_comments(browser, content="Awesome"):
  comment_xpath_str = "//textarea[contains(@placeholder, 'Add a comment')]"
  time.sleep(4)
  comment_el = browser.find_element_by_xpath(comment_xpath_str)
  time.sleep(4)
  try:
    comment_el.send_keys(content)
  except:
    pass  
  time.sleep(2)
  submit_btn = browser.find_element_by_css_selector("button[type='submit']")
  time.sleep(2)
  try:
    submit_btn.submit()
  except:
    pass


automate_comments(browser)


def automate_likes(browser):
  like_heart_svg_xpath = "//*[contains(@aria-label, 'Like')]"
  like_heart_svg_els = browser.find_elements_by_xpath(like_heart_svg_xpath)
  max_height = -1
  for heart_el in like_heart_svg_els:
    h = heart_el.get_attribute('height')
    current_h = int(h)
    if current_h > max_height:
      max_height = current_h
  for heart_el in like_heart_svg_els:
    h = heart_el.get_attribute('height')
    if h == max_height or h == f'{max_height}':
      parent_button = heart_el.find_element_by_xpath("..")
      try:
        browser.execute_script('argument[0].click();', parent_button)
      except:
        pass

automate_likes(browser)