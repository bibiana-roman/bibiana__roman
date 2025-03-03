
import json
import requests
import sys
import numpy as np
import matplotlib.pyplot as plt

class Actividad_1():
    def __init__(self):
        self.ruta_static = r"C:\src\poo_2025\static"
        sys.stdout.reconfigure(encoding = 'utf-8')

#Script para graficar rectas ax ** n
    def graficar_rectas(self, a, n):
        x = np.linspace(-10, 10, 400)  #Generación de valores de x en el rango de -10 a 10
        y = (a * x) ** n  # Definición de la función

        # Graficar 
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f'$f(x) = ({a}x)^{n}$', color="b")
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend()
        plt.title("Gráfica de la función f(x) = (a * x)^n")
        plt.xlabel("X")
        plt.ylabel("f(X)")
        plt.show()

    def escribir_txt(self, nombre_archivo = "", datos = None):
        if nombre_archivo == "":
            nombre_archivo = "datos.txt"
        if datos is None:
            datos = "No hay datos"
        ruta_txt = "{}\txt\{}".format(self.ruta_static, nombre_archivo)
        with open(ruta_txt, "w", encoding = 'utf-8') as f:
            json.dump(datos, f, ensure_ascii = False, indent = 4)
            f.write(str(datos))
        return True        


    def leer_api(self, url):
        # Realiza una solicitud GET a la API
        response = requests.get(url)
        return response.json()    
        
        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Devuelve los datos en formato JSON
            return response.json()
        else:
            # Si hubo un error, devuelve None o maneja el error según sea necesario
            return None

    #def escribir_json(self, nombre, datos):
        #r: read, w: write
        #ruta_json = "{}.json".format(nombre) 
        #with open(file = ruta_json, mode = "w", encoding = "utf-8") as f:
            #datos = json.dump(datos, f)
        #return datos

    def graficar_rectas(self, a, x, n):
        f = (a * x) ** n
        print("Funcion calculo: ", f) 

ingestion = Actividad_1()
#datos_json = ingestion.leer_api("https://api.github.com/users/octocat")
datos_json = ingestion.leer_api("https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=json&jscmd=data")
print("Datos json: ", datos_json)
if ingestion.escribir_txt(nombre_archivo = "Entrega_actividad_1.txt", datos = datos_json):
    print("Se creo el archivo txt")
#print("Esta es la ruta estatica: ", ingestion.ruta_static)
ingestion.graficar_rectas(5, 2)          