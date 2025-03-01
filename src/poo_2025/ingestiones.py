import json

class Ingestiones():
    def __init__(self):
        self.ruta_static = r"C:\Users\Usuario\Documents\POO_Bibiana_Roman\repositorios\bibiana__roman\src\poo_2025\static"
    
    def leer_json(self):
        #r: read, w: write
        ruta_json = "{}\json\datos_persona.json".format(self.ruta_static) 
        with open(file = ruta_json, mode = "r", encoding = "utf-8") as f:
            datos = json.load(f)
        return datos

inges = Ingestiones()
datos_json = inges.leer_json()
print(datos_json)


