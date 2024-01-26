import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2

        if num2 != 0:
            division = num1 / num2
            entry_resultado.delete(0, tk.END)
            entry_resultado.insert(0, f"Suma: {suma:.2f}\nResta: {resta:.2f}\nMultiplicación: {multiplicacion:.2f}\nDivisión: {division:.2f}")
        else:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x200")

# Crear etiquetas y entradas
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="E")

entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="E")

entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular, bg="green", fg="white")
boton_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Entrada para mostrar el resultado
entry_resultado = tk.Entry(ventana, width=30, state="readonly", justify="center")
entry_resultado.grid(row=3, column=0, columnspan=2, pady=5)

# Iniciar el bucle principal de la ventana
ventana.mainloop()