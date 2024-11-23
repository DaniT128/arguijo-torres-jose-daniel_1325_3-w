def es_palindromo(cadena):
    # Convertimos la cadena a minúsculas y eliminamos espacios
    cadena = cadena.replace(" ", "").lower()
    # Comparamos la cadena con su inversa
    return cadena == cadena[::-1]

# Ejemplo de uso
print(es_palindromo("oscarin"))  # Debería devolver True
print(es_palindromo("payola"))   # Debería devolver False
print(es_palindromo("dani"))  # Debería devolver True
