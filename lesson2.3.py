from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)
browser.find_element_by_css_selector('.btn').click()
conf = browser.switch_to.alert
conf.accept()
wer = browser.find_element_by_id('input_value')
x = wer.text

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
y = calc(x)
time.sleep(1)
baba = browser.find_element_by_css_selector('.form-control')
baba.send_keys(y)
browser.find_element_by_css_selector('.btn').click()
