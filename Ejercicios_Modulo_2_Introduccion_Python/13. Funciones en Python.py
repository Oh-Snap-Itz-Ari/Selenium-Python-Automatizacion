# FUNCIONES SIMPLES

# 1. Se crea una función que no recibe ningun valor, imprime un mensaje y realiza una suma
def bienvenida():
    a = 5
    b = 10
    c = a+b
    print("\n¡Bienvenido al sistema espero tengas un buen día!\n\nLa suma de las variables A ({}) y B ({}) es {}".format(a,b,c))

# 2. Se imprime un texto informativo y luego se llama la función
print("\nEsto es una función:")
bienvenida()

# FUNCIONES CON PARAMETROS

def saludo (nombre):
    print("\n¡Bienvenido al sistema "+nombre+"!")

def salir (nombre):
    print("\nEs una lastima que te tengas que ir "+nombre+" esperamos verte de nuevo pronto")

def suma (a,b):
    c = a+b
    print("\nEl resultado de la suma entre A ({}) y B ({}) es igual a {}".format(a,b,str(c)))

# 1. Se comienza con la ejecución de las funciones

print("\n Ingresa tu nombre para poder ingresar al sistema")
nombre = input()

saludo(nombre)

print("\nIngresa el valor de A: ")
a = input()
a = int(a)

print("Ingresa el valor de B: ")
b = input()
b = int(b)

suma(a,b)
salir(nombre)
