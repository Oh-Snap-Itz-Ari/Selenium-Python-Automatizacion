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
from Ejercicios.Ejercicios_Modulo_8_Pytest.Funciones import Funciones_Globales

def setup_function(function): # 1. Es preferible que dentro del parentesis tenga también la variable function
    print("\n\n----------Inicio de la prueba----------\n")

def teardown_function(function): # 2. Es preferible que dentro del parentesis tenga también la variable function
    print("\n----------Final de la prueba----------\n")

def test_uno():
    print("Test uno")

def test_dos():
    print("Test dos")

def test_tres():
    print("Test tres")

def test_cuatro():
    print("Test cuatro")

def test_cinco():
    print("Test cinco")