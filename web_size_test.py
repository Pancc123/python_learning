from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
print(driver.title)
#driver.find_element_by_id('kw').send_keys('Selenium2')
#driver.find_element_by_id('su').click()
#driver.find_element_by_link_text('新闻').click()
#driver.find_element_by_partial_link_text('新').click()
driver.find_element_by_xpath("//span[@class='bg s_ipt_wr quickdelete-wrap']/input").send_keys('Selenium2')
driver.find_element_by_id('su').click()
time.sleep(30)
#参数数字为像素点
#print("设置浏览器宽480,、高800显示")
#driver.set_window_size(480, 800)
driver.quit()
