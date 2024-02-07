from behave import *
from feature.funcion import funciones
from selenium import webdriver
from selenium.webdriver import Chrome
import time
driver =""
t = 0.2
    #PARA CORRERLO behave feature

@given(u'Navegar al sitio web')
def step_impl(context):
    print(u'STEP: Given Navegar al sitio web')
    context.driver= webdriver.Chrome()
    global driver, f
    f = funciones ()
    f.navegador("https://www.saucedemo.com/", t)


@when(u'Ingresa el nombre de "{user}"')
def step_impl(context, user):
    f.validacion("//input[contains(@id,'user-name')]", user, t)


@when(u'Ingresa la "{contraseña}"')
def step_impl(context, contraseña):
    f.validacion("//input[contains(@id,'password')]", contraseña, t)


@then(u'dar click al boton de aceptar')
def step_impl(context):
    f.cliquear("//input[contains(@id,'login-button')]", t)
    context.driver.close()