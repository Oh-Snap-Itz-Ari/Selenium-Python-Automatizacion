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

def setup_function(function): # 2. Es preferible que dentro del parentesis tenga también la variable function
    print("\n----------Inicio de la prueba----------\n") #
    # ser = Service("C:\Drivers\chromedriver.exe")
    # op = webdriver.ChromeOptions()
    # global driver  # 6. Continuando con el punto 1, es importante también declarar la variable "driver" como global
    # driver = webdriver.Chrome(service=ser, options=op)
    # f = Funciones_Globales(driver)

def teardown_function(function): # 3. Es preferible que dentro del parentesis tenga también la variable function
    print("\n----------Final de la prueba----------\n")
    # driver.close()


@pytest.mark.validar_if
def test_validarIf():

    nombre1 = "Alex"
    nombre2 = "Fabián"

    # 4. Se ingresa la condición + El mensaje en caso tal de que falle
    assert nombre1 == nombre2, "\nLos nombres no es el mismo - Test no exitoso"

@pytest.mark.validar_If_MenorIgual_And
def test_validarIf_2():

    a = 19
    b = 23
    c = 18

    # 4. Se ingresa la condición + El mensaje en caso tal de que falle
    assert a <= b and a <= c, "\nA es mayor o igual que que B o A es mayor o igual que que C - Test no exitoso"

@pytest.mark.validar_MenorIgual_Or
def test_validarIf_3():

    a = 19
    b = 23
    c = 18

    # 4. Se ingresa la condición + El mensaje en caso tal de que falle
    assert a <= b or a <= c, "\nA es mayor o igual que que B o A es mayor o igual que que C - Test no exitoso"

@pytest.mark.validar_IN
def test_IN():
    dato = "Computador"
    frase = "Dentro de los computadores hay memoria RAM"

    assert dato in frase, "El campo ""Computador"" no se encuentra dentro de la frase"

@pytest.mark.doble_Validacion
def test_Doble_Validacion():
    a = 20
    b = 25

    if (a == b):
        print("\n\nLos datos son iguales")
        (a == b)

    else:
        assert a == b, "\n\nLos datos no son iguales"

@pytest.mark.doble_Validacion_2
def test_Doble_Validacion_2():
    a = 20
    b = 25

    if (a == b):
        assert True, "\n\nLos datos son iguales"

    else:
        assert False, "\n\nLos datos no son iguales"