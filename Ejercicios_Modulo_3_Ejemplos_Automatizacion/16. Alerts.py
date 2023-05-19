import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

t = 2

driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()
time.sleep(t)

driver.find_element(By.XPATH,("//a[@href='#myModal0']")).click()
try:
    options = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]")))
    driver.find_element(By.XPATH,("(//a[@href='#'][contains(.,'Save changes')])[1]")).click()
    time.sleep(t)

    driver.find_element(By.XPATH, ("//a[@href='#myModal0']")).click()
    options2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Close')])[1]")))
    driver.find_element(By.XPATH, ("(//a[@href='#'][contains(.,'Close')])[1]")).click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no existe.")

driver.close()