# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado

    mipersona = {
                  "nombre": "Jesus",
                  "apellido": "Gonzalez",
                  "DNI": "26701556",
                  "elementos_vestir": [
                      {
                       "prenda": "chaleco", 
                       "cantidad": 4
                      },
                      {
                       "prenda": "zapato",
                       "cantidad": 12
                      }
                      ]
                   }

    with open('mi_persona_json.json', 'w') as jsonfile:
        data = [mipersona]
        json.dump(data, jsonfile, indent=4)

def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior

    mipersona = {
                  "nombre": "Jesus",
                  "apellido": "Gonzalez",
                  "DNI": "26701556",
                  "elementos_vestir": [
                      {
                       "prenda": "chaleco", 
                       "cantidad": 4
                      },
                      {
                       "prenda": "zapato",
                       "cantidad": 12
                      }
                      ]
                   }

    with open('mi_persona_json.json', 'r') as jsonfile:
        current_data = json.load(jsonfile)
        current_data.append(mipersona)

    with open('mi_persona_json.json', 'w') as jsonfile:
        json.dump(current_data, jsonfile, indent=4)

    with open('mi_persona_json.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

    print('Mostrar el contenido del archivo mi_persona_json')
    print(json.dumps(json_data, indent=4))


if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    
    serializar()
    deserializar()

    print("terminamos")