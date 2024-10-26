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
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors 


def conexion(nombre):
    try:  
        conexion = psycopg2.connect(
        database = nombre,
        user = "postgres",
        password = "admin",
        host = "localhost",
        port = "5432")
        
    except OperationalError as e:
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("La contraseña es erronea")
        elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
            print("Error de conexion")
        else:
            print(f"Ocurrió el error {e}")

    return conexion



def crear_tablas(conexion, cursor):
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Supermercados (
        id_supermercado INT PRIMARY KEY,
        nombre VARCHAR(255)
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos (
        id_producto SERIAL PRIMARY KEY,
        id_supermercado INT,
        categoria VARCHAR(255),
        producto VARCHAR(255),
        marca VARCHAR(255),
        Volumen VARCHAR(255),
        FOREIGN KEY (id_supermercado) REFERENCES Supermercados(id_supermercado)
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Precios (
        id_precio SERIAL PRIMARY KEY,
        id_supermercado INT,
        fecha DATE,
        precio DECIMAL(10, 2),
        porcentaje INT,
        FOREIGN KEY (id_supermercado) REFERENCES Supermercados(id_supermercado)
    );
    ''')
    

def insertar_datos(df_mercado, conexion):
    cursor = conexion.cursor()

    lista_tuplas_mercados = [tuple(fila) for fila in df_mercado[['id_supermercado', 'Supermercado']].values]
    query_insercion_super = '''
    INSERT INTO Supermercados (id_supermercado, nombre)
    VALUES (%s, %s)
    ON CONFLICT (id_supermercado) DO NOTHING;
    '''
    cursor.executemany(query_insercion_super, lista_tuplas_mercados)
    conexion.commit()

    lista_tuplas_productos = [tuple(fila) for fila in df_mercado[['id_supermercado', 'Categoria', 'producto', 'Marca', 'Volumen']].values]
    query_insercion_productos = '''
    INSERT INTO Productos (id_supermercado, categoria, producto, Marca, Volumen)
    VALUES (%s, %s, %s, %s, %s);
    '''
    cursor.executemany(query_insercion_productos, lista_tuplas_productos)
    conexion.commit()

    lista_tuplas_precios = [tuple(fila) for fila in df_mercado[['id_supermercado', 'fecha', 'Precio', 'Porcentaje']].values]
    query_insercion_precios = '''
    INSERT INTO Precios (id_supermercado, fecha, Precio, Porcentaje)
    VALUES (%s, %s, %s, %s);
    '''
    cursor.executemany(query_insercion_precios, lista_tuplas_precios)
    conexion.commit()