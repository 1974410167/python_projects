from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import by

import time

browser = webdriver.Chrome()
browser.get("http://218.29.109.240/eams/loginExt.action;jsessionid=4E0C1D389ACCF74E91A29C7A0E295D6E")

input_name = browser.find_element_by_xpath('//input[@id="username"]')
input_name.send_keys('2018105150124')

input_pass = browser.find_element_by_xpath('//input[@class="pw"]')
input_pass.send_keys('HYuan.5637')

button = browser.find_element_by_xpath('//input[@class="submit"]')
button.click()

pingjiao = browser.find_element_by_xpath("//li//a[@href='/eams/quality/stdEvaluate.action']")
url = pingjiao.get_attribute('href')

browser.get(url)



time.sleep(2)
