from selenium import webdriver
#初始化Chrome浏览器
browser=webdriver.Chrome()
#初始化Edge浏览器
#browser=webdriver.Edge()
#打开页面，以百度为例
browser.get("http://www.baidu.com")
#输出百度网页源码
print(browser.page_source)
#关闭浏览器
browser.close()