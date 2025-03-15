

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
        print("****Punto 1****")
        print("Array de 10 a 29:\n", array_10_29)

    def punto_02(self):
        # Calcula la suma de todos los elementos en un array de NumPy de tamaño 10x10 lleno de unos
        array_ones = np.ones((10, 10))
        sum_ones = np.sum(array_ones)
        print("****Punto 2****")
        print("Suma de elementos en matriz 10x10 de unos:\n", sum_ones)

    def punto_03(self):
        # Producto elemento a elemento de dos arrays de tamaño 5, con números aleatorios de 1 a 10
        array1 = np.random.randint(1, 11, 5)
        array2 = np.random.randint(1, 11, 5)
        product_array = array1 * array2
        print("****Punto 3****")
        print("Array 1:\n", array1)
        print("Array 2:\n", array2)
        print("Producto elemento a elemento:\n", product_array)

    def punto_04(self):
        # Crea una matriz 4x4 donde cada elemento es igual a i+j, y calcula su inversa
        # Crea una matriz 4x4 aleatoria para asegurar que no sea singular
        matrix_4x4 = np.random.rand(4, 4)  # Matriz con valores aleatorios entre 0 y 1
        # Calcula la inversa
        matrix_inverse = np.linalg.inv(matrix_4x4)
        print("****Punto 4****")
        print("Matriz 4x4:\n", matrix_4x4)
        print("Matriz inversa:\n", matrix_inverse)

    def punto_05(self):             
        # Encuentra los valores máximo y mínimo en un array de 100 elementos aleatorios y muestra sus índices
        random_array = np.random.rand(100)  # Números aleatorios entre 0 y 1
        max_value = np.max(random_array)
        min_value = np.min(random_array)
        max_index = np.argmax(random_array)
        min_index = np.argmin(random_array)
        print("****Punto 5****")
        print("Valor máximo:", max_value, "en el índice", max_index)
        print("Valor mínimo:", min_value, "en el índice", min_index)

    def punto_06(self):
        # Crea un array de tamaño 3x1 y uno de 1x3, y súmalos utilizando broadcasting para obtener un array de 3x3.
        array_3x1 = np.array([[1], [2], [3]])
        array_1x3 = np.array([[1, 2, 3]])
        result_broadcast = array_3x1 + array_1x3
        print("****Punto 6****")
        print("Resultado de broadcasting:\n", result_broadcast)    

    def punto_07(self):
        # 7. De una matriz 5x5, extrae una submatriz 2x2 que comience en la segunda fila y columna.
        matrix_5x5 = np.random.randint(1, 10, (5, 5))
        submatrix_2x2 = matrix_5x5[1:3, 1:3]
        print("****Punto 7****")
        print("Submatriz 2x2:\n", submatrix_2x2)

    def punto_08(self):
        # Crea un array de ceros de tamaño 10 y usa indexado para cambiar el valor de los elementos en el rango de índices 3 a 6 a 5.
        zeros_array = np.zeros(10)
        zeros_array[3:7] = 5
        print("****Punto 8****")
        print("Array con valores modificados:\n", zeros_array)

    def punto_09(self):
        # Dada una matriz de 3x3, invierte el orden de sus filas.
        matrix_3x3 = np.random.randint(1, 10, (3, 3))
        inverted_rows = matrix_3x3[::-1]
        print ("****Punto 9****")
        print("Matriz original:\n", matrix_3x3)
        print("Matriz con filas invertidas:\n", inverted_rows)

    def punto_10(self):
        # Dado un array de números aleatorios de tamaño 10, selecciona y muestra solo aquellos que sean mayores a 0.5.
        random_numbers = np.random.rand(10)
        filtered_numbers = random_numbers[random_numbers > 0.5]
        print ("****Punto 10****")
        print("Valores mayores a 0.5:\n", filtered_numbers)


act = Actividad_2()
act.punto_01()
act.punto_02()
act.punto_03()
act.punto_04()
act.punto_05()
act.punto_06()
act.punto_07()
act.punto_08()
act.punto_09()
act.punto_10()