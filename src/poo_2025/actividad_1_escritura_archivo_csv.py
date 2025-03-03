import csv
import sys
import os  # Para manejar rutas correctamente

class Actividad_1_escritura_archivo_csv():
    def __init__(self):
        self.ruta_static = r"C:\src\poo_2025\static"
        sys.stdout.reconfigure(encoding='utf-8')

    def escribir_csv(self, nombre_archivo="frutas.csv", datos=None):
        if datos is None:
            datos = [["No hay datos"]]

        # Ruta corregida usando os.path.join
        ruta_csv = os.path.join(self.ruta_static, "csv", nombre_archivo)

        # Asegurar que la carpeta existe antes de escribir el archivo
        os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)

        with open(ruta_csv, mode="w", encoding="utf-8", newline="") as f:
            escritor = csv.writer(f)
            escritor.writerow(["Fruta", "Color", "Sabor"])  # Encabezados opcionales
            escritor.writerows(datos)  

        print(f"Archivo '{ruta_csv}' guardado correctamente.")

# Datos
frutas = [
    ["Manzana", "Roja", "Dulce"],
    ["Plátano", "Amarillo", "Dulce"],
    ["Lima", "Verde", "Ácida"]
]

# Crear objeto y escribir CSV
actividad = Actividad_1_escritura_archivo_csv()
actividad.escribir_csv("frutas.csv", frutas)
