import pytest
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Ejercicios.Ejercicios_Modulo_8_Pytest.Funciones import Funciones_Globales
from Ejercicios.Ejercicios_Modulo_8_Pytest.Funciones_Login import Funciones_Login

t = .2

def test_completo():
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    fl = Funciones_Login(driver)
    fl.test_1_Login_Correo_Vacio("","Alfamego#123456","Please enter your email",t)
    fl.test_2_Login_Password_Vacio("alexfabianmelo12@hotmail.com","","No customer account found",t)
    fl.test_3_Email_Incompleto("alexfabianmelo12","Alfamego#123456","Wrong email",t)
    fl.test_4_Login_Campos_Vacio("","","Please enter your email",t)
    fl.test_5_Login_Datos_Incorrectos("alexfabianmelo12@hotmail.com","Alfamego#123456","No customer account found",t)
    fl.test_6_Login_Datos_Correctos("admin@yourstore.com","admin","Dashboard",t)


