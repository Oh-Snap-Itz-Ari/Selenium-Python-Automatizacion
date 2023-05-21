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

    # Función que permite navegar a una URL en concreto
    def Navegar(self,url,tiempo):
        self.driver.get(url) # 2. Espera a que se le envie url a través de la función Navegar
        self.driver.maximize_window()
        print("\nPágina abierta de forma satisfactoria:\n"+str(url))
        t = time.sleep(tiempo)
        return t

    # Función que permite escribir texto, lo anterior a través de la busqueda del selector (XPATH o ID)
    def TextoMixto(self,tipo,selector,texto,tiempo):
        if (tipo == "XPATH"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector))) # 3. Busca el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val) # 4. Si lo encuentra va hacia el elemento
                val = self.driver.find_element(By.XPATH, (selector)) # 5. Selecciona el elemento a través de su XPath
                val.clear()  # 6. Permite limpiar el campo por si tiene algún valor escrito
                val.send_keys(texto)  # 7. Recibe el valor de texto en la función y lo escribe sobre el elemento
                print("\n- Escribiendo en el campo con {} ({}) el texto -> {}".format(tipo,selector,texto))
                t = time.sleep(tiempo)  # 8. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("\n- No se encontró el elemento:\n- " + selector)
                return t

        elif(tipo == "ID"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))  # 3. Busca el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 4. Si lo encuentra va hacia el elemento
                val = self.driver.find_element(By.ID, (selector))  # 5. Selecciona el elemento a través de su XPath
                val.clear()  # 6. Permite limpiar el campo por si tiene algún valor escrito
                val.send_keys(texto)  # 7. Recibe el valor de texto en la función y lo escribe sobre el elemento
                print("\n- Escribiendo en el campo con {} ({}) el texto -> {}".format(tipo,selector,texto))
                t = time.sleep(tiempo)  # 8. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("\n- No se encontró el elemento:\n- " + selector)
                return t

    # Función que permite hacer clic en un elemento en concreto, lo anterior a través de la busqueda del selector (XPATH o ID)
    def ClickMixto(self,tipo,selector,tiempo):
        if (tipo == "XPATH"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector))) # 13. Busca el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val) # 14. Si lo encuentra va hacia el elemento
                val = self.driver.find_element(By.XPATH, (selector)) # 15. Selecciona el elemento a través de su XPath
                val.click()
                print("\n- Se da click en el campo con {} -> ({})".format(tipo,selector))
                t = time.sleep(tiempo)  # 16. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("\n- No se encontró el elemento:\n- " + selector)
                return t

        elif (tipo == "ID"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))  # 13. Busca el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 14. Si lo encuentra va hacia el elemento
                val = self.driver.find_element(By.ID, (selector))  # 15. Selecciona el elemento a través de su XPath
                val.click()
                print("\n- Se da click en el campo con {} -> ({})".format(tipo, selector))
                t = time.sleep(tiempo)  # 16. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("\n- No se encontró el elemento:\n- " + selector)
                return t

    # Función que permite hacer la busqueda y selección de un elemento de una lista desplegable, lo anterior a través de
    # su elemento (XPATH o ID)
    def Select_Mixto_Text(self, tipo, selector, text, tiempo):
        if (tipo == "XPATH"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))  # 13. Busca el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 14. Si lo encuentra va hacia el elemento
                val = self.driver.find_element(By.XPATH, (selector))  # 15. Selecciona el elemento a través de su XPath
                val = Select(val)
                val.select_by_visible_text(text) # 16. Busca y selecciona el valor de text en el listado
                print("\n- El campo seleccionado es -> ({})".format(text))
                t = time.sleep(tiempo)  # 17. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("\n- No se encontró el elemento:\n- " + selector)
                return t

        elif (tipo == "ID"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))  # 13. Busca el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 14. Si lo encuentra va hacia el elemento
                val = self.driver.find_element(By.ID, (selector))  # 15. Selecciona el elemento a través de su XPath
                val = Select(val)
                val.select_by_visible_text(text) # 16. Busca y selecciona el valor de text en el listado
                print("\n- El campo seleccionado es -> ({})".format(text))
                t = time.sleep(tiempo)  # 17. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("\n- No se encontró el elemento:\n- " + selector)
                return t

    # Función que permite hacer la busqueda y selección de un elemento de una lista desplegable (text, index o value),
    # lo anterior a través de su elemento (XPATH o ID)
    def Select_Mixto_Type(self, tipo, selector, type, dato, tiempo):
        if (tipo == "XPATH"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))  # 13. Busca el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 14. Si lo encuentra va hacia el elemento
                val = self.driver.find_element(By.XPATH, (selector))  # 15. Selecciona el elemento a través de su XPath
                val = Select(val)

                if(type == "text"):
                    val.select_by_visible_text(dato)  # 16. Busca y selecciona el valor de text en el listado

                elif(type == "index"):
                    val.select_by_index(dato)

                elif(type == "value"):
                    val.select_by_value(dato)

                print("\n- Se realizó la busqueda a través de ({}) y el campo seleccionado es equivalente a -> ({})".format(type,dato))
                t = time.sleep(tiempo)  # 17. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("\n- No se encontró el elemento:\n- " + selector)
                return t

        elif (tipo == "ID"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))  # 13. Busca el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 14. Si lo encuentra va hacia el elemento
                val = self.driver.find_element(By.ID, (selector))  # 15. Selecciona el elemento a través de su XPath
                val = Select(val)

                if (type == "text"):
                    val.select_by_visible_text(dato)  # 16. Busca y selecciona el valor de text en el listado

                elif (type == "index"):
                    val.select_by_index(dato)

                elif (type == "value"):
                    val.select_by_value(dato)

                print("\n- Se realizó la busqueda a través de ({}) y el campo seleccionado es equivalente a -> ({})".format(type,dato))
                t = time.sleep(tiempo)  # 17. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("\n- No se encontró el elemento:\n- " + selector)
                return t

    # Función que permite subir un archivo especifico de una ruta del computador, lo anterior filtrando el campo a través de
    # su elemento (XPATH o ID)
    def Upload_Mixto(self, tipo, selector, ruta, tiempo):
        if (tipo == "XPATH"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))  # 13. Busca el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 14. Si lo encuentra va hacia el elemento
                val = self.driver.find_element(By.XPATH, (selector))  # 15. Selecciona el elemento a través de su XPath
                val.send_keys(ruta)

                print("\n- Se carga el archivo de forma satisfactoria a través de la busqueda en la ruta -> ({})".format(ruta))
                t = time.sleep(tiempo)  # 17. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("\n- No se encontró el elemento:\n- " + selector)
                return t

        elif (tipo == "ID"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))  # 13. Busca el elemento
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 14. Si lo encuentra va hacia el elemento
                val = self.driver.find_element(By.ID, (selector))  # 15. Selecciona el elemento a través de su XPath
                val.send_keys(ruta)

                print("\n- Se carga el archivo de forma satisfactoria a través de la busqueda en la ruta -> ({})".format(ruta))
                t = time.sleep(tiempo)  # 17. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("\n- No se encontró el elemento:\n- " + selector)
                return t

    # Esta función permite hacer click en varios campos de un formulario, sin importar la cantidad de argumentos que se envie
    def Clic_Multiple_Mixto(self, tipo, tiempo, *args):
        if (tipo == "XPATH"):
            try:
                for num in args: # 13. Recorre la cantidad de argumentos y se almacena este valor dentro de num
                    val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, num)))  # 13. Busca el elemento
                    val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 14. Si lo encuentra va hacia el elemento
                    val = self.driver.find_element(By.XPATH, (num))  # 15. Selecciona el elemento a través de su XPath
                    val.click()
                    print("\n- Se da click en el campo con ({}) -> ({})".format(tipo,num))
                    t = time.sleep(tiempo)  # 16. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                    return t

            except TimeoutException as ex:
                for num in args:
                    print(ex.msg)
                    print("\n- No se encontró el elemento:\n- " + num)

        elif (tipo == "ID"):
            try:
                for num in args:  # 13. Recorre la cantidad de argumentos y se almacena este valor dentro de num
                    val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, num)))  # 13. Busca el elemento
                    val = self.driver.execute_script("arguments[0].scrollIntoView();",val)  # 14. Si lo encuentra va hacia el elemento
                    val = self.driver.find_element(By.ID, (num))  # 15. Selecciona el elemento a través de su XPath
                    val.click()
                    print("\n- Se da click en el campo con ({}) -> ({})".format(tipo,num))
                    t = time.sleep(tiempo)  # 16. Recibe el valor de tiempo y lo implementa una vez que se escribe el texto
                    return t

            except TimeoutException as ex:
                for num in args:
                    print(ex.msg)
                    print("\n- No se encontró el elemento:\n- " + num)

    # Función que realiza una captura de pantalla
    def Screenshot(self, name, tiempo):
        self.driver.get_screenshot_as_file("C:/Users/alexf/Desktop/Automatización Selenium Python/Ejercicios/img/scr/{}.png".format(name))
        print("\nLa Captura ha sido guardada con el nombre -> ({}.png)".format(name))
        t = time.sleep(tiempo)
        return t

    # Función que brinda un mensaje de finalización exitoso
    def Salida(self):
        print("\nLa prueba ha sido finalizada de forma satisfactoria.")