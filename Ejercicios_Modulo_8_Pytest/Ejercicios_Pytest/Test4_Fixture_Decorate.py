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
def setup_uno():
    print("\n\n-----------------Iniciando las pruebas #1-----------\n")
    yield
    print("\n-------------Pruebas #1 finalizadas con exito-------")

@pytest.fixture(scope='module')
def setup_dos():
    print("\n\n-----------------Iniciando las pruebas #2-----------\n")
    yield
    print("\n----------Pruebas #2 finalizadas con exito----------")

@pytest.fixture(scope='module')
def setup_tres():
    print("\n\n-----------------Iniciando las pruebas #3-----------\n")
    yield
    print("\n----------Pruebas #3 finalizadas con exito----------")

def test_uno(setup_uno):
    print("\n\nEjecución de prueba - Test #1")

def test_dos(setup_dos):
    print("\n\nEjecución de prueba - Test #2")

@pytest.mark.usefixtures("setup_tres")
def test_tres():
    print("\n\nEjecución de prueba - Test #3")