from selenium import webdriver

#打开Edge浏览器
browser=webdriver.Edge()
#进入淘宝
browser.get("http://www.taobao.com")
#选取节点"q",即淘宝的搜索框
input=browser.find_element_by_id("q")
#在搜索框内输入"iPhone"
input.send_keys("iPhone")
#清空搜索框
input.clear()
#再次输入"iPad"
input.send_keys("iPad")
#模拟点击"搜索"按钮
button=browser.find_element_by_class_name("btn-search")
#最后用click完成搜索动作
button.click()

"""
所有获取单个节点的方法
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
"""

#也可以用通用方法，传入两个参数:查找方式By,和值,但需要额外导入By
from selenium.webdriver.common.by import By
browser1=webdriver.Chrome()
browser1.get("http://www.baidu.com")
input1=browser.find_element(By.ID,"q")
print(input1)
browser1.close()
#此方法更加灵活





