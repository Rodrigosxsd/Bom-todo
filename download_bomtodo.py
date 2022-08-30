from selenium import webdriver
import pyautogui as bot
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd
import openpyxl

navegador = webdriver.Chrome()

navegador.get('https://smart.dekra.com.br/PortalParceiro/Login')

login_path = '//*[@id="Login"]'
password_path = '//*[@id="Senha"]'
enter_path = '//*[@id="btSubmit"]/div[2]'
chassi_path = '//*[@id="Chassi"]'
pesquisar_path = '//*[@id="FuncPesquisa"]'
laudo_path = "ng-scope"

sleep(5)
login_element = navegador.find_element('xpath', login_path)
sleep(5)
password_element = navegador.find_element('xpath', password_path)
sleep(5)
enter_element = navegador.find_element('xpath', enter_path)

login_element.send_keys('pdekra.fandrade')
password_element.send_keys('n@Pista2022')
enter_element.click()


sleep(5)
chassi_element = navegador.find_element('xpath', chassi_path)
sleep(5)
pesquisar_element = navegador.find_element('xpath', pesquisar_path)
sleep(5)
laudo_element = navegador.find_elements('xpath', laudo_path)

chassi_element.send_keys(input('Insira o chassi: \n'))
pesquisar_element.click()
bot.sleep(10)
bot.click(x=1212, y=457)