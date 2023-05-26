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

t = .1

def get_data(): # 1. Se especifica los datos que se van a tomar y se separan entre (... , ...),
    return [
        ("MrBlueSky123",""),
        ("", "Alfamego#123"),
        ("", ""),
        ("MrBlueSky123", "Alfamego123"),
        ("Admin", "admin123")
    ]

def setup_function(function): # 2. Es preferible que dentro del parentesis tenga también la variable function
    print("\n----------Inicio de la prueba----------\n") #

def teardown_function(function): # 3. Es preferible que dentro del parentesis tenga también la variable function
    print("\n----------Final de la prueba----------\n")
    driver.close()

@pytest.mark.login # 4. Se declara el nombre que nos permite realizar la ejecución por consola
@pytest.mark.parametrize("username,password",get_data()) # 5. Dentro del pytest se especifica los datos y de donde se van a tomar
def test_login(username, password):
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    global driver  # 6. Continuando con el punto 1, es importante también declarar la variable "driver" como global
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", t)
    f.TextoMixto("XPATH", "//input[contains(@name,'username')]", username, t)
    f.TextoMixto("XPATH", "//input[contains(@type,'password')]", password, t)
    f.ClickMixto("XPATH", "//button[@type='submit'][contains(.,'Login')]", t)
    # 7. En esta versión de pytest no reconoce el yield, por eso es necesario usar el setuc y el teardown al inicio