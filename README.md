# Proyecto4-AnalisisFacua
![Portada](https://github.com/user-attachments/assets/e31e77fb-da6a-47c6-8bda-b41ec96d72e6)

Bienvenidos! 

# *Es un placer recibirlos*


# 📝 En que consiste:

¡Bienvenidos a un nuevo proyecto¡ Esta vez vamos a realizar un escrapeo de datos de Facua donde vamos a comparar 6 supermercados: Alcampo, Carrefour, Dia, Eroski, Hipercor y Mercadona. Dentro de estos vamos a seleccionar 3 catagerias, aceite de oliva, aceite de girasol y leche.



# Objetivos del proyecto:


Scraping de datos: Extraer información detallada de todos los productos disponibles en la web de FACUA para cada uno de los supermercados listados.

Almacenamiento en base de datos: Crear una base de datos en SQL que almacene la información recolectada de manera estructurada.

Análisis de Datos:

Comparación de Precios entre Supermercados

Análisis de la Evolución de Precios

Detección de Anomalías

Análisis de la Dispersión de Precios

Comparación de Precios Promedio

Visualización de datos

## 🗂️ Estructura del Proyecto
Hemos creado un entorno llamado Webscraping para el siguiente proyecto.

        ├── notebooks/           # Notebooks de Jupyter donde se encontraran la limpieza de los datos y la visualizacion
        ├── src/                 # Scripts de procesamiento y modelado
        ├─  Datos                # Datos, donde estaran los archivos csv que se han obtenido
        ├── README.md            # Descripción del proyecto
        ├── README_English version.md   # Descripción del proyecto en ingles
      
## 🛠️ Instalación y Requisitos
        Este proyecto usa Python 3.12.6.
        Se ha importado la libreria BeautifulSoup
        Se ha importado la libreria requests
        Se ha importado la libreria  pandas 
        Se ha importado la libreria numpy 
        Se ha importado la libreria webdriver  
        Se ha importado la libreria ChromeDriverManager 
        Se ha importado la libreria Keys  
        Se ha importado la libreria Select  
        Se ha importado la libreria WebDriverWait
        Se ha importado la libreria expected_conditions as EC
        Se ha importado la libreria NoSuchElementException 
        Se ha importado la libreria re
        Se ha importado la libreria sys
        Se ha importado la libreria os



# 📝Webs:

    Facua: https://super.facua.org/
 
 
**Resultados , Conclusiones**

En primer lugar tenemos 6 supermercados los cuales analizamos tres categorias de productos obteniendo un total de 135.869 datos.

-Observamos que el producto mas ofertado es el aceite de oliva  en la suma de todos los supermercados. En este caso Aceite de oliva marca carbonel suave es el maximo producto ofertado.

-Al observar supermercado por supermercado vemos que la tendencia es la misma observando que el aceite de girasol es el que menos oferta tiene.

En el historico se puede ver que la leche es el profucto que predomina en los 6 supermercados por delante del aceite de oliva. Individalemte vemos que hay supermercados como puede ser hipercor que no sigue este patron y su oferta historica es predominante el aceite de oliva

-Con respecto a precios medios en el historico:   Eroski seria el supermercado  mas conveniente en aceite de girasol.
                                                  hipercor seria el supermercado  mas conveniente en leche.
                                                  Dia seria el supermercado  mas conveniente en aceite de oliva.

-Con respecto a precios Maximos en el historico:   Carrefour seria el supermercado  mas destacado en aceite de girasol.
                                                   Carrefour  seria el supermercado  mas destacado en leche.
                                                   Hipercor seria el supermercado  mas destacado con casi el doble que los otrosd de precio maximo  en aceite                                                      de oliva.


-Con respecto a precios Minimos en el historico:   Alcampo seria el supermercado  mas destacado en aceite de girasol.
                                                   Alcampo  seria el supermercado  mas destacado en leche.
                                                   Carrefour  seria el supermercado  mas destacado en aceite de oliva.


- Con respecto a las evoluciones de los precios en el historico observamos que en igual medida los precios suben y bajam de manera constante, exventuando el cado de carrefour que tiene picos de subida bastante altos.

-Algo que puede parece sorprendente es la caida de los precios minimos en Alcampo,que tiene picos de bajada en estos muy fuertes, esto puede ser debido a las promociones todo a 1 euro las cuales se estan implementando cada vez mas en estos supermercados.

Anomalias: 

Como hemos dicho antes las anomalias mas claras las tiene Carrefour que el dia 01/09 subio el precio de la leche en un 96% el 02/08 la bajo un 49% y el 08/08 la volvio a subir un 228 %.

Con respecto al aceite de girasol las anomalias mas claras las encontramos en alcampo y carrefour el el que el porcentaje maximo de subida es un 34% en caso de carrefour el dia 02/08 y la bajada mas pronunciada es de un 25% en carrefour el dia 01/09.

Con respecto a las anomalias de del aceite de oliva, son mas constante se juega mas con el precio de este alimento, con subidas y bajadas bruscas a lo largo del historico, deberiamos observar el grafico y la tabla.


- **Próximos Pasos**

 📈 Al scrapear totalmente todo lo que es la pagina web proporcionada, la recoleccion de datos tardo unos 31 minuto por lo que claramente es necesario incluir paralelizacion y asincronia lo que nos permitira reducir proximas recolecciones.

Por otra añadiremos funciones soporte para las viasualizacion de las graficas, no estando estas directamente en el Notebook.

Para finalizar los proximos, pensamos en limpiar los datos de la marca-volumen para poder hacer un analisis mas en profundidad por formato de produco, puesto que esta columna ya estaba incluida en nuestro analisis pero aun no ha sido posible limpiarla.
 
🏍️ 🌟


 

![OIP](https://github.com/user-attachments/assets/a3261f22-9193-45df-bf33-14a396dfd988)
