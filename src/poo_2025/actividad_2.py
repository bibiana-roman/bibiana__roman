

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class Actividad_2:
    def __init__(self):
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/poo_2025/actividad_2/".format(self.ruta_raiz)
        print(self.ruta_raiz)

    def punto_01(self):
        # Generar un array de NumPy con valores desde 10 hasta 29.
        array_10_29 = np.arange(10, 30)
        print("Punto 1:")
        print("Array de 10 a 29:", array_10_29)

    def punto_02(self):
        # Calcula la suma de todos los elementos en un array de NumPy de tamaño 10x10 lleno de unos
        array_ones = np.ones((10, 10))
        sum_ones = np.sum(array_ones)
        print("Punto 2:")
        print("Suma de elementos en matriz 10x10 de unos:", sum_ones)

    def punto_03(self):
        # Producto elemento a elemento de dos arrays de tamaño 5, con números aleatorios de 1 a 10
        array1 = np.random.randint(1, 11, 5)
        array2 = np.random.randint(1, 11, 5)
        product_array = array1 * array2
        print("Punto 3:")
        print("Array 1:", array1)
        print("Array 2:", array2)
        print("Producto elemento a elemento:", product_array)

    def punto_04(self):
        # Crea una matriz 4x4 donde cada elemento es igual a i+j, y calcula su inversa
        # Crea una matriz 4x4 aleatoria para asegurar que no sea singular
        matrix_4x4 = np.random.rand(4, 4)  # Matriz con valores aleatorios entre 0 y 1
        # Calcula la inversa
        matrix_inverse = np.linalg.inv(matrix_4x4)
        print("Punto 4:")
        print("Matriz 4x4:\n", matrix_4x4)
        print("Matriz inversa:\n", matrix_inverse)

    def punto_05(self):             
        # Encuentra los valores máximo y mínimo en un array de 100 elementos aleatorios y muestra sus índices
        random_array = np.random.rand(100)  # Números aleatorios entre 0 y 1
        max_value = np.max(random_array)
        min_value = np.min(random_array)
        max_index = np.argmax(random_array)
        min_index = np.argmin(random_array)
        print("Punto 5:")
        print("Valor máximo:", max_value, "en el índice", max_index)
        print("Valor mínimo:", min_value, "en el índice", min_index)



act = Actividad_2()
act.punto_01()
act.punto_02()
act.punto_03()
act.punto_04()
act.punto_05()