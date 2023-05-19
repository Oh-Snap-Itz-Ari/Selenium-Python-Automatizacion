import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
t = 1
time.sleep(t)

driver.find_element(By.XPATH,("//input[@name='first_name']")).send_keys("Alex Fabián" + Keys.TAB + "Melo Gómez" + Keys.TAB + "alexfabianmelo12@hotmail.com")
time.sleep(t)
driver.find_element(By.XPATH,("//input[@name='phone']")).send_keys("3245447847" + Keys.TAB + "Calle 28 # 27 - 26" + Keys.TAB + "Fusagasugá, Cundinamarca")
time.sleep(t)
state = Select(driver.find_element(By.XPATH,("//select[@name='state']")))
state.select_by_index(5)
time.sleep(t)

driver.find_element(By.XPATH,("//input[@name='zip']")).send_keys("33010" + Keys.TAB + "https://www.crunchyroll.com/es")
driver.find_element(By.XPATH,("//input[@value='yes']")).click()
driver.find_element(By.XPATH,("//textarea[@name='comment']")).send_keys("Mr. Blue Sky was here ..." + Keys.TAB + Keys.ENTER)
time.sleep(5)

time.sleep(t)

driver.close()