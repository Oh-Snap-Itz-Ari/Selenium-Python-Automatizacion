import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Ejercicios_Modulo_5_POM.Funciones import Funciones_Globales # 1. Se hace un import de Funciones.py en la raiz de la carpeta Ejercicios_Modulo_5_POM

t = 1 # 2. Nos sirve si queremos que se ejecute de forma más rapida la prueba, solo con cambiar el valor de t cambia en todos

class baseTest(unittest.TestCase):
    def setUp(self):
        ser = Service("C:\Drivers\chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def test_POM(self): # 3. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver) # 4. Estas 2 primeras lineas siempre se deben hacer, para que se vinculen con el Funciones.py
        f.Navegar("https://www.saucedemo.com/",t)
        f.TextoByXPath("//input[@id='user-name']","MrBlueSky123",t)
        f.TextoByID("password", "Alfamego#123456", t)
        f.ClickByXPath("//input[@id='login-button']",t)

    def tearDown(self):
        driver = self.driver
        time.sleep(2)
        driver.close()

if __name__ == '__main__':
    unittest.main()