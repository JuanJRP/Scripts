from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.acer.com/ar-es')

sleep(3)

titulos_anuncios = driver.find_elements(By.XPATH, '//body/footer[@id="footer"]/div[1]')

for titulo in titulos_anuncios:
    print(titulo.text)