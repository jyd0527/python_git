import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("tgl0527")
browser.find_element_by_id("pw").send_keys("rhakqtmqslek")


browser.find_element_by_id("log.login").click()

time.sleep(3)

# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")


# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료 
browser.quit()

SCROLL_PAUSE_TIME = 1

while True:
    time.sleep(SCROLL_PAUSE_TIME)
