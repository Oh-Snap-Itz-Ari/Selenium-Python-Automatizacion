import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/")
driver.maximize_window()

t = 2

# 1. Si se cumple la condición del dayselect se hace la ejecución (try) sino, continua con lo que esta por fuera de este
try:
    btnMas = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@id,'btn_basic_example')]")))
    btn = driver.find_element(By.XPATH, ("//a[contains(@id,'btn_basic_example')]"))
    ir = driver.execute_script("arguments[0].scrollIntoView();",btn)  # 2. Hace Scroll hasta que encuentra el elemento
    time.sleep(t)

except TimeoutException as ex: # 5. Se define y se guarda en "ex"
    print(ex.msg)
    print("El elemento no existe.")

time.sleep(t)

driver.close()