import time
import unittest
import openpyxl # 1. Importante añadir la libreria
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Funciones import Funciones_Globales

t = .5
driver = "" # 2. Para no tener que definir la variable también el el teardown se crea aca y se vacia

@pytest.fixture(scope='module')
def setup_Login_uno():
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    global driver  # 4. Continuando con el punto 1, es importante también declarar la variable "driver" como global
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
    f.TextoMixto("XPATH", "//input[contains(@id,'Email')]", "admin@yourstore.com", t)
    f.TextoMixto("XPATH", "//input[@id='Password']", "admin", t)
    f.ClickMixto("XPATH", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("\n\n----------Inicio de la Prueba Login #1----------\n")
    yield
    print("\n----------Final de la Prueba Login #1----------\n")
    driver.close()

@pytest.fixture(scope='module')
def setup_Login_dos():
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    global driver  # 4. Continuando con el punto 1, es importante también declarar la variable "driver" como global
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", t)
    f.TextoMixto("XPATH", "//input[contains(@name,'username')]", "Admin", t)
    f.TextoMixto("XPATH", "//input[contains(@type,'password')]", "admin123", t)
    f.ClickMixto("XPATH", "//button[@type='submit'][contains(.,'Login')]", t)
    print("\n\n----------Inicio de la Prueba Login #2----------\n")
    yield
    print("\n----------Final de la Prueba Login #2----------\n")
    driver.close()

@pytest.mark.usefixtures("setup_Login_uno")
def test_uno():
    f = Funciones_Globales(driver)
    print("\n\n¡Bienvenido al Login #1!")

    # 5. Buscando un usuario a través del correo electrónico
    f.ClickMixto("XPATH","(//p[contains(.,'Customers')])[1]",t)
    f.ClickMixto("XPATH", "(//p[contains(.,'Customers')])[2]", t)
    f.TextoMixto("XPATH", "//input[@name='SearchEmail']", "victoria_victoria@nopCommerce.com", t)
    f.ClickMixto("XPATH", "//button[@id='search-customers']", t)

    # 6. Creando un nuevo usuario
    f.ScrollPageUp(t)
    f.ClickMixto("XPATH", "//a[@href='/Admin/Customer/Create']", t)
    f.TextoMixto("XPATH", "//input[@id='Email']", "Prueba123@gmail.com", t)
    f.TextoMixto("XPATH", "//input[@id='Password']", "Alfamego#654789", t)
    f.TextoMixto("XPATH", "//input[@id='FirstName']", "Alex Fabián", t)
    f.TextoMixto("XPATH", "//input[@id='LastName']", "Melo Gómez", t)
    f.ClickMixto("XPATH", "//input[@id='Gender_Male']", t)
    f.TextoMixto("XPATH", "//input[@id='DateOfBirth']", "4/5/2000", t)
    f.TextoMixto("XPATH", "//input[@id='Company']", "Apple Company", t)
    f.ClickMixto("XPATH", "//input[@id='IsTaxExempt']", t)
    f.Select_Mixto_Type("XPATH","//select[@id='VendorId']","value","2",t)
    f.TextoMixto("XPATH", "//textarea[@id='AdminComment']", "Prueba Test Mr Blue Sky", t)
    f.ScrollPageUp()
    f.ClickMixto("XPATH", "//button[@name='save']", t)

@pytest.mark.usefixtures("setup_Login_dos")
def test_dos():
    f = Funciones_Globales(driver)
    print("\n\n¡Bienvenido al Login #2!")

    # 5. Buscando un usuario a través del correo electrónico
    f.ClickMixto("XPATH", "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Admin')]", t)
    f.ClickMixto("XPATH", "//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'User Management')]", t)
    f.ClickMixto("XPATH", "(//li[contains(.,'Users')])[2]", t)
    f.TextoMixto("XPATH", "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input", "Cecil.Bonaparte"+Keys.ENTER, 3)
    f.ScrollPageUp()