import tkinter as tk
from math import sqrt

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("360x590")

        self.resultado_var = tk.StringVar()
        self.resultado_var.set("0")

        self.interfaz()

    def interfaz(self):
        pantalla = tk.Entry(self, textvariable=self.resultado_var, font=('Arial', 24), bd=10, insertwidth=4, width=14,
                            justify='right')
        pantalla.grid(row=0, column=0, columnspan=4)

        botones = [
            ('7', '#4CAF50', 'white'), ('8', '#4CAF50', 'white'), ('9', '#4CAF50', 'white'), ('/', '#FFA500', 'white'),
            ('4', '#4CAF50', 'white'), ('5', '#4CAF50', 'white'), ('6', '#4CAF50', 'white'), ('*', '#FFA500', 'white'),
            ('1', '#4CAF50', 'white'), ('2', '#4CAF50', 'white'), ('3', '#4CAF50', 'white'), ('-', '#FFA500', 'white'),
            ('0', '#4CAF50', 'white'), ('.', '#4CAF50', 'white'), ('%', '#FFA500', 'white'), ('+', '#FFA500', 'white'),
            ('lim', '#4B0082', 'white'), ('C', 'red', 'white'),  ('=', '#008000', 'white'),
            ('^', '#4CAF50', 'white'), ('+/-', '#4CAF50', 'white'), ('√', '#4CAF50', 'white')  # Botón de raíz cuadrada
        ]

        row_val = 1
        col_val = 0

        for bon_tex, color_fondo, color_texto in botones:
            tk.Button(self, text=bon_tex, padx=20, pady=20, font=('Arial', 18),
                      command=lambda text=bon_tex: self.pulsar_boton(text),
                      bg=color_fondo, fg=color_texto).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def pulsar_boton(self, texto):
        if texto == 'lim':
            self.resultado_var.set("0")
        elif texto == 'C':
            self.resultado_var.set(self.resultado_var.get()[:-1])
            if not self.resultado_var.get():
                self.resultado_var.set("0")
        elif texto == '=':
            try:
                resultado = eval(self.resultado_var.get())
                self.resultado_var.set(str(resultado))

            except ZeroDivisionError:
                self.resultado_var.set("Mal :(")

            except Exception as e:
                self.resultado_var.set("Mal :(")
                
        elif texto == 'sqrt':
            num = float(self.resultado_var.get())
            if num < 0:
                self.resultado_var.set("Mal :(")
            else:
                self.resultado_var.set(str(sqrt(num)))
        elif texto == '^':
            self.resultado_var.set(str(float(self.resultado_var.get())**2))  # Eleva al cuadrado, puedes ajustar según tus necesidades
        elif texto == '+/-':
            current_value = float(self.resultado_var.get())
            new_value = current_value * -1
            self.resultado_var.set(str(new_value))
        elif texto == '√':
            num = float(self.resultado_var.get())
            if num < 0:
                self.resultado_var.set("Mal :(")
            else:
                self.resultado_var.set(str(sqrt(num)))
        else:
            if self.resultado_var.get() == "0" or self.resultado_var.get() == "Mal :(":
                self.resultado_var.set(texto)
            else:
                self.resultado_var.set(self.resultado_var.get() + texto)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
