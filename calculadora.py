def calculadora(op, num1, num2):
    if op == "suma":
        resultado = num1 + num2
    elif op == "resta":
        resultado = num1 - num2
    elif op == "multiplicacion":
        resultado = num1 * num2
    elif op == "division":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "No se puede dividir entre 0"
    else:
        return "Operación no válida"
    
    return resultado

# Ejemplo de uso:
texto1 = float(input("Ingrese el primer número: "))
texto2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ")

resultado = calculadora(operacion, texto1, texto2)
print("Resultado:", resultado)