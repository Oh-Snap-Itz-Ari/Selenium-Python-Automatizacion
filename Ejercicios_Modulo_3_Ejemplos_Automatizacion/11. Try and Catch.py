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

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
t = 2

# 1. Si se cumple la condición del dayselect se hace la ejecución (try) sino, continua con lo que esta por fuera de este
try:
    daysselect = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='select-demo']")))
    days = Select(daysselect)

    days.select_by_visible_text("Monday") # 2. Se realiza la busqueda a través del texto visible "Monday"
    time.sleep(t)
    days.select_by_index(4) # 3. Se realiza la busqueda a través del número de valor (1 - Sunday, 2 - Monday, 3 - Tuesday, 4 - Wednesday, etc.)
    time.sleep(t)
    days.select_by_index(6)
    time.sleep(t)
    days.select_by_value("Sunday") # 4. Este valor se obtiene inspeccionando el elemento y tomando el valor de value="..."
    time.sleep(t)

except TimeoutException as ex: # 5. Se define y se guarda en "ex"
    print(ex.msg)
    print("El elemento con id = 'select-demo' no existe.")

# 6. En caso tal de que no encuentre el XPATCH del Try continua esto que esta por fuera

driver.execute_script("window.scrollTo(0,150)")
time.sleep(t)

ciudad = Select(driver.find_element(By.ID, "multi-select"))

ciudad.select_by_index(1)  # 1 - California
time.sleep(t)

ciudad.select_by_index(2)  # 2 - Florida
time.sleep(t)

ciudad.select_by_index(3)  # 3 - New Jersey
time.sleep(t)

driver.close()