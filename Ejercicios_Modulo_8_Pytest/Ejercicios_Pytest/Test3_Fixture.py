import time
import unittest
import openpyxl # 1. Importante añadir la libreria

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Funciones import Funciones_Globales # 1. Al estar en la misma carpeta solo es necesario el "from Funciones import ..."

t = .5
driver = "" # 2. Para no tener que definir la variable también el el teardown se crea aca y se vacia

def setup_function(function): # 3. Es preferible que dentro del parentesis tenga también la variable function
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    global driver # 4. Continuando con el punto 1, es importante también declarar la variable "driver" como global
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)
    f.TextoMixto("XPATH", "//input[contains(@id,'Email')]", "admin@yourstore.com", t)
    f.TextoMixto("XPATH", "//input[@id='Password']", "admin", t)
    f.ClickMixto("XPATH", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("\n\n----------Inicio de la prueba----------\n")

def teardown_function(function): # 5. Es preferible que dentro del parentesis tenga también la variable function
    print("\n----------Final de la prueba----------\n")
    driver.close()

def test_1_Buscar_Producto():
    f = Funciones_Globales(driver)
    f.ClickMixto("XPATH", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.ClickMixto("XPATH", "(//p[contains(.,'Products')])[1]", t)
    f.TextoMixto("XPATH", "//input[contains(@id,'SearchProductName')]", "HP", t)
    f.ClickMixto("XPATH", "//button[@id='search-products']", t)

def test_2_Añadir_Manufactura():
    f = Funciones_Globales(driver)
    f.ClickMixto("XPATH", "(//p[contains(.,'Catalog')])[1]", t)
    f.ClickMixto("XPATH", "//p[contains(.,'Manufacturers')]", t)
    f.ClickMixto("XPATH", "//a[@href='/Admin/Manufacturer/Create']", 3)
    f.TextoMixto("ID", "Name", "Macintosh INC"+Keys.TAB+"Prueba", t)
    f.ClickMixto("XPATH", "//button[@name='save']", t)
    time.sleep(3)

def test_3_Añadir_Producto():
    f = Funciones_Globales(driver)
    f.ClickMixto("XPATH", "(//p[contains(.,'Catalog')])[1]", t)
    f.ClickMixto("XPATH", "(//p[contains(.,'Products')])[1]", t)
    f.ClickMixto("XPATH", "//a[@href='/Admin/Product/Create']", t)
    f.TextoMixto("XPATH", "//input[@id='Name']", "Alex Fabián Melo Gómez", t)
    f.TextoMixto("XPATH", "//textarea[contains(@id,'ShortDescription')]", "Prueba"+Keys.TAB+"Prueba", t)
    f.TextoMixto("XPATH", "//input[contains(@id,'Sku')]", "1235", t)
    f.ScrollPageDown(t)
    f.ScrollPageUp(t)
    f.ClickMixto("XPATH", "//button[@name='save']", t)