# -- coding: utf-8 --
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import login

resp = int(input('Novo cadastro (1- Sim, 2-Não)?'))


if resp == 1:

    recebeEmail = input('Digite um email:')
    # Variável para receber o path e dar acesso ao google chrome
    driver = webdriver.Chrome(executable_path=r'D:\Programas\chromedriver.exe')

    # get para abrir o navegador e no caso, o chrome
    driver.get(
        "http://automationpractice.com/index.php?controller=authentication&back=my-account")

    # seleção de elementos para manipular o DOM da página web

    driver.find_element_by_id("email_create").send_keys(recebeEmail)

    driver.find_element_by_id("SubmitCreate").click()

    # Todos os "times.sleep's"  foram colocados para evitar bugs na automação dos processos "

    time.sleep(10)

    driver.find_element_by_id("id_gender1").click()

    time.sleep(2)

    driver.find_element_by_id("customer_firstname").send_keys('Joao')
    driver.find_element_by_id("customer_lastname").send_keys('Andrade')
    driver.find_element_by_id("passwd").send_keys('123456')

    time.sleep(2)

    driver.find_element_by_id("days").send_keys('1')
    driver.find_element_by_id("months").send_keys('setembro')
    driver.find_element_by_id("years").send_keys('1994')

    time.sleep(2)

    driver.find_element_by_id("optin").click()
    driver.find_element_by_id("newsletter").click()

    time.sleep(2)

    driver.find_element_by_id("company").send_keys('Mercado Eletronico')
    driver.find_element_by_id("city").send_keys('Sao Paulo')
    driver.find_element_by_id("address1").send_keys('Rua 1')
    driver.find_element_by_id("address2").send_keys('Rua 2')
    driver.find_element_by_id("postcode").send_keys('00000')
    driver.find_element_by_id("id_state").send_keys('Alabama')
    driver.find_element_by_id("phone").send_keys('(11) 1111-1111')
    driver.find_element_by_id("phone_mobile").send_keys('(22) 2 2222-2222')


elif resp == 2:

    recebeEmail = input('Digite um email:')

    # Variável para receber o path e dar acesso ao google chrome
    driver = webdriver.Chrome(executable_path=r'D:\Programas\chromedriver.exe')

    # get para abrir o navegador e no caso, o chrome
    driver.get(
        "http://automationpractice.com/index.php?controller=authentication&back=my-account")

    driver.find_element_by_id("email").send_keys(recebeEmail)
    driver.find_element_by_id("passwd").send_keys('teste')
    driver.find_element_by_id(SubmitLogin).click()
