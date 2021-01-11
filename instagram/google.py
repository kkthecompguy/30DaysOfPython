import time
from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://google.com/'

time.sleep(2)
browser.get(url)

search_el = browser.find_element_by_name('q')

time.sleep(2)
search_el.send_keys("Selenium python")

submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
time.sleep(2)
submit_btn_el.submit()