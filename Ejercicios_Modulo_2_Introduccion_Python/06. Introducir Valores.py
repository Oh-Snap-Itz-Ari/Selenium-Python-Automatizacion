# 1. Solicitamos el nombre, apellido, valor de A y valor de B por teclado (Se almacenan dentro de un input

print("Ingresa tu nombre completo: ")
nombre = input()

print("Ingresa tus apellidos: ")
apellidos = input()

# 2. En el caso de A y B es necesario que se haga la conversión a entero porque o sino imprime los valores como concatenados

print("Ingresa el valor de A: ")
a = input()
a = int(a)

print("Ingresa el valor de B: ")
b = input()
b = int(b)

suma = a+b

# 3. Se imprimen los valores que se ingresaron por teclado a través de un texto informativo

print("\nBienvenido al sistema {} {}".format(nombre,apellidos))
print("\nEl resultado de la suma entre {} y {} es igual a: {}".format(a,b,suma))