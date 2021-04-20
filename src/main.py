# -- coding: utf-8 --

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(
    executable_path=r'D:\Programas\chromedriver.exe')

driver.get(
    "http://automationpractice.com/index.php?controller=authentication&back=my-account")


driver.find_element_by_id("email_create").send_keys(
    "joaovandrade3@gmail.com")

driver.find_element_by_id("SubmitCreate").click()
time.sleep(10)

driver.find_element_by_id("id_gender1").click()

time.sleep(2)

driver.find_element_by_id("customer_firstname").send_keys('Joao')
driver.find_element_by_id("customer_lastname").send_keys('Andrade')
driver.find_element_by_id("passwd").send_keys('123456')
