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

card = driver.find_elements(By.XPATH, '/html/body/main/section/div[2]/div/div/section/div[13]/div[1]/div/form/div/select/option')

#abrindo a lista e selecionando item da lista
for i in range(len(card)):
    if i == 0 or i == 1:
        continue
    
    driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/div/section/div[13]/div[1]/div/form/div/div/a/span').click() #clicando na lista
    nome_municipio = driver.find_element(By.XPATH, f'/html/body/main/section/div[2]/div/div/section/div[13]/div[1]/div/form/div/div/div/ul/li[{i}]').text  #adicionando o municipio a lista
    driver.find_element(By.XPATH, f'/html/body/main/section/div[2]/div/div/section/div[13]/div[1]/div/form/div/div/div/ul/li[{i}]').click() #acessando o municipio

    municipio.append(nome_municipio)

    time.sleep(2)
        #selecionando o campo do PIB e salvando
        # driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/div/section/div[13]/div[1]/div/form/div/div/div/ul/li[2]').click()

        #formatando o campo de valor do PIB
    pib_per = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/div/section/div[13]/div[2]/div[2]/div/ul/li[3]/div/p[2]').text ##NÃO ALTERA LI[]
    pib_per = pib_per.split(sep, 1)[0] #separador que deleta o ano
    pib_per = pib_per.split(sep2, 1)[0] #separador que deleta o cifrao

        #adicinando o valor a tabela
    pib_per_format.append(pib_per)

    
    # print(municipio)
    # print(pib_per_format)

    df = pd.DataFrame(list(zip(municipio, pib_per_format)),
                    columns=['Municipio', 'PIB'])

    print(df.head)