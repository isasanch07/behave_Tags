import unittest
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.select import Select

timeout = 3

class funciones():
    
    def __init__(self,):
        driver = webdriver.Chrome()

    #Funcion para abrir el navegador
    def navegador(self, url, segundos):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        print("Pagina abierta " + str(url))
        t = time.sleep(segundos)
        return t
    
    #Mejorando funciones
    def search_Xpath(self, elemento):
        verify = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        verify = self.driver.find_element(By.XPATH, elemento)
        return verify
    
    def search_ID(self, elemento):
        verify = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, elemento)))
        verify = self.driver.find_element(By.ID, elemento)
        return verify
    
    #Funcion para rellenar campos
    def validacion(self, xpath, valor, segundos):
        
        try: 
            verify = self.search_Xpath(xpath)
            verify.send_keys(valor)
            print("Rellenando campos {} cuyo valor es: {} ".format(xpath, valor))
            t = time.sleep(segundos)
            return t
        
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no fue encontrado" + xpath)

    #Funcion para cliquear
    def cliquear(self, xpath, segundos):
        self.driver.find_element(By.XPATH, xpath).click()
        print("Haciendo click de ingreso " + str(xpath))
        t = time.sleep(segundos)      
        return t
    
    #Funcion para encontrar elementos
    def elementos(self, xpath):
        self.driver.find_element(By.XPATH, xpath)
        print("Encontrando elemento: " + xpath)
        time.sleep(2)
    
    #Funcion para seleccionar un elemento, segun un tipo específico, en este caso "text"
    def seleccion(self, xpath, texto, segundos):
        
        try: 
            verify = self.search_Xpath(xpath)
            select = Select(verify)
            select.select_by_visible_text(texto)
            
            print("El campo seleccionado es {}".format(texto))
            t = time.sleep(segundos)
            return t
        
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no fue encontrado" + xpath)

#Funcion para generar los 3 tipos de seleccion, "text, value, index"
    
    def selec_by_Xpath_type(self, xpath, type, value,  segundos):
        
        try: 
            verify = self.search_Xpath(xpath)
            select = Select(verify)
            
            if(type == "text"):
                select.select_by_visible_text(value)
            elif(type == "index"):
                select.select_by_index(value)
            elif(type == "value"):
                select.select_by_value(value)

            print("El campo seleccionado es {}".format(value))
            t = time.sleep(segundos)
            return t
        
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no fue encontrado" + xpath)

    #Funcion para cargar una imagen
    def upload_element_by_Xpath_(self, xpath, path,  segundos):
        
        try: 
            verify = self.search_Xpath(xpath)
            verify.send_keys(path)
            print("Se ha seleccionado una imagen {}".format(path))
            t = time.sleep(segundos)
            return t
        
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no fue encontrado" + xpath)

    #Función para checkbox
    def radio_button_by_Xpath(self, xpath,  segundos):
        
        try: 
            verify = self.search_Xpath(xpath)
            verify.click()
            print("Se ha cliqueado un radio-button {}".format(xpath))
            t = time.sleep(segundos)
            return t
        
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no fue encontrado" + xpath)

    #Funcion para multiples checkbox
    def multiple_checkbox_by_Xpath(self, segundos, *args):
        
        try: 
            for num in args:
                select = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, num)))
                select = self.driver.find_element(By.XPATH, num).click()
                print("Se ha cliqueado un radio-button {}".format(num))
                t = time.sleep(segundos)
                return t
        
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("El elemento no fue encontrado" + num)

    
    
    #Funcion mixta por xpath o id
    def seleccion_mixta(self, type, selector, texto, segundos):
        if(type == "xpath"):
            try: 
                verify = self.search_Xpath(selector)
                verify.send_keys(texto)
                print("El dato ingresado es:  {}".format(texto))
                t = time.sleep(segundos)
                return t
        
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no fue encontrado" + selector)

        elif(type == "id"):
            try: 
                verify = self.search_ID(selector)
                verify.send_keys(texto)
                print("El dato ingresado es:  {}".format(texto))
                t = time.sleep(segundos)
                return t
        
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no fue encontrado" + selector)
