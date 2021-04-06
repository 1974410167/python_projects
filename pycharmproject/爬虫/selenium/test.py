from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import by

import time

browser = webdriver.Chrome()
browser.get("https://www.youtube.com/")
xpath = '/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[2]/a'
current_popular = browser.find_element_by_xpath(xpath)
current_popular.click()

# input_pass = browser.find_element_by_xpath('//input[@class="pw"]')
# input_pass.send_keys('HYuan.5637')
#
# button = browser.find_element_by_xpath('//input[@class="submit"]')
# button.click()
#
# pingjiao = browser.find_element_by_xpath("//li//a[@href='/eams/quality/stdEvaluate.action']")
# url = pingjiao.get_attribute('href')
#
# browser.get(url)