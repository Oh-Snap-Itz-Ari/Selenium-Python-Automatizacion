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

    def test_POM(self): # 4. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver) # 5. Se importan los driver tanto de Funciones_Globales, Pagina_Login y DropdownForm
        f.Navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html",t)
        f.Select_XPath_Type("//select[@id='select-demo']","text","Monday",t)
        f.Salida()

    def test_POM2(self):
        driver = self.driver
        f = Funciones_Globales(driver)  # 5. Se importan los driver tanto de Funciones_Globales, Pagina_Login y DropdownForm
        f.Navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", t)
        f.Select_XPath_Type("//select[@id='select-demo']", "value", "Tuesday", t)
        f.Salida()

    def test_POM3(self):
        driver = self.driver
        f = Funciones_Globales(driver)  # 5. Se importan los driver tanto de Funciones_Globales, Pagina_Login y DropdownForm
        f.Navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", t)
        f.Select_XPath_Type("//select[@id='select-demo']", "index", "4", t)
        f.Salida()

    def test_POM4(self):
        driver = self.driver
        f = Funciones_Globales(driver) # 5. Se importan los driver tanto de Funciones_Globales, Pagina_Login y DropdownForm
        f.Navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html",t)
        f.Select_ID_Type("select-demo","text","Monday",t) # 6. Se implementa la función pero con ID
        f.Salida()

    def test_POM5(self):
        driver = self.driver
        f = Funciones_Globales(driver)  # 5. Se importan los driver tanto de Funciones_Globales, Pagina_Login y DropdownForm
        f.Navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", t)
        f.Select_ID_Type("select-demo", "value", "Tuesday", t)
        f.Salida()

    def test_POM6(self):
        driver = self.driver
        f = Funciones_Globales(driver)  # 5. Se importan los driver tanto de Funciones_Globales, Pagina_Login y DropdownForm
        f.Navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", t)
        f.Select_ID_Type("select-demo", "index", "4", t)
        f.Salida()

    def tearDown(self):
        driver = self.driver
        time.sleep(2)
        driver.close()

if __name__ == '__main__':
    unittest.main()