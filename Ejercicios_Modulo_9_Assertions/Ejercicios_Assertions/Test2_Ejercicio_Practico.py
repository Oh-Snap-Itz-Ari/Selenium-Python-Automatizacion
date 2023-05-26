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
def setup_Login():
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    global driver  # 3. Continuando con el punto 2, es importante también declarar la variable "driver" como global
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", t)
    f.TextoMixto("XPATH", "//input[contains(@name,'username')]", "Admin", t)
    f.TextoMixto("XPATH", "//input[contains(@type,'password')]", "admin123", t)
    f.ClickMixto("XPATH", "//button[@type='submit'][contains(.,'Login')]", t)

def teardown_function(function): # 3. Es preferible que dentro del parentesis tenga también la variable function
    print("\n----------Final de la prueba----------\n")
    driver.close()

@pytest.mark.test_uno
@pytest.mark.usefixtures("setup_Login")
def test_uno_login():
    f = Funciones_Globales(driver)
    # 4. Se busca la etiqueta que tiene el texto "Dashboard", se almacena en la variable "etiqueta" y se valida si fue encontrada (if)
    etiqueta = f.FindElementByXPATH("//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module'][contains(.,'Dashboard')]").text
    print("\n\n- Se encontró la etiqueta y contiene la siguiente información -> " + etiqueta)
    if (etiqueta == "Dashboard"): # 5. Si se cumple la condición (Acceso exitoso) aparece el siguiente mensaje
        print("\n##################################################\n\nHas ingresado al sistema de forma satisfactoria\n\n##################################################\n")
        assert etiqueta == "Dashboard"
    else:
        assert etiqueta == "Dashboard", "\nNo has podido ingresar al sistema de forma satisfactoria"

