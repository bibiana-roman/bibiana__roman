
#from clase_1 import Personas

#persona = Personas()

import json
import requests
import sys

class Actividad_1():
    def __init__(self):
        self.ruta_static = r"C:src\poo_2025\static"
        sys.stdout.reconfigure(encoding = 'utf-8')

    def leer_api(self, url):
        # Realiza una solicitud GET a la API
        response = requests.get(url)    
        
        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Devuelve los datos en formato JSON
            return response.json()
        else:
            # Si hubo un error, devuelve None o maneja el error según sea necesario
            return None

    def escribir_json(self, nombre, datos):
        #r: read, w: write
        ruta_json = "{}.json".format(nombre) 
        with open(file = ruta_json, mode = "w", encoding = "utf-8") as f:
            datos = json.dump(datos, f)
        return datos

ingestion = Actividad_1()
#datos_json = ingestion.leer_api("https://api.github.com/users/octocat")
datos_json = ingestion.leer_api("https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=json&jscmd=data")
print("Datos json: ", datos_json)            