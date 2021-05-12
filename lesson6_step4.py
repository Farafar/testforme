from selenium import webdriver
import requests

import time


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()

browser.get(link)
act1 = browser.find_element_by_css_selector('span.mat-button-wrapper')
act1.click()
act2 = browser.find_element_by_xpath('//div/button')
act2.click()
act3 = browser.find_element_by_css_selector('#username')
act3.send_keys('super')
act4 = browser.find_element_by_css_selector('#mat-input-1')
act4.send_keys('comnetuc484965')
act5 = browser.find_element_by_css_selector('button.mat-raised-button')
act5.click()
time.sleep(5)
act6 = browser.find_element_by_css_selector('#mat-input-2')
act6.send_keys('602')
time.sleep(2)
act7 = browser.find_element_by_xpath('//a[text()="896 (kirya.pecherenko.99@bk.ru)"]')
act7.click()
act8 = browser.find_element_by_css_selector('#896').innerHtml
#act9 = browser.find_element_by_css_selector('#mat-input-5').text
log = act8
print(log)
#pas = act9
#link2 = 'https://hq1.appsflyer.com/auth/login'
#browser.get(link2)
#act10 = Select(browser.find_element_by_css_selector('#user-email.form-control.icon'))
#act10.select_by_value(act8)
#browser.quit()
   # a = str(math.ceil(math.pow(math.pi, math.e)*10000))
    #input0 = browser.find_element_by_partial_link_text(a)
    #input0.click()
    #input1 = browser.find_element_by_css_selector("#mat-input-34")
    #input1.send_keys("328")
    #input2 = browser.find_element_by_name("last_name")
    #input2.send_keys("P")
    #input3 = browser.find_element_by_class_name("form-control.city")
    #input3.send_keys("S")
    #input4 = browser.find_element_by_id("country")
    #input4.send_keys("R")
    #button = browser.find_element_by_xpath('//button[text()="Submit"]')



    #button.click()

#finally:
    # успеваем скопировать код за 30 секунд
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()

while True:
    print(123)