# -- coding: utf-8 --

# Importações de bibliotecas conforme suas necessidades

import time
import json
import os
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Campos para fazer a importação do Json

with open('C:/Users/João Andrade/OneDrive/Documentos/loginRegister/src/usuarioCadastro.json') as f:
    userCadastro = json.load(f)

with open('C:/Users/João Andrade/OneDrive/Documentos/loginRegister/src/usuarioLogin.json') as s:
    userLogin = json.load(s)


# Conexão com banco de dados local

conDb = mysql.connector.connect(
    host='localhost',
    database='bd_loginregister',
    user='root',
    password='CcO21377@')

if conDb.is_connected():
    dbInfos = conDb.get_server_info()

    cursor = conDb.cursor()
    cursor.execute("select database();")

    recebeDb = cursor.fetchone()

resp = int(input('Novo cadastro? 1- Sim 2-Não \nR:'))

# Menu de interação com usuario

if resp == 1:

    print("Campos a serem preenchidos:")
    for i in userCadastro:
        print(i)

    recebeEmail = input('Digite um email:')

    # Verifica se email digitado já esta no DB local

    comandoSql = "SELECT * FROM usuario_login WHERE email = %s"
    valores = (recebeEmail,)
    cursor.execute(comandoSql, valores)

    linha = cursor.fetchone()

    if linha is None:

        # Variável para receber o path e dar acesso ao google chrome
        driver = webdriver.Chrome(
            executable_path=r'D:\Programas\chromedriver.exe')

        # get para abrir o navegador e no caso, o chrome
        driver.get(
            "http://automationpractice.com/index.php?controller=authentication&back=my-account")

        # seleção de elementos para manipular o DOM da página web

        driver.find_element_by_id("email_create").send_keys(recebeEmail)

        driver.find_element_by_id("SubmitCreate").click()

        # Todos os "times.sleep's"  foram colocados para evitar bugs na automação dos processos "

        time.sleep(10)

        # Criação do usuário

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

        time.sleep(5)

        driver.find_element_by_xpath(
            "/html/body/div/div[1]/header/div[2]/div/div/nav/div[2]/a").click()

        time.sleep(5)

        driver.find_element_by_id("id_contact").send_keys('Webmaster')
        driver.find_element_by_id("email").send_keys(recebeEmail)
        driver.find_element_by_id("id_order").send_keys('Teste')
        driver.find_element_by_id("message").send_keys('Teste mensagem')
        driver.find_element_by_id("submitMessage").click()

        time.sleep(5)

        # Ir para página inicial

        driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[3]/div/ul/li/a/span").click()

        time.sleep(5)

        driver.find_element_by_xpath(
            "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a").click()

        time.sleep(5)

        # Logar com o usuário

        driver.find_element_by_id("email").send_keys(recebeEmail)
        driver.find_element_by_id("passwd").send_keys('123456')
        driver.find_element_by_id("SubmitLogin").click()

        # Armazena dados no DB local para gerar o loop de novos cadastro em sua verificações

        comandoSql = "INSERT INTO usuario_login(email, nome, senha) VALUES(%s, %s, %s)"
        valores = (recebeEmail, 'Joao', '123456')
        cursor.execute(comandoSql, valores)
        conDb.commit()

    else:
        print("email já cadastrado, por favor execute o programa novamente!")

elif resp == 2:

    print("Campos a serem preenchidos")

    for j in userLogin:
        print(j)

    # Busca email no DB local para realizar o login caso já tenha cadastrp

    recebeEmail = input('Digite um email:')

    # Variável para receber o path e dar acesso ao google chrome
    driver = webdriver.Chrome(executable_path=r'D:\Programas\chromedriver.exe')

    # get para abrir o navegador e no caso, o chrome
    driver.get(
        "http://automationpractice.com/index.php?controller=authentication&back=my-account")

    driver.find_element_by_id("email").send_keys(recebeEmail)
    driver.find_element_by_id("passwd").send_keys('123456')
    driver.find_element_by_id("SubmitLogin").click()

# Fecha a conexão com banco de dados

if conDb.is_connected():
    cursor.close()
    conDb.close()
