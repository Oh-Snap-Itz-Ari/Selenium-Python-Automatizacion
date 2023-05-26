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

@pytest.mark.run
def test_uno():
    print("\n\nTest uno\n")

@pytest.mark.skip
def test_dos():
    print("\n\nTest dos\n")

@pytest.mark.run
def test_tres():
    print("\n\nTest tres\n")

@pytest.mark.notrun
def test_cuatro():
    print("\n\nTest cuatro\n")

@pytest.mark.run
def test_cinco():
    print("\n\nTest cinco\n")