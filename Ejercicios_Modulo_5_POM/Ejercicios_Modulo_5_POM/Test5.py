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
        f.Navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html",t)
        for n in range(1,7):
            if (n == 3 or n == 4 or n == 7):
                continue
            f.Clic_Multiple_Mixto("XPATH",t,"(//input[contains(@type,'checkbox')])["+str(n)+"]")
        f.Salida()

if __name__ == '__main__':
    unittest.main()