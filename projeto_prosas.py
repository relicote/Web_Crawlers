from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


nome = []

WINDOW_SIZE = "1366,900"
chrome_options = webdriver.ChromeOptions()

# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome(executable_path='D:/python/chromedriver', chrome_options=chrome_options)

driver.get('https://pictransparenciapf.prosas.com.br')
time.sleep(4)

card =  driver.find_elements(By.XPATH, '//*[@id="voting-app"]/div/div/main/div/div/div[5]/article/div[2]/div')


for i in range(len(card)):
    if i == 0:
        continue
    
    nome.append(driver.find_element(By.XPATH, f'//*[@id="voting-app"]/div/div/main/div/div/div[5]/article/div[2]/div[{i}]/div/a/div[2]/div[2]/div/div/span').text)
    # print(i)
    if i == 127:
        i+=1
        nome.append(driver.find_element(By.XPATH, f'//*[@id="voting-app"]/div/div/main/div/div/div[5]/article/div[2]/div[{i}]/div/a/div[2]/div[2]/div/div/span').text)

print(nome)
time.sleep(100)


