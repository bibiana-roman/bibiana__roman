import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class actividad_3:
    def __init__(self):
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/poo_2025/".format(self.ruta_raiz) #os.path.join(self.ruta_raiz, "src", "poo_2025")
        self.archivo_csv = os.path.join(self.ruta_act2, "winemag-data-130k-v2.csv")

        datos = {
            "Numero_punto": [1,2,3,4,5,6,7,8,9,10,11,12],
            "Resultado": [0,0,0,0,0,0,0,0,0,0,0,0]
        }
        self.df = pd.DataFrame(datos)
        #print(self.ruta_raiz)

    def cargar_csv(self):
        """ Método centralizado para leer el archivo CSV de manera segura. """
        if not os.path.exists(self.archivo_csv):
            print(f"Error: El archivo no existe en la ruta {self.archivo_csv}")
            return None
        print(f"Cargando archivo: {self.archivo_csv}")
        return pd.read_csv(self.archivo_csv)
    
    def punto_1(self):
        frutas = pd.DataFrame([[20, 50]], columns=["Granadilla", "Tomates"])
        self.df.loc[0,"Resultado"] = "punto_1.csv" #len(frutas)
        frutas.to_csv("punto_1.csv", index=False)#C:\Users\Usuario\Documents\POO_Bibiana_Roman\repositorios\bibiana__roman\src\poo_2025\actividad_3
        print("punto_1\n", frutas)

    def punto_2(self):
        ventas_frutas = pd.DataFrame(
        [[20, 50], [49, 100]], 
        columns = ["Granadilla", "Tomates"], 
        index = ["ventas 2021", "ventas 2022"]
        )
        self.df.loc[1,"Resultado"] = "punto_2.csv" #len(ventas_frutas)
        ventas_frutas.to_csv("punto_2.csv", encoding="utf-8", sep=";", index=True)
        print("punto_2\n", ventas_frutas)    

    def punto_3(self):
        utensilios = pd.Series(
        ["3 unidades", "2 unidades", "4 unidades", "5 unidades"],
        index = ["Cuchara", "Tenedor", "Cuchillo", "Plato"],
        name = "Cocina"
        )
        self.df.loc[2,"Resultado"] = "punto_3.csv"
        utensilios.to_csv("punto_3.csv", encoding="utf-8", sep=";", header=True)
        print("punto_3\n", utensilios)

    def punto_4(self):
        # Construcción de la ruta del archivo CSV
        archivo = os.path.join(self.ruta_act2, "winemag-data-130k-v2.csv")  # Ruta del archivo
        archivo = os.path.abspath(archivo)  # Convertir a ruta absoluta

        #print(f"Intentando leer: {archivo}")  # Depuración

        # Verificar si el archivo existe antes de intentar abrirlo
        if not os.path.exists(archivo):
            print("Error: El archivo no existe en la ruta especificada.")
            return

        # Cargar el archivo en un DataFrame
        review = pd.read_csv(archivo)

        # Mostrar las primeras filas del DataFrame
        print("punto_4 - DataFrame cargado correctamente:")
        print(review.head())  # Muestra las primeras filas 

        # Guardar el resultado en el DataFrame principal
        self.df.loc[3, "Resultado"] = "punto_4.csv" #f"{len(review)} filas"

        review.to_csv("punto_4.csv", index=False, encoding="utf-8")
        print("punto_4\n", review)
        
    def punto_5(self):
        # Cargar el archivo CSV en un DataFrame
        archivo = os.path.join(self.ruta_act2, "winemag-data-130k-v2.csv")
        archivo = os.path.abspath(archivo)  # Convierte en ruta absoluta

        # Verificar si el archivo existe antes de intentar abrirlo
        if not os.path.exists(archivo):
            print(f"Error: El archivo no existe en la ruta especificada ({archivo}).")
            return

        # Cargar el archivo en un DataFrame
        review = pd.read_csv(archivo)

        # Mostrar las primeras filas del DataFrame
        print(review.head().to_string(index=False))  # Muestra las primeras 5 filas

        self.df.loc[4,"Resultado"] = "punto_5.csv"
        review.to_csv("punto_5.csv", index=False, encoding="utf-8")
        print("punto_5\n", review)

    def punto_6(self):
        # Construcción de la ruta del archivo CSV
        archivo = os.path.join(self.ruta_act2, "winemag-data-130k-v2.csv")
        archivo = os.path.abspath(archivo)  # Convertir a ruta absoluta

        # Verificar si el archivo existe antes de intentar abrirlo
        if not os.path.exists(archivo):
            print(f"Error: El archivo no existe en la ruta especificada ({archivo}).")
            return

        # Cargar el archivo en un DataFrame
        review = pd.read_csv(archivo)

        # Obtener información del DataFrame
        print("punto_6 - Información del DataFrame:")
        review.info()

        # Guardar el resultado en el DataFrame principal
        num_filas = review.shape[0]  # Número de filas en el DataFrame
        self.df.loc[5, "Resultado"] = f"{num_filas} filas"

        # Guardar el DataFrame en un archivo CSV de salida
        review.to_csv("punto_6.csv", index=False, encoding="utf-8")
        print(f"punto_6.\n Se encontraron {num_filas} filas.")

    def punto_7(self):
        # Construcción de la ruta del archivo CSV
        archivo = os.path.join(self.ruta_act2, "winemag-data-130k-v2.csv")
        archivo = os.path.abspath(archivo)  # Convertir a ruta absoluta

        # Verificar si el archivo existe antes de intentar abrirlo
        if not os.path.exists(archivo):
            print(f"Error: El archivo no existe en la ruta especificada ({archivo}).")
            return

        # Cargar el archivo en un DataFrame
        review = pd.read_csv(archivo)

        # Calcular el precio promedio, ignorando valores NaN
        precio_promedio = review["price"].mean()

        # Guardar el resultado en el DataFrame principal
        self.df.loc[6, "Resultado"] = round(precio_promedio, 2)

        review.to_csv("punto_7.csv", index=False, encoding="utf-8")
        print(f"punto_7\n - Precio promedio: {precio_promedio:.2f}")

    def punto_8(self):
        # Construcción de la ruta del archivo CSV
        archivo = os.path.join(self.ruta_act2, "winemag-data-130k-v2.csv")
        archivo = os.path.abspath(archivo)  # Convertir a ruta absoluta

        # Verificar si el archivo existe antes de intentar abrirlo
        if not os.path.exists(archivo):
            print(f"Error: El archivo no existe en la ruta especificada ({archivo}).")
            return

        # Cargar el archivo en un DataFrame
        review = pd.read_csv(archivo)

        # Obtener el precio más alto
        precio_maximo = review["price"].max()

        # Guardar el resultado en el DataFrame principal
        self.df.loc[7, "Resultado"] = precio_maximo
        review.to_csv("punto_8.csv", index=False, encoding="utf-8")
        print(f"punto_8 \n - Precio más alto pagado: {precio_maximo:.2f}")

    def punto_9(self):
        # Construcción de la ruta del archivo CSV
        archivo = os.path.join(self.ruta_act2, "winemag-data-130k-v2.csv")
        archivo = os.path.abspath(archivo)  # Convertir a ruta absoluta

        # Verificar si el archivo existe antes de intentar abrirlo
        if not os.path.exists(archivo):
            print(f"Error: El archivo no existe en la ruta especificada ({archivo}).")
            return

        # Cargar el archivo en un DataFrame
        review = pd.read_csv(archivo)

        # Filtrar los vinos de California
        vinos_california = review[review["province"] == "California"]

        # Guardar en un nuevo archivo CSV
        vinos_california.to_csv("vinos_california.csv", index=False, encoding="utf-8")

        # Guardar el resultado en el DataFrame principal
        self.df.loc[8, "Resultado"] = "vinos_california.csv"
        review.to_csv("punto_9.csv", index=False, encoding="utf-8")
        print(f"punto_9 - Se encontraron {len(vinos_california)} vinos de California.")
        print(vinos_california.head(10))  # Muestra las primeras filas como en la imagen
        #print(f"punto_9\n")

    def punto_10(self):
        # Verificar si ya se ha filtrado el DataFrame de California
        archivo = "vinos_california.csv"

        if not os.path.exists(archivo):
            print(f"Error: No se encontró el archivo {archivo}. Ejecuta el punto 9 primero.")
            return

        # Cargar los vinos de California
        vinos_california = pd.read_csv(archivo)

        # Encontrar el índice del vino más caro
        idx_max_precio = vinos_california["price"].idxmax()

        # Obtener la información completa de ese vino
        vino_mas_caro = vinos_california.loc[idx_max_precio]

        print(f"punto_10\n")
        print("El vino más caro de California es:")
        print(vino_mas_caro)
        
        """self.df.loc[9,"Resultado"]
        print("punto_10")"""

    def punto_11(self):

        # Verificar si ya se ha filtrado el DataFrame de California
        archivo = "vinos_california.csv"

        if not os.path.exists(archivo):
            print(f"Error: No se encontró el archivo {archivo}. Ejecuta el punto 9 primero.")
            return

        # Cargar los vinos de California
        vinos_california = pd.read_csv(archivo)

        # Contar la cantidad de vinos por tipo de uva
        variedades_mas_comunes = vinos_california["variety"].value_counts()

        print(f"punto11\n")
        print(variedades_mas_comunes)

        """self.df.loc[10,"Resultado"]
        print("punto_11")"""

    def punto_12(self):
        # Verificar si ya se ha filtrado el DataFrame de California
        archivo = "vinos_california.csv"

        if not os.path.exists(archivo):
            print(f"Error: No se encontró el archivo {archivo}. Ejecuta el punto 9 primero.")
            return

        # Cargar los vinos de California
        vinos_california = pd.read_csv(archivo)

        # Obtener los 10 tipos de uva más comunes
        top_10_variedades = vinos_california["variety"].value_counts().head(10)

        print(f"punto_12\n")
        print(top_10_variedades)
        
        """self.df.loc[11,"Resultado"]
        print("punto_12")"""
                                        
    def ejecutar(self):
        self.punto_1()
        self.punto_2()
        self.punto_3()
        self.punto_4()
        self.punto_5()
        self.punto_6()
        self.punto_7()
        self.punto_8()
        self.punto_9()
        self.punto_10()
        self.punto_11()
        self.punto_12()
        self.df.to_csv("actividad_3.csv")

act = actividad_3()
act.ejecutar()   