import unittest
from selenium import webdriver
browser = webdriver.Chrome()
import time
class Testl6(unittest.TestCase):
    def test_les1(self):

        link = "http://suninjuly.github.io/registration1.html"

        browser.get(link)
        time.sleep(7)
        input1 = browser.find_element_by_class_name('first')
        input1.send_keys('Farid')
        input2 = browser.find_element_by_css_selector('.second[required]')
        input2.send_keys('Azimov')
        input3 = browser.find_element_by_class_name('third')
        input3.send_keys('farid@gmail.com')

        button = browser.find_element_by_class_name('btn-default')
        button.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        time.sleep(3)

    def test_les2(self):
        browser.implicitly_wait(10)
        link = "http://suninjuly.github.io/registration2.html"

        browser.get(link)
        input1 = browser.find_element_by_class_name('first')
        input1.send_keys('Farid')
        input2 = browser.find_element_by_css_selector('.second[required]')
        input2.send_keys('Azimov')
        input3 = browser.find_element_by_class_name('third')
        input3.send_keys('farid@gmail.com')



        button = browser.find_element_by_class_name('btn-default')
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text), f"NoSuchElementException"

if __name__ == "__main__":
    unittest.main()

