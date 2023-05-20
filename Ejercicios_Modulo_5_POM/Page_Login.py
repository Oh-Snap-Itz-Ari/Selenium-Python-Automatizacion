import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Ejercicios_Modulo_5_POM.Funciones import Funciones_Globales

class Pagina_Login (): # 1. Se crea la clase Pagina_Login y se crea la inicialización dentro de esta
    def __init__(self,driver):
        self.driver = driver

    # Función que permite llenar el formulario de Login, haciendo llenado de diferentes funcione pertenecientes a Funciones_Globales
    def Login_Master(self,url,username,password,t):
        driver = self.driver
        f = Funciones_Globales(driver)  # 2. Estas 2 primeras lineas siempre se deben hacer, para que se vinculen con el Funciones.py
        f.Navegar(url, t)
        f.TextoByXPath("//input[@id='user-name']", username, t)
        f.TextoByID("password", password, t)
        f.ClickByXPath("//input[@id='login-button']", t)
        return t