def generar_n_caracteres(n, caracter):
    resultado = ""
    for _ in range(n):
        resultado += caracter
    return resultado

# Ejemplo de uso
print(generar_n_caracteres(5, "x"))  # Debería devolver "xxxxx"
