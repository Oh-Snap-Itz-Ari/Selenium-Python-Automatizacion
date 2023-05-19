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

driver.get("https://hackstore.re/")
driver.maximize_window()
#driver.implicitly_wait(10) # 6. No siempre el aviso va a aparecer al mismo tiempo, por eso es importante darle 10 segundos de
# holgura por si se demora en salir

t = .2

btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#cerrar-aviso']")))
btn.click()

click = driver.find_element(By.XPATH,"//input[@id='s']").click()
search = driver.find_element(By.XPATH,"//input[@id='s']").send_keys("The Good Doctor" + Keys.ENTER)
click2 = driver.find_element(By.XPATH,"//a[@title='The Good Doctor (2017)']").click()

time.sleep(t)

driver.close()