import tkinter as tk
from tkinter import messagebox

def es_numero(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

def realizar_operacion(operacion):
    try:
        if not es_numero(entry_num1.get()) or not es_numero(entry_num2.get()):
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")
            return
        

        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operacion == 'Suma':
            resultado = num1 + num2
        elif operacion == 'Resta':
            resultado = num1 - num2
        elif operacion == 'Multiplicación':
            resultado = num1 * num2
        elif operacion == 'División':
            if num2 != 0:
                resultado = num1 / num2
            else:
                messagebox.showerror("Error", "No se puede dividir entre cero.")
                return

        entry_resultado.config(state=tk.NORMAL)
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, f"Resultado de {operacion}: {resultado:.2f}")
        entry_resultado.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x250")


label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="E")

entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="E")

entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

boton_suma = tk.Button(ventana, text="Suma", command=lambda: realizar_operacion('Suma'), bg="blue", fg="white")
boton_suma.grid(row=2, column=0, padx=5, pady=5)

boton_resta = tk.Button(ventana, text="Resta", command=lambda: realizar_operacion('Resta'), bg="orange", fg="white")
boton_resta.grid(row=2, column=1, padx=5, pady=5)

boton_multiplicacion = tk.Button(ventana, text="Multiplicación", command=lambda: realizar_operacion('Multiplicación'), bg="purple", fg="white")
boton_multiplicacion.grid(row=3, column=0, padx=5, pady=5)

boton_division = tk.Button(ventana, text="División", command=lambda: realizar_operacion('División'), bg="red", fg="white")
boton_division.grid(row=3, column=1, padx=5, pady=5)

entry_resultado = tk.Entry(ventana, width=30, state="readonly", justify="center")
entry_resultado.grid(row=4, column=0, columnspan=2, pady=5)

ventana.mainloop()
