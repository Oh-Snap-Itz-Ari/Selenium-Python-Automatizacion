import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
t = 1
time.sleep(t)

links = driver.find_elements(By.TAG_NAME,"a") # 1. Nos permite hacer la busqueda de todos los links <a> dentro de la página
print("\nEl número total de Links son: ", len(links)) # 2. Len imprime la cantidad de valores que se almacenan dentro de "links"

for nums in links:
    print(nums.text) # 3. Se almacena dentro de nums los links buscados y se imprimen por consola

driver.find_element(By.LINK_TEXT,("Date pickers")).click() # 4. Se hace la busqueda de un elemento a través del nombre de su link
time.sleep(3)

driver.find_element(By.LINK_TEXT,("Bootstrap Date Picker")).click()
time.sleep(2)

time.sleep(t)

driver.close()