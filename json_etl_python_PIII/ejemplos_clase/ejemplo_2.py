#!/usr/bin/env python
'''
JSON ETL [Python]
Ejemplos de clase
---------------------------
Autor: Ing.Jesús González
Version: 2.0

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Ing.Jesús Matías González"
__email__ = "ingjesusmrgonzalez@gmail.com"
__version__ = "2.0"


import json
import requests


if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    #
    print('# ---- Ejemplos con JSON Request ---- #')

    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    # Se puede obtener el objeto JSON de dos formas distintas
    data = json.loads(response.text)
    data = response.json()
    print('Imprimir los datos traídos de la nube')
    print(json.dumps(data, indent=4))

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()

    for user in data:
        if user['userId'] > 2:
            # No mostrar más de 2 usuarios
            # para no ocupar toda la pantalla con mensajes
            break
        print('El usuario {} completó {}? {}'.format(user['userId'],
                                                      user['title'],
                                                      user['completed']
                                                      ))

    print("terminamos")
