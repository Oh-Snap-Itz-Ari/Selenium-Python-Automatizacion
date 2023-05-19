import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

t = 2

driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(t)

titulo = driver.find_element(By.XPATH,("//img[@src='/images/Toolsqa.jpg']"))
print("\n¿Se encontró la imagen? - " + str(titulo.is_displayed()))

btnElements = driver.find_element(By.XPATH,("//h5[contains(.,'Elements')]"))

if(titulo.is_displayed() == True):
    print("\nLa imagen existe.")
    btnElements.click()
    driver.find_element(By.XPATH,("//span[@class='text'][contains(.,'Text Box')]")).click()
    time.sleep(t)
else:
    print("\nLa imagen no existe.")

btnSubmit = driver.find_element(By.XPATH,("//button[@id='submit']"))
print("\n¿Se encontró el botón? - " + str(btnSubmit.is_enabled()))

if(btnSubmit.is_enabled() == True):
    print("\nEl botón existe.")
    driver.find_element(By.XPATH,("//input[@id='userName']")).send_keys("Alex Fabián Melo Gómez" + Keys.TAB + "alexfabianmelo12@hotmail.com"
                                                                        + Keys.TAB + "Calle 28 # 01 - 26" + Keys.TAB + "Calle 28 # 01 - 26")
    btnSubmit.click()
    time.sleep(t)
else:
    print("\nEl botón no existe.")

time.sleep(t)

driver.close()