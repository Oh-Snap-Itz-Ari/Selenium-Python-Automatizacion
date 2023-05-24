import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Ejercicios.Ejercicios_Modulo_7_Mouse_Actions.Funciones import Funciones_Globales
from selenium.webdriver import ActionChains # 1. Es importante añadir esto para las funciones del Mouse Actions

t = 1

class MouseActions(unittest.TestCase):
    def setUp(self):
        ser = Service("C:\Drivers\chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.maximize_window()

    def test_1(self): # 2. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver)
        act = ActionChains(driver) # 3. Se almacena dentro de la variable act el driver de ActionChains
        f.Navegar("https://www.browserstack.com/",t)

        Developers = driver.find_element(By.XPATH,("//span[@class='nav_item_name'][contains(.,'Developers')]"))
        Products = driver.find_element(By.XPATH,("//button[@id='product-menu-toggle']"))
        Live = driver.find_element(By.XPATH,("(//div[@class='dropdown-link-heading'][contains(.,'Live')])[1]"))
        AppAutomate = driver.find_element(By.XPATH,("(//div[@class='dropdown-link-heading'][contains(.,'App Automate')])[1]"))

        # 4. El move_to_element se encarga de simular el comportamiento del puntero, de ponerlo encima del elemento más no dar clic
        # 5. en el caso de move_to_element(AppAutomate).click() pone el puntero sobre el elemento y luego le da click

        act.move_to_element(Developers).move_to_element(Products).move_to_element(Live).move_to_element(AppAutomate).click().perform()

        f.Salida()

    def test_2(self): # 2. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver)
        act = ActionChains(driver) # 3. Se almacena dentro de la variable act el driver de ActionChains
        f.Navegar("https://demoqa.com/buttons",t)

        f.ClickDoble("XPATH","//button[@id='doubleClickBtn']",t)
        f.Navegar("https://demoqa.com/buttons", t)
        f.ClickDoble("ID","doubleClickBtn",t)

        f.Salida()

    def test_3(self): # 2. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver)
        act = ActionChains(driver) # 3. Se almacena dentro de la variable act el driver de ActionChains
        f.Navegar("https://demoqa.com/buttons",t)

        f.ClickDerecho("XPATH","//button[@id='rightClickBtn']",t)
        f.Navegar("https://demoqa.com/buttons", t)
        f.ClickDerecho("ID","rightClickBtn",t)

        f.Salida()

    def test_4(self): # 2. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver)
        act = ActionChains(driver) # 3. Se almacena dentro de la variable act el driver de ActionChains
        f.Navegar("https://testpages.herokuapp.com/styled/drag-drop-javascript.html",t)

        f.DragAndDrop("ID","draggable1","droppable1",t)
        f.DragAndDrop("XPATH","//div[@id='draggable2']","//div[@id='droppable2']",t)

        f.Salida()

    def test_5(self): # 2. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver)
        act = ActionChains(driver) # 3. Se almacena dentro de la variable act el driver de ActionChains
        f.Navegar("https://jqueryui.com/draggable/",t)

        f.DragAndDropXY("XPATH","//div[contains(@id,'draggable')]",150,120,t)
        f.Navegar("https://jqueryui.com/draggable/", t)
        f.DragAndDropXY("ID","draggable",150,120,t)

        f.Salida()

    def test_6(self): # 2. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver)
        act = ActionChains(driver) # 3. Se almacena dentro de la variable act el driver de ActionChains
        f.Navegar("https://jqueryui.com/",t)

        f.ClickXY("XPATH","//a[@href='https://jqueryui.com/demos/'][contains(.,'Demos')]",350,0,t)
        f.ClickXY("XPATH","//a[@href='https://jqueryui.com/demos/'][contains(.,'Demos')]",650,0,t)

        f.Salida()

    def test_7(self): # 2. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver)
        act = ActionChains(driver) # 3. Se almacena dentro de la variable act el driver de ActionChains

        f.Navegar("https://www.google.com.co/",t)
        f.TextoMixto("XPATH","//textarea[contains(@id,'APjFqb')]","Marvel",t)
        f.ClickXY("XPATH","//textarea[contains(@id,'APjFqb')]",0,50,t)

        f.Navegar("https://www.google.com.co/", t)
        f.TextoMixto("ID", "APjFqb", "Marvel", t)
        f.ClickXY("ID", "APjFqb", 0, 150, t)

        f.Salida()

    def test_8(self): # 2. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver)
        act = ActionChains(driver) # 3. Se almacena dentro de la variable act el driver de ActionChains

        f.Navegar("https://demoqa.com/automation-practice-form",t)
        f.TextoMixto("XPATH","//input[contains(@id,'firstName')]","Alex Fabián",t)
        f.TextoMixto("XPATH", "//input[contains(@id,'lastName')]", "Melo Gómez", t)
        f.Copiar("XPATH","//input[contains(@id,'firstName')]",t)
        f.Pegar("XPATH","//textarea[contains(@id,'currentAddress')]",t)

        f.Navegar("https://demoqa.com/automation-practice-form",t)
        f.TextoMixto("ID", "firstName", "Alex Fabián",t)
        f.TextoMixto("ID", "lastName", "Melo Gómez",t)
        f.Copiar("ID", "firstName",t)
        f.Pegar("ID", "currentAddress",t)

        f.Salida()

    def test_9(self): # 2. Es importante que se añada el "test_name" porque sino nos va a dar error
        driver = self.driver
        f = Funciones_Globales(driver)
        act = ActionChains(driver) # 3. Se almacena dentro de la variable act el driver de ActionChains

        f.Navegar("https://demoqa.com/automation-practice-form",t)
        f.TextoMixto("XPATH","//input[contains(@id,'firstName')]","Alex Fabián",t)
        f.TextoMixto("XPATH", "//input[contains(@id,'lastName')]", "Melo Gómez", t)
        f.Copiar("XPATH","//input[contains(@id,'firstName')]",t)
        f.ClickMixto("XPATH","//textarea[contains(@id,'currentAddress')]",t)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).send_keys(" Dirección Residencia").perform()  # 4. El ctrl + v permite pegar

        f.Navegar("https://demoqa.com/automation-practice-form",t)
        f.TextoMixto("ID", "firstName", "Alex Fabián",t)
        f.TextoMixto("ID", "lastName", "Melo Gómez",t)
        f.Copiar("ID", "firstName",t)
        f.ClickMixto("ID", "currentAddress", t)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).send_keys(" Dirección Residencia").perform()  # 4. El ctrl + v permite pegar

        f.Salida()

    def tearDown(self):
        driver = self.driver
        time.sleep(2)
        driver.close()


if __name__ == '__main__':
    unittest.main()