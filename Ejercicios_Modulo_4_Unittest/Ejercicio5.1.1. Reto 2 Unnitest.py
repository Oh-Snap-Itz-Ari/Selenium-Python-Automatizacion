import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class PruebaLogin(unittest.TestCase):
    def setUp(self):
        ser = Service("C:\Drivers\chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.maximize_window()


    def test_login1(self): # 1. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        userName = driver.find_element(By.XPATH,("//input[@id='user-name']"))
        userPass = driver.find_element(By.XPATH,("//input[@id='password']"))
        btnLogin = driver.find_element(By.XPATH,("//input[@id='login-button']"))

        userName.send_keys("MrBlueSky123")
        userPass.send_keys("Alfamego#123456")
        btnLogin.click()

        # 2. Se captura el error y se almacena en la variable "error"
        error = driver.find_element(By.XPATH,("//h3[contains(@data-test,'error')]"))
        error = error.text
        print("\n------------------------------------------------------------------------------------------\n"
              "El error que se digitó por pantalla es el siguiente:\n- " + str(error))

        if (error == "Epic sadface: Username and password do not match any user in this service"):
            print("\nLos datos de ingreso no son correctos, por favor validarlos y volver a intentar")
            print("\nPrueba #1 = OK"
                  "\n------------------------------------------------------------------------------------------")
        time.sleep(2)


    def test_login2(self): # 1. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        userName = driver.find_element(By.XPATH,("//input[@id='user-name']"))
        userPass = driver.find_element(By.XPATH,("//input[@id='password']"))
        btnLogin = driver.find_element(By.XPATH,("//input[@id='login-button']"))

        userName.send_keys("")
        userPass.send_keys("Alfamego#123456")
        btnLogin.click()

        # 2. Se captura el error y se almacena en la variable "error"
        error = driver.find_element(By.XPATH,("//h3[contains(@data-test,'error')]"))
        error = error.text
        print("\n------------------------------------------------------------------------------------------\n"
              "El error que se digitó por pantalla es el siguiente:\n- " + str(error))

        if (error == "Epic sadface: Username is required"):
            print("\nLos datos de ingreso no estan completos, por favor validar el campo de Username")
            print("\nPrueba #2 = OK"
                  "\n------------------------------------------------------------------------------------------")
        time.sleep(2)


    def test_login3(self): # 1. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        userName = driver.find_element(By.XPATH,("//input[@id='user-name']"))
        userPass = driver.find_element(By.XPATH,("//input[@id='password']"))
        btnLogin = driver.find_element(By.XPATH,("//input[@id='login-button']"))

        userName.send_keys("MrBlueSky123")
        userPass.send_keys("")
        btnLogin.click()

        # 2. Se captura el error y se almacena en la variable "error"
        error = driver.find_element(By.XPATH,("//h3[contains(@data-test,'error')]"))
        error = error.text
        print("\n------------------------------------------------------------------------------------------\n"
              "El error que se digitó por pantalla es el siguiente:\n- " + str(error))

        if (error == "Epic sadface: Password is required"):
            print("\nLos datos de ingreso no estan completos, por favor validar el campo de Password")
            print("\nPrueba #3 = OK"
                  "\n------------------------------------------------------------------------------------------")
        time.sleep(2)


    def test_login4(self): # 1. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        userName = driver.find_element(By.XPATH,("//input[@id='user-name']"))
        userPass = driver.find_element(By.XPATH,("//input[@id='password']"))
        btnLogin = driver.find_element(By.XPATH,("//input[@id='login-button']"))

        userName.send_keys("")
        userPass.send_keys("")
        btnLogin.click()

        # 2. Se captura el error y se almacena en la variable "error"
        error = driver.find_element(By.XPATH,("//h3[contains(@data-test,'error')]"))
        error = error.text
        print("\n------------------------------------------------------------------------------------------\n"
              "El error que se digitó por pantalla es el siguiente:\n- " + str(error))

        if (error == "Epic sadface: Username is required"):
            print("\nLos datos de ingreso no estan completos, por favor validar los campos de Username y Password")
            print("\nPrueba #4 = PENDIENTE (Muestra mensaje de Username al dejar los 2 campos vacios)"
                  "\n------------------------------------------------------------------------------------------")
        time.sleep(2)


    def test_login5(self): # 1. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        userName = driver.find_element(By.XPATH,("//input[@id='user-name']"))
        userPass = driver.find_element(By.XPATH,("//input[@id='password']"))
        btnLogin = driver.find_element(By.XPATH,("//input[@id='login-button']"))

        userName.send_keys("standard_user")
        userPass.send_keys("secret_sauce")
        btnLogin.click()
        print("\n------------------------------------------------------------------------------------------\n")
        print("\nSe ha ingresado al sistema de forma satisfactoria")
        print("\nPrueba #5 = OK"
              "\n------------------------------------------------------------------------------------------")

        time.sleep(2)

    def tearDown(self):
        driver = self.driver
        time.sleep(2)
        driver.close()

if __name__ == '__main__':
    unittest.main()