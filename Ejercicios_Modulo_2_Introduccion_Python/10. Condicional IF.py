# 1. Se solicita por teclado el valor A y B

print("\nIngresa el valor de A: ")
a = input()
a = int(a)

print("Ingresa el valor de B: ")
b = input()
b = int(b)

# 2. Se imprime dependiendo si el valor de A es mayor o menor que el valor de B (Importante que el print no quede debajo del if)

if (a<=b):
    print("\nEl valor de A ({}) es menor o igual que el valor de B ({})".format(a,b))
else:
    print("\nEl valor de A ({}) es mayor o igual que el valor de B ({})".format(a,b))

# 2. Se imprime dependiendo si el valor de A es igual o diferente que el valor de B

if (a==b):
    print("\nEl valor de A ({}) es igual que el valor de B ({})".format(a, b))
else:
    print("\nEl valor de A ({}) no es igual que el valor de B ({})".format(a, b))

# 2. Se imprime dependiendo si el valor de A es diferente o igual que el valor de B

if (a!=b):
    print("\nEl valor de A ({}) es diferente que el valor de B ({})".format(a, b))
else:
    print("\nEl valor de A ({}) igual que el valor de B ({})".format(a, b))