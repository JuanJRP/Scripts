from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#valores
user_name = "Admin"
password = "admin123"

#configuracion
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(1)

#parametros
element = driver.find_element("name","username")
element.send_keys(user_name)
element = driver.find_element("name","password")
element.send_keys(password)
element.send_keys(Keys.RETURN)

#espera y cerrado
time.sleep(10)
driver.quit()