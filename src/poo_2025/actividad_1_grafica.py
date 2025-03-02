
import sys
import numpy as np
import matplotlib.pyplot as plt

class Actividad_1_grafica():
    def __init__(self):
        self.ruta_static = r"C:src\poo_2025\static"
        sys.stdout.reconfigure(encoding = 'utf-8')

    #def graficar_rectas(self, a, x, n):
        #f = (a * x) ** n
        #print("Funcion calculo: ", f)

    def graficar_rectas(self, a, n):
        x = np.linspace(-10, 10, 400)  # Generar valores de x en el rango de -10 a 10
        y = (a * x) ** n  # Definir la función

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

ingestion = Actividad_1_grafica()
ingestion.graficar_rectas(2, 1)            