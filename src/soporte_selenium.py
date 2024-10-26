from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from time import sleep
from selenium import webdriver  
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import Select  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
import re
import sys

def obtener_supermercados():
    driver = webdriver.Chrome()
    url = 'https://super.facua.org/'
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, '#rcc-confirm-button').click()
    links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Acceder")
    
    supermercados = []
    for link in links:
        supermercados.append(link.get_attribute("href"))
    
    driver.quit()
    return supermercados


def obtener_urls_productos(supermercados, categorias):
    urls_totales = []

    for supermercado in supermercados:
        for categoria in categorias:
            url = f'{supermercado}{categoria}/'             #le añado la categoria  que queremos
            res = requests.get(url)
            
            if res.status_code != 200:
                continue
                
            sopa_actividades = BeautifulSoup(res.content, "html.parser")
            lista_productos = sopa_actividades.findAll("div", {'class': 'card-footer p-4 pt-0 border-top-0 bg-transparent'})
            
            for producto in lista_productos:
                urls = producto.findAll('a', href=True)
                for url in urls:
                    clean_url = url['href']
                    urls_totales.append(clean_url)
    
    return urls_totales

def obtener_datos_supermercados(urls):
    lista_de_tuplas = []
    
    for url in urls:
        res = requests.get(url)
        if res.status_code == 200:
            print(f"Solicitud exitosa para {url}")
        else:
            print(f"Error en la solicitud para {url}")
            continue
        
        sopa = BeautifulSoup(res.content, "html.parser")
        lista_productos = sopa.findAll('tbody')
        
        for i in lista_productos:
            filas = i.findAll("tr")
            for fila in filas:
                lista_td = fila.findAll("td")
                lista_h2 = fila.findAll('h2')
                lista_intermedia = [elemento.text for elemento in lista_td]
                lista_intermedia.extend(url.split("/")[3:6])
                lista_de_tuplas.append(lista_intermedia)
    
    df_mercado = pd.DataFrame(lista_de_tuplas)
    df_mercado.columns = ['fecha', 'Precio', 'Porcentaje de subida', 'Supermercado', 'Categoria', 'Producto']
    df_mercado['Categoria'] = df_mercado['Categoria'].str.replace('-', ' ')
    df_mercado['Producto'] = df_mercado['Producto'].str.replace('-', ' ')
    df_mercado['Precio'] = df_mercado['Precio'].str.replace(',', '.')
    
    return df_mercado

