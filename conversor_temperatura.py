# se le pedira al usuario la cantidad de grados celsius a grados fahrenheit
temperatura = float(input("ingrese la cantidad de grados Cº que desea convertir a grados Fº: "))

# se utiliza la formula matematica para convertir los grados celsius a grados fahrenheit
conversion = temperatura * (9/5) + 32

# se imprime en consola el resultado final de la conversion en grados fahrenheit
print(f"{temperatura} Cº equivalen a {conversion} Fº")
