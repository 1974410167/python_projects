from selenium import webdriver
browser=webdriver.Edge()
browser.get("http://www.taobao.com")
with open("taobao.txt","w",encoding="utf-8") as f:
    f.write(browser.page_source)
browser.close()