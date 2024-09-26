from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

usuario_xpath = "//input[@id='email']"
password_xpath = "//input[@id='pass']"
login_boton_xpath = "//button[@name='login']"
wh_boton_xpath = "//body/div[@id='mount_0_0_Wr']/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/ul[1]/li[3]/span[1]/div[1]/a[1]"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.facebook.com')

try:
    time.sleep(2)
    usuario_elemento = driver.find_element(By.XPATH, usuario_xpath)
    usuario_elemento.send_keys("user")
    password_elemento = driver.find_element(By.XPATH, password_xpath)
    password_elemento.send_keys("pass")
    login_boton_elemento = driver.find_element(By.XPATH, login_boton_xpath)
    login_boton_elemento.click()
    time.sleep(10)
    wh_boton_xpath_ele = driver.find_element(By.XPATH, wh_boton_xpath)
    wh_boton_xpath_ele.click
except Exception as e:
    print("Error: ", e)

