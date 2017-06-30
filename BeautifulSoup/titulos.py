#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#-----------------------------------------------------------------------------
# Incluimos los módulos necesarios.
#-----------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
 
 

# El usuario escribe la url
url = "https://jarroba.com/"
req = requests.get(url)

status_code = req.status_code
if(status_code == 200):
    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")

    # Obtenemos todos los divs donde están las entradas
    entradas = html.find_all('div', {'class': 'col-md-4 col-xs-12'})
 
    for i, entrada in enumerate(entradas):
        # Con el método "getText()" no nos devuelve el HTML
        titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
        # Sino llamamos al método "getText()" nos devuelve también el HTML
        autor = entrada.find('span', {'class': 'autor'})
        fecha = entrada.find('span', {'class': 'fecha'}).getText()

        # Imprimo el Título, Autor y Fecha de las entradas
        print("%d - %s  |  %s  |  %s" % (i + 1, titulo, autor, fecha))

else:
    print("Status Code %d" % status_code)
