from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.implicitly_wait(10)
link = "http://www.google.com"
browser.get(link)
act_1 = browser.find_element_by_name('q')
act_1.send_keys('habr')
act_1.send_keys(Keys.RETURN)
act_2 = browser.find_element_by_css_selector('.LC20lb').click()

all_el_with_class = browser.find_elements(By.XPATH, "//*[@class]")

uniq_classes = set()

for el in all_el_with_class:
    uniq_classes.add(el.get_attribute("class"))
print("all uniques classes: \n", uniq_classes)

