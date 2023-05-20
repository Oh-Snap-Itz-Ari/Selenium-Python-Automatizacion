from selenium import webdriver # 1. Importamos el Web Driver
from selenium.webdriver.chrome.service import Service # 2. Con la misma libreria importamos el Servicio

# 3. Creamos el driver de Chrome y le indicamos la ruta en el que se encuentra
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demoqa.com/text-box") # 4. Le indicamos la ruta a la que queremos que vaya

print(driver.title) # 5. Imprimimos el titulo de la página en la consola

driver.close() # 6. Cerramos el Driver (Finalizamos el proceso)