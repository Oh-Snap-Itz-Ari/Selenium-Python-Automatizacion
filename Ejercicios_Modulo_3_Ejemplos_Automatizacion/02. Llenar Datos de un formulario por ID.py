import time
from selenium import webdriver # 1. Importamos el Web Driver
from selenium.webdriver.chrome.service import Service # 2. Con la misma libreria importamos el Servicio
from selenium.webdriver.common.by import By # 3. Necesario para hacer el envio de la información a través del xPath

# 4. Creamos el driver de Chrome y le indicamos la ruta en el que se encuentra
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demoqa.com/text-box") # 5. Le indicamos la ruta a la que queremos que vaya

driver.maximize_window() # 6. Sirve para maximizar el tamaño de la ventana
time.sleep(1) # 7. Espera 2 segundos tras maximizar el tamaño de la ventana

# 8. Busca el elemento a través del ID y envia el valor de "Alex Fabián Melo Gómez"
name = driver.find_element(By.ID,"userName").send_keys("Alex Fabián Melo Gómez")
time.sleep(1)

email = driver.find_element(By.ID,"userEmail").send_keys("alexfabianmelo12@hotmail.com")
time.sleep(1)

address = driver.find_element(By.ID,"currentAddress").send_keys("Calle 28 # 01 - 26 San Fernando")
time.sleep(1)

peraddress = driver.find_element(By.ID,"permanentAddress").send_keys("Calle 28 # 01 - 26 San Fernando")
time.sleep(1)

driver.execute_script("window.scrollTo(0,300)") # 9. Hacemos que baje el scroll 300 pixeles para que pueda encontrar el botón (x,y)
time.sleep(2)

bsubmit = driver.find_element(By.ID,"submit").click() # 10. Le ordenamos que dé clic al botón de "Submit"
time.sleep(4)

driver.close() # 11. Cerramos el Driver (Finalizamos el proceso)