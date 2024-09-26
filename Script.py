from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#valores
user_name = "correo"
password = "contraseña"

#configuracion
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.facebook.com')

#parametros
element = driver.find_element("id","email")
element.send_keys(user_name)
element = driver.find_element("id","pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)

#espera y cerrado
time.sleep(10)
driver.quit()