
import sys
import numpy as np
import matplotlib.pyplot as plt
import os

#src\poo_2025\static
class Actividad_2_graficas():
    def __init__(self):
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/poo_2025/".format(self.ruta_raiz)
        print(self.ruta_raiz)

    def punto_11(self, num = 100):
        # Genera dos arrays de tamaño 100 con números aleatorios y crea un gráfico de dispersión.
        x = np.random.rand(num)
        y = np.random.rand(num)
        plt.scatter(x, y)
        ruta = "{}Grafica_punto_11.png".format(self.ruta_act2)
        plt.savefig(ruta)
        #plt.savefig("punto_11.png")

    def punto_12(self):
        # Genera un gráfico de dispersión para y = sin(x) + ruido Gaussiano
        x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
        y = np.sin(x) + np.random.normal(0, 0.1, 100)
        plt.scatter(x, y)
        #plt.plot(x, np.sin(x), color='red', label='sin(x)')
        #plt.legend()
        #plt.show()
        ruta = "{}Grafica_punto_12.png".format(self.ruta_act2)
        plt.savefig(ruta)

    def punto_13(self):
        # Utiliza np.meshgrid para crear una cuadrícula y graficar contorno
        x, y = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
        z = np.cos(x) + np.sin(y)
        plt.contour(x, y, z)
        plt.show()
        ruta = "{}Grafica_punto_13.png".format(self.ruta_act2)
        plt.savefig(ruta)

    def punto_14(self):
        # Gráfico de dispersión con densidad de color
        dens_x = np.random.randn(1000)
        dens_y = np.random.randn(1000)
        plt.scatter(dens_x, dens_y, c=dens_x + dens_y, cmap='viridis')
        plt.colorbar()
        plt.show()
        ruta = "{}Grafica_punto_14.png".format(self.ruta_act2)
        plt.savefig(ruta)

    def punto_15(self):
        # Crea un histograma de una distribución normal.
        data = np.random.randn(1000)
        plt.hist(data, bins=30)
        plt.show()
        ruta = "{}Grafica_punto_15.png".format(self.ruta_act2)
        plt.savefig(ruta)   

    def punto_16(self):
        # Dos distribuciones normales en un mismo histograma.
        data1 = np.random.normal(0, 1, 1000)
        data2 = np.random.normal(3, 1, 1000)
        plt.hist(data1, bins=30, alpha=0.5, label='Distribución 1')
        plt.hist(data2, bins=30, alpha=0.5, label='Distribución 2')
        plt.legend()
        plt.show()
        ruta = "{}Grafica_punto_16.png".format(self.ruta_act2)
        plt.savefig(ruta)

    def punto_17(self):
        # Experimenta con diferentes valores de bins en un histograma.
        data = np.random.randn(1000)
        plt.hist(data, bins=10, alpha=0.5, label='10 bins')
        plt.hist(data, bins=30, alpha=0.5, label='30 bins')
        plt.hist(data, bins=50, alpha=0.5, label='50 bins')
        plt.legend()
        plt.show()
        ruta = "{}Grafica_punto_17.png".format(self.ruta_act2)
        plt.savefig(ruta)

    def punto_18(self):
        data = np.random.randn(1000)
        # Crear la figura
        plt.figure(figsize=(10, 5))
        # Histogramas con diferentes valores de bins
        plt.hist(data, bins=10, alpha=0.5, label='10 bins')
        plt.hist(data, bins=30, alpha=0.5, label='30 bins')
        plt.hist(data, bins=50, alpha=0.5, label='50 bins')
        # Etiquetas y título
        plt.xlabel("Valores")
        plt.ylabel("Frecuencia")
        plt.title("Comparación de histogramas con diferentes bins")
        plt.legend()
        # Mostrar gráfico
        plt.show()
        ruta = "{}Grafica_punto_18.png".format(self.ruta_act2)
        plt.savefig(ruta)                 

    def punto_19(self):
        data = np.random.randn(1000)

        # Calcular la media de los datos
        media = np.mean(data)

        # Crear la figura
        plt.figure(figsize=(10, 5))

        # Histogramas con diferentes valores de bins
        plt.hist(data, bins=10, alpha=0.5, label='10 bins')
        plt.hist(data, bins=30, alpha=0.5, label='30 bins')
        plt.hist(data, bins=50, alpha=0.5, label='50 bins')

        # Línea vertical para la media
        plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media: {media:.2f}')

        # Etiquetas y título
        plt.xlabel("Valores")
        plt.ylabel("Frecuencia")
        plt.title("Comparación de histogramas con diferentes bins y media")
        plt.legend()

        # Mostrar gráfico
        plt.show()
        ruta = "{}Grafica_punto_19.png".format(self.ruta_act2)
        plt.savefig(ruta)

    def punto_20(self):
        data1 = np.random.randn(1000)  # Distribución normal centrada en 0
        data2 = np.random.randn(1000) + 3  # Distribución normal desplazada a la derecha

        # Crear la figura
        plt.figure(figsize=(10, 5))

        # Histogramas superpuestos con colores y transparencias diferentes
        plt.hist(data1, bins=30, alpha=0.5, color='blue', label='Distribución 1 (Media = 0)')
        plt.hist(data2, bins=30, alpha=0.5, color='orange', label='Distribución 2 (Media = 3)')

        # Etiquetas y título
        plt.xlabel("Valores")
        plt.ylabel("Frecuencia")
        plt.title("Histogramas Superpuestos de Dos Distribuciones")
        plt.legend()

        # Mostrar gráfico
        plt.show()
        ruta = "{}Grafica_punto_20.png".format(self.ruta_act2)
        plt.savefig(ruta)
    

act = Actividad_2_graficas()
act.punto_11()
act.punto_12()
act.punto_13()
act.punto_14()
act.punto_15()
act.punto_16()
act.punto_17()
act.punto_18()
act.punto_19()
act.punto_20()

