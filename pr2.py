def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

# Ejemplo de uso
numero1 = 15
numero2 = 30
numero3 = 45
resultado = max_de_tres(numero1, numero2, numero3)
print(f"El número mayor entre {numero1}, {numero2} y {numero3} es {resultado}")
