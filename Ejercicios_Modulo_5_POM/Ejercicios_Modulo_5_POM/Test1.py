import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Ejercicios_Modulo_5_POM.Funciones import Funciones_Globales # 1. Se hace un import de Funciones.py en la raiz de la carpeta Ejercicios_Modulo_5_POM
from Ejercicios_Modulo_5_POM.Page_Login import Pagina_Login # 2. Se hace un import de Page_Login.py en la raiz de la carpeta Ejercicios_Modulo_5_POM

t=1

class baseTest(unittest.TestCase):
    def setUp(self):
        ser = Service("C:\Drivers\chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def test_POM(self): # 3. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver) # 4. Se importan los driver tanto de Funciones_Globales como el Pagina_Login
        pg = Pagina_Login(driver)
        pg.Login_Master("https://www.saucedemo.com/","MrBlueSky123","Alfamego#123456",t)

    def tearDown(self):
        driver = self.driver
        time.sleep(2)
        driver.close()

if __name__ == '__main__':
    unittest.main()