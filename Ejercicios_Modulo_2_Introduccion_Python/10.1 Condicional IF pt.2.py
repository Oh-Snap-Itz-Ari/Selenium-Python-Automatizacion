# 1. Se solicita por teclado el valor A, B y C

print("\nIngresa el valor de A: ")
a = input()
a = int(a)

print("Ingresa el valor de B: ")
b = input()
b = int(b)

print("Ingresa el valor de C: ")
c = input()
c = int(c)

# 2. Se imprime el resultado según corresponda, en este caso en vez de poner else if se pone elif
print("\nLos valores ingresados son: A = {}, B = {}, y C = {}, entonces decimos que: ".format(a,b,c))

if (a>b and a>c):
    print("\n1. El valor de A ({}) es mayor que el valor de B ({}) y a su vez mayor que el valor de C ({})".format(a,b,c))
elif (b>a and b>c):
    print("\n1. El valor de B ({}) es mayor que el valor de A ({}) y a su vez mayor que el valor de C ({})".format(b,a,c))
elif (c>a and c>b):
    print("\n1. El valor de C ({}) es mayor que el valor de A ({}) y a su vez mayor que el valor de B ({})".format(c,a,b))
else:
    print("\n1. El valor de A ({}) es igual que el valor de B ({}) y a su vez igual que el valor de C ({})".format(a,b,c))

# 3. Se hace una prueba con or

if (a>b or a>c):
    print("\n2. El valor de A ({}) es mayor que el valor de B ({}) ó que el valor de C ({})".format(a,b,c))
elif (b>a or b>c):
    print("\n2. El valor de B ({}) es mayor que el valor de A ({}) ó que el valor de C ({})".format(b,a,c))
elif (c>a or c>b):
    print("\n3. El valor de C ({}) es mayor que el valor de A ({}) ó que el valor de B ({})".format(c,a,b))
