from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/explicit_wait2.html')
browser.execute_script("window.scrollBy(0, 150);")
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element_by_id('book').click()
browser.execute_script("window.scrollBy(0, 150);")
wer = browser.find_element_by_id('input_value')
x = wer.text
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
y = calc(x)
baba = browser.find_element_by_css_selector('.form-control')
baba.send_keys(y)
browser.find_element_by_id('solve').click()




