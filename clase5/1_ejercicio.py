"""

Crear una función que reciba argumentos indeterminados que
sean alturas de personas, crear una lista y ordenarla de menor a mayor
y devolver la lista ordenada
Usar isinstance para validar que los argumentos sean de tipo numerico

"""

def ordenar_alturas(*args):
    alturas = [] 
    for arg in args:
        if isinstance(arg, (int, float)):
            alturas.append(arg)
        else:
            print(f"Advertencia: Se ignoró el valor '{arg}' por no ser un valor numérico.") 
    alturas.sort()
    return alturas


resultado = ordenar_alturas(1.72, 1.60, 1.82, "metro noventa", 1.55, 1.70)
print("Lista de alturas ordenadas:", resultado)