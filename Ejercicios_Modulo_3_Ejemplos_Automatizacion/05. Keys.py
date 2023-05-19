import time
from selenium import webdriver # 1. Importamos el Web Driver
from selenium.webdriver.chrome.service import Service # 2. Con la misma libreria importamos el Servicio
from selenium.webdriver.common.by import By # 3. Necesario para hacer el envio de la información a través del xPath
from selenium.webdriver.common.keys import Keys # 4. Las keys son necesarias para este ejercicio

# 5. Creamos el driver de Chrome y le indicamos la ruta en el que se encuentra
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demoqa.com/text-box") # 6. Le indicamos la ruta a la que queremos que vaya

driver.maximize_window() # 7. Sirve para maximizar el tamaño de la ventana
time.sleep(1) # 8. Espera 1 segundo tras maximizar el tamaño de la ventana

# 9. Busca el elemento a través del xPath, y a partir de ese comienza a dar tab para navegar por los diferentes campos
test = driver.find_element(By.XPATH,"//*[@id='userName']")
test.send_keys("Alex Fabián Melo Gómez" + Keys.TAB + "alexfabianmelo12@hotmail.com" + Keys.TAB + "Calle 28 # 01 - 26 San Fernando" +
               Keys.TAB + "Calle 28 # 01 - 26 San Fernando" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(3)

driver.find_element(By.XPATH, "//div[@class='header-text'][contains(.,'Forms')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(.,'Practice Form')]").click()
time.sleep(2)

driver.close() # 10. Cerramos el Driver (Finalizamos el proceso)

print("\nScript ejecutado de forma Satisfactoria")