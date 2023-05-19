import time
from selenium import webdriver # 1. Importamos el Web Driver
from selenium.webdriver.chrome.service import Service # 2. Con la misma libreria importamos el Servicio
from selenium.webdriver.common.by import By # 3. Necesario para hacer el envio de la información a través del xPath
from selenium.webdriver.common.keys import Keys # 4. Las keys son necesarias para este ejercicio

# 5. Creamos el driver de Chrome y le indicamos la ruta en el que se encuentra
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

tiemp = 3 # 6. Guardamos el valor del tiempo dentro de una variable (Si es de más de 2 es necesario usar una función de JavaScript)

driver.get("https://demoqa.com/text-box") # 7. Le indicamos las rutas a la que queremos que vaya
driver.maximize_window() # 8. Sirve para maximizar el tamaño de la ventana
time.sleep(tiemp)

driver.get("https://demoqa.com/automation-practice-form")
time.sleep(tiemp)

driver.get("https://demoqa.com/alerts")
time.sleep(tiemp)

driver.get("https://demoqa.com/auto-complete")
time.sleep(2)

driver.back() # 9. Devuelve a la página anterior (https://demoqa.com/alerts)
time.sleep(1)
driver.forward() # 10. Devuelve a la página siguiente (https://demoqa.com/auto-complete)
time.sleep(1)

driver.execute_script("window.history.go(-1)") # 11. Pasa a la página anterior (https://demoqa.com/alerts)
time.sleep(1)

driver.execute_script("window.history.go(-2)") # 12. Se devuelve 2 páginas a partir de la actual (https://demoqa.com/automation-practice-form)
time.sleep(1)

driver.execute_script("window.history.go(3)") # 13. Se mueve 3 páginas a partir de la página actual (https://demoqa.com/auto-complete)
time.sleep(3)

driver.close() # 10. Cerramos el Driver (Finalizamos el proceso)

print("\nScript ejecutado de forma Satisfactoria")