from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import requests
import time

from selenium.webdriver.support.ui import Select
sep = ' '
sep2 = 'R'
municipio = []
pib_per_format = []

WINDOW_SIZE = "1500,900"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome(executable_path='D:/python/chromedriver', chrome_options=chrome_options)

driver.get('https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html?=&t=pib-por-municipio')

#abrindo a lista e selecionando item da lista
driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/div/section/div[13]/div[1]/div/form/div/div/a/span').click() #clicando na lista
nome_municipio = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/div/section/div[13]/div[1]/div/form/div/div/div/ul/li[2]').text  #selecionando valor na lista

municipio.append(nome_municipio)

#selecionando o campo do PIB e salvando
driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/div/section/div[13]/div[1]/div/form/div/div/div/ul/li[2]').click()

#formatando o campo de valor do PIB
pib_per = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/div/section/div[13]/div[2]/div[2]/div/ul/li[3]/div/p[2]').text
pib_per = pib_per.split(sep, 1)[0] #separador que deleta o ano
pib_per = pib_per.split(sep2, 1)[0] #separador que deleta o cifrao

#adicinando o valor a tabela
pib_per_format.append(pib_per)


print(municipio)
print(pib_per_format)
time.sleep(10)
