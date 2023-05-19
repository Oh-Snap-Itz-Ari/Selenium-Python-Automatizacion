#Introducción a las variables

# 1. Declaramos las variables a y b y les damos el valor de 100 y 50 respectivamente
a = 100
b = 50

# 2. Creamos las variables de suma, resta, multiplicación y división y almacenamos en ellas el resultado de cada operación
suma = a+b
resta = a-b
multiplicacion = a*b
division =  a/b

# 3. Creamos variables de tipo String que contengan mis nombres y mis 2 apellidos
nombres  = "Alex Fabián"
apellido1 = "Melo"
apellido2 = "Gómez"

# 3. Imprimimos el resultado de las operaciones, añadiendo un "str" ya que es necesario hacer la transformación a String ya
# que las variable que contienen números no se pueden imprimir asi solas por consola
print("La suma es: "+ str(suma))
print("La resta es: "+ str(resta))
print("La multiplicación es: "+ str(multiplicacion))
print("La división es: "+ str(division))

print("\nMi nombre es: " +nombres + " " +apellido1 + " " +apellido2)

# 4. Imprimimos los tipos de las variables declaradas anteriormente

print("\nLos tipos de datos de las variables son\n")

print(type(a))
print(type(b))
print(type(suma))
print(type(resta))
print(type(multiplicacion))
print(type(division))
print(type(nombres))
print(type(apellido1))
print(type(apellido2))

