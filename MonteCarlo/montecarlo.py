import random
import tkinter as tk
from tkinter import ttk

def integracion_monte_carlo(n):
    limite_inferior = 2
    limite_superior = 3
    f = lambda x: 3*x**2 + 2*x

    total = 0
    contador_dentro = 0

    for _ in range(n):
        x = random.uniform(limite_inferior, limite_superior)
        y = random.uniform(0, f(3))  # Estimación superior para y

        if limite_inferior <= x <= limite_superior and 0 <= y <= f(x):
            contador_dentro += 1

    aproximacion_integral = (contador_dentro / n) * (limite_superior - limite_inferior) * f(3)

    return aproximacion_integral

def calcular_integral():
    n = int(entrada_simulaciones.get())
    resultado_real = (3/3)*3**3 + (2/2)*3**2 - (3/3)*2**3 - (2/2)*2**2  # Valor matemático de la integral
    aproximacion = integracion_monte_carlo(n)
    porcentaje_error = ((resultado_real - aproximacion) / resultado_real) * 100

    resultado_matematico.config(text=f"Resultado matemático de la integral: {resultado_real}")
    resultado_aproximado.config(text=f"Resultado aproximado de la integral por el método de Monte Carlo: {aproximacion:.2f}")
    porcentaje_error_label.config(text=f"Porcentaje de error entre el valor real y el valor aproximado: {porcentaje_error:.2f}%")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Integral por Método de Monte Carlo")
ventana.config(bg='gray15')  # Establecer color de fondo a gris oscuro

# Ajustar tamaño de la ventana y la fuente
ventana.geometry("600x250")
ventana.option_add('*Font', 'TkDefaultFont 12')

# Crear etiqueta y entrada para el número de simulaciones
etiqueta_simulaciones = ttk.Label(ventana, text="Número de simulaciones:", foreground='white', background='gray15')
etiqueta_simulaciones.pack(pady=10)

entrada_simulaciones = ttk.Entry(ventana)
entrada_simulaciones.pack(pady=5)

# Crear botón para calcular la integral
boton_calcular = ttk.Button(ventana, text="Calcular", command=calcular_integral)
boton_calcular.pack(pady=10)

# Crear etiquetas para mostrar los resultados
resultado_matematico = ttk.Label(ventana, text="Resultado matemático de la integral:", foreground='white', background='gray15', justify=tk.LEFT)
resultado_matematico.pack(pady=10)

resultado_aproximado = ttk.Label(ventana, text="Resultado aproximado de la integral por el método de Monte Carlo:", foreground='white', background='gray15', justify=tk.LEFT)
resultado_aproximado.pack(pady=5)

porcentaje_error_label = ttk.Label(ventana, text="Porcentaje de error entre el valor real y el valor aproximado:", foreground='white', background='gray15', justify=tk.LEFT)
porcentaje_error_label.pack(pady=5)

# Iniciar el bucle de eventos
ventana.mainloop()