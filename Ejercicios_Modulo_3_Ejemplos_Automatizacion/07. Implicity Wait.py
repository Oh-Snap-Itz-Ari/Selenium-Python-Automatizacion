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
driver.implicitly_wait(10) # 7. Sirve para darle este tiempo al navegador para que verifique si todos los elementos existen,
# antes de que dé el error, si ve que todos los elementos estan bien continua sin problemas

t = 1

time.sleep(t) # 8. Espera 2 segundos tras maximizar el tamaño de la ventana

# 9. Busca el elemento a través del xPath y envia el valor de "Alex Fabián Melo Gómez"
name = driver.find_element(By.XPATH,"//*[@id='userName']").send_keys("Alex Fabián Melo Gómez")
time.sleep(t)

email = driver.find_element(By.XPATH,"//*[@id='userEmail']").send_keys("alexfabianmelo12@hotmail.com")
time.sleep(t)

address = driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("Calle 28 # 01 - 26 San Fernando")
time.sleep(t)

peraddress = driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys("Calle 28 # 01 - 26 San Fernando")
time.sleep(t)

driver.execute_script("window.scrollTo(0,300)") # 10. Hacemos que baje el scroll 300 pixeles para que pueda encontrar el botón (x,y)
time.sleep(2)

bsubmit = driver.find_element(By.XPATH,"//button[@id='submit']").click() # 11. Le ordenamos que dé clic al botón de "Submit"
time.sleep(2)

driver.close() # 12. Cerramos el Driver (Finalizamos el proceso)