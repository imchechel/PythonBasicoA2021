#Ejercicio 1
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

#variable a almacenar el número que ingrese el usuario
num = int(input("indica un numero: "))

#ciclo para recorrer el número ingresado y pintar en consola los asteriscos
for x in range(num):
    for y in range(num):
        if y <= x:
            print("*", end = "")
        if y == x:
            print("")


#Ejercicio 2
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

#variable a almacenar el número que ingrese el usuario
num = int(input("indica un número: "))
x = 2
while num % x != 0:
    x += 1
if x == num:
    print(str(num) + " es un número primo")
else:
    print(str(num) + " no es un número primo")