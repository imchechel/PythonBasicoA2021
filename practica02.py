# Ejercicio 1
# ************
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# Variables
clv = "contraseña"
ing = input("Ingresa una contraseña: ")

# Validación e impresión
if clv == ing.lower():
    print("La contraseña ingresada coincide.")
else:
    print("La contrasñea ingresada no coincide.") 


# Ejercicio 2
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo con el sexo y el nombre. 
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
# posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

# Variables
nom = input("¿Cuál es tu nombre? ")
sex = input("¿Cuál es tu sexo (M o F? ")

# Validación e impresión
if sex == "F":
    if nom.lower() < "m":
        grp = "A"
    else:
        grp = "B"
else:
    if nom.lower() > "n":
        grp = "A"
    else:
        grp = "B"

print("El grupo al que pertenece es: " + grp)