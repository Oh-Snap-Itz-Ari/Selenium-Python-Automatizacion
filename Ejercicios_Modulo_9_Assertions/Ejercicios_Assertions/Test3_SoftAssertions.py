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

def teardown_function(function): # 3. Es preferible que dentro del parentesis tenga también la variable function
    print("\n----------Final de la prueba----------\n")
    # driver.close()

@pytest.mark.run
def test_uno_Soft():
    print("\nPrimer test")
    assert True

@pytest.mark.run
def test_dos_Soft():
    a = 10
    b = 10
    assert a == b, "A es diferente de B (No son iguales)"
    assert a != b, "A es igual que B"
    assert a < b, "A no es menor que B"
    assert a > b, "A no es mayor que B"


@pytest.mark.run
def test_tres_Soft():
    a = 15
    b = 10
    assert a < b, "A no es menor que B"

@pytest.mark.run
def test_cuatro_Soft():
    a = 20
    b = 15
    assert a > b, "A no es mayor que B"

@pytest.mark.run
def test_cinco_Soft():
    nombre1 = "Alex"
    nombre2 = "Fabián"
    assert nombre1 == nombre2, "\nLos nombres no es el mismo - Test no exitoso"

