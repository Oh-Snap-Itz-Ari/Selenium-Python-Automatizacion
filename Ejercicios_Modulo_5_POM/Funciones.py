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

class Funciones_Globales (): # 1. Se crea la clase Funciones_Globales y se crea la inicialización dentro de esta
    def __init__(self,driver):
        self.driver = driver

    def Navegar(self,url,tiempo):
        self.driver.get(url) # 2. Espera a que se le envie url a través de la función Navegar
        self.driver.maximize_window()
        t = time.sleep(tiempo)
        return t

    def TextoByXPath(self,xpath,texto,tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath))) # 3. Busca el elemento
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val) # 4. Si lo encuentra va hacia el elemento
            val = self.driver.find_element(By.XPATH, (xpath)) # 5. Selecciona el elemento a través de su XPath
            val.clear()  # 6. Permite limpiar el campo por si tiene algún valor escrito
            val.send_keys(texto)  # 7. Recibe el valor de texto en la función y lo escribe sobre el elemento
            t = time.sleep(tiempo)  # 8. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontró el elemento:\n- " + xpath)
            return t

    def TextoByID(self,id,texto,tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 9. Si lo encuentra va hacia el elemento
            val = self.driver.find_element(By.ID, (id))
            val.clear()  # 10. Permite limpiar el campo por si tiene algún valor escrito
            val.send_keys(texto)  # 11. Recibe el valor de texto en la función y lo escribe sobre el elemento
            t = time.sleep(tiempo)  # 12. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontró el elemento:\n- " + id)
            return t

    def ClickByXPath(self,xpath,tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath))) # 13. Busca el elemento
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val) # 14. Si lo encuentra va hacia el elemento
            val = self.driver.find_element(By.XPATH, (xpath)) # 15. Selecciona el elemento a través de su XPath
            val.click()
            t = time.sleep(tiempo)  # 16. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontró el elemento:\n- " + xpath)
            return t

    def ClickByID(self,id,tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, id))) # 13. Busca el elemento
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val) # 14. Si lo encuentra va hacia el elemento
            val = self.driver.find_element(By.XPATH, (id)) # 15. Selecciona el elemento a través de su XPath
            val.click()
            t = time.sleep(tiempo)  # 16. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontró el elemento:\n- " + id)
            return t