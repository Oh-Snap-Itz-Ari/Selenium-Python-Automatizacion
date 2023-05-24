import pytest
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Ejercicios.Ejercicios_Modulo_8_Pytest.Funciones import Funciones_Globales

t = .2

def test_1_Login_Correo_Vacio():
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)

    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)

    f.TextoMixto("XPATH", "//input[contains(@id,'Email')]", "", t)
    f.TextoMixto("XPATH", "//input[@id='Password']", "Alfamego#123456", t)
    f.ClickMixto("XPATH", "//button[@type='submit'][contains(.,'Log in')]", t)

    elementoError = f.FindElementByXPATH("//span[contains(@id,'Email-error')]")
    elementoError = elementoError.text
    print("\n- Se realiza la prueba y se encuentra el siguiente error -> {}".format(elementoError))

    if (elementoError == "Please enter your email"):
        print("\nLos datos de ingreso estan incompletos, por favor validarlos y volver a intentar")
        f.Salida()
        print("\nPrueba #1 = OK\n\n"
              "-------------------------------------------------------------------------------")
        time.sleep(t)
    driver.close()

def test_2_Login_Password_Vacio():
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)

    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)

    f.TextoMixto("XPATH", "//input[contains(@id,'Email')]", "alexfabianmelo12@hotmail.com", t)
    f.TextoMixto("XPATH", "//input[@id='Password']", "", t)
    f.ClickMixto("XPATH", "//button[@type='submit'][contains(.,'Log in')]", t)

    elementoError = f.FindElementByXPATH("//li[contains(.,'No customer account found')]")
    elementoError = elementoError.text
    print("\n- Se realiza la prueba y se encuentra el siguiente error -> {}".format(elementoError))

    if (elementoError == "No customer account found"):
        print("\nLos datos de ingreso estan incompletos, por favor validarlos y volver a intentar")
        f.Salida()
        print("\nPrueba #2 = OK\n\n"
              "-------------------------------------------------------------------------------")
        time.sleep(t)
    driver.close()

def test_3_Email_Incompleto():
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)

    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)

    f.TextoMixto("XPATH", "//input[contains(@id,'Email')]","alexfabianmelo12", t)
    f.TextoMixto("XPATH", "//input[@id='Password']","Alfamego#123456", t)
    f.ClickMixto("XPATH", "//button[@type='submit'][contains(.,'Log in')]", t)

    elementoError = f.FindElementByXPATH("//span[contains(@id,'Email-error')]")
    elementoError = elementoError.text
    print("\n- Se realiza la prueba y se encuentra el siguiente error -> {}".format(elementoError))

    if (elementoError == "Wrong email"):
        print("\nLa estructura del correo no es valida o esta incompleto, por favor validarlo y volver a intentar")
        f.Salida()
        print("\nPrueba #3 = OK\n\n"
              "-------------------------------------------------------------------------------")
        time.sleep(t)
    driver.close()

def test_4_Login_Campos_Vacio():
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)

    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)

    f.TextoMixto("XPATH", "//input[contains(@id,'Email')]", "", t)
    f.TextoMixto("XPATH", "//input[@id='Password']", "", t)
    f.ClickMixto("XPATH", "//button[@type='submit'][contains(.,'Log in')]", t)

    elementoError = f.FindElementByXPATH("//span[contains(@id,'Email-error')]")
    elementoError = elementoError.text
    print("\n- Se realiza la prueba y se encuentra el siguiente error -> {}".format(elementoError))

    if (elementoError == "Please enter your email"):
        print("\nLos datos de ingreso estan incompletos, por favor validarlos y volver a intentar")
        f.Salida()
        print("\nPrueba #4 = OK\n\n"
              "-------------------------------------------------------------------------------")
        time.sleep(t)
    driver.close()

def test_5_Login_Datos_Incorrectos():
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)

    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)

    f.TextoMixto("XPATH","//input[contains(@id,'Email')]","alexfabianmelo12@hotmail.com",t)
    f.TextoMixto("XPATH","//input[@id='Password']","Alfamego#123456",t)
    f.ClickMixto("XPATH","//button[@type='submit'][contains(.,'Log in')]",t)

    elementoError = f.FindElementByXPATH("//li[contains(.,'No customer account found')]")
    elementoError = elementoError.text
    print("\n- Se realiza la prueba y se encuentra el siguiente error -> {}".format(elementoError))

    if (elementoError == "No customer account found"):
        print("\nLos datos de ingreso no son correctos, por favor validarlos y volver a intentar")
        f.Salida()
        print("\nPrueba #5 = OK\n\n"
              "-------------------------------------------------------------------------------")
        time.sleep(t)
    driver.close()

def test_6_Login_Datos_Correctos():
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)

    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)

    f.TextoMixto("XPATH","//input[contains(@id,'Email')]","admin@yourstore.com",t)
    f.TextoMixto("XPATH","//input[@id='Password']","admin",t)
    f.ClickMixto("XPATH","//button[@type='submit'][contains(.,'Log in')]",t)

    elementoLogin = f.FindElementByXPATH("//h1[contains(.,'Dashboard')]")
    elementoLogin = elementoLogin.text
    print("\n- Se realiza la prueba, se logra ingresar al sistema y se encuentra en la ventana de -> {}".format(elementoLogin))

    if (elementoLogin == "Dashboard"):
        print("\nSe ingresó al sistema de forma satisfactoria")
        f.Salida()
        print("\nPrueba #6 = OK\n\n"
              "-------------------------------------------------------------------------------")
        time.sleep(t)
    driver.close()
