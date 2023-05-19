import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
t = 2

# 1. Busca el elemento a través del ID y a través del Select(days) permite buscar su contenido
days = driver.find_element(By.XPATH,("//select[@id='select-demo']"))
daysselect = Select(days)

daysselect.select_by_visible_text("Monday") # 2. Se realiza la busqueda a través del texto visible "Monday"
time.sleep(t)
daysselect.select_by_index(4) # 3. Se realiza la busqueda a través del número de valor (1 - Sunday, 2 - Monday, 3 - Tuesday, 4 - Wednesday, etc.)
time.sleep(t)
daysselect.select_by_index(6)
time.sleep(t)
daysselect.select_by_value("Sunday") # 4. Este valor se obtiene inspeccionando el elemento y tomando el valor de value="..."
time.sleep(t)

# 5. Esta es una forma un poco más rapido de hacerlo, se selecciona el ID del MultiSelect y se navega a través de su index
ciudad = Select(driver.find_element(By.ID,"multi-select"))

ciudad.select_by_index(1) # 1 - California
time.sleep(t)
ciudad.select_by_index(2) # 2 - Florida
time.sleep(t)
ciudad.select_by_index(3) # 3 - New Jersey
time.sleep(t)

driver.close()