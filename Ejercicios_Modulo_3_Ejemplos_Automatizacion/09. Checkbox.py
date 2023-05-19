import time
from selenium import webdriver # 1. Importamos el Web Driver
from selenium.webdriver.chrome.service import Service # 2. Con la misma libreria importamos el Servicio
from selenium.webdriver.common.by import By # 3. Necesario para hacer el envio de la información a través del xPath
from selenium.webdriver.common.keys import Keys # 4. Las keys son necesarias para este ejercicio
from selenium.webdriver.support.wait import WebDriverWait # 5. El WebDriverWait y el Expectec_Conditions son para el Implicity wait
from selenium.webdriver.support import expected_conditions as EC

# 5. Creamos el driver de Chrome y le indicamos la ruta en el que se encuentra
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()

t = 3

# 6. Se indica a través del XPATH cuales Checkbox queremos que se marquen
btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[1]")))
btn.click()

btn5 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[5]")))
btn5.click()

btn6 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[6]")))
btn6.click()

time.sleep(t)

driver.close()