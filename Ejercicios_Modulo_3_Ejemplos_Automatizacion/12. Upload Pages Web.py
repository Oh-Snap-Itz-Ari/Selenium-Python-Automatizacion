import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException # 1. Esta excepción sirve como alternativa al catch (finally)

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()

t = 2

# 1. Si se cumple la condición del dayselect se hace la ejecución (try) sino, continua con lo que esta por fuera de este
try:
    # 2. Valida la existencia del botón de "Seleccionar archivo" a través de su ID
    btnBuscar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fileinput']")))
    # 3. Selecciona el botón y se envia a través de la Key la ruta en la que se encuentra
    btn = driver.find_element(By.XPATH,("//input[@id='fileinput']")).send_keys("C:/Users/alexf/Desktop/"
                                                                               "Automatización Selenium Python/Ejercicios/img/1.jpg")
    time.sleep(t)

    driver.find_element(By.XPATH,("//input[@id='itsanimage']")).click()
    time.sleep(t)

    driver.find_element(By.XPATH, ("//input[@value='Upload']")).click()
    time.sleep(t)

except TimeoutException as ex: # 5. Se define y se guarda en "ex"
    print(ex.msg)
    print("El elemento con id = 'select-demo' no existe.")

time.sleep(t)

driver.close()