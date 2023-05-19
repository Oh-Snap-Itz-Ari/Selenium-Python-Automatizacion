import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

t = 2

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

btn = driver.find_element(By.XPATH,("//button[@type='submit'][contains(.,'Send')]"))
btn.click()
time.sleep(t)

name_val = driver.find_element(By.XPATH,("//small[@class='help-block'][contains(.,'Please supply your first name')]"))
name = name_val.text # 1. Busca el valor del nombre y lo almacena dentro de la variable name

print("\nEl valor del error es: " + name)

if (name == "Please supply your first name"):
    print("\n- Falta el nombre")
    wn = driver.find_element(By.XPATH,("//input[@name='first_name']")).send_keys("Alex Fabián")
    time.sleep(t)
    print("\n- El nombre ha sido escrito de forma correcta")

else:
    print("\n- Falta el nombre")

apell_val = driver.find_element(By.XPATH,("//small[@class='help-block'][contains(.,'Please supply your last name')]"))
apell = apell_val.text # 2. Busca el valor del apellido y lo almacena dentro de la variable name

print("\nEl valor del error es: " + apell)

if (apell == "Please supply your last name"):
    print("\n- Falta el apellido")
    wa = driver.find_element(By.XPATH,("//input[@name='last_name']")).send_keys("Melo Gómez")
    time.sleep(t)
    print("\n- El apellido ha sido escrito de forma correcta")

else:
    print("\n- Falta el apellido")

print("\n¿El botón de Enviar esta habilitado? - " + str(btn.is_enabled())) # 3. Valida si esta habilidado el botón de enviar

if(btn.is_enabled() == False):
    print("\n- Faltan campos por llenar")

else:
    print("\n- Todo correcto, enviado de forma correcto")

time.sleep(t)

driver.close()