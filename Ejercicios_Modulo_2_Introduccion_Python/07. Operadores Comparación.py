# 1. Se solicita por teclado el valor A y B

print("\nIngresa el valor de A: ")
a = input()
a = int(a)

print("Ingresa el valor de B: ")
b = input()
b = int(b)

# 2. Se imprime True o False dependiendo si los valores cumplen o no con la comparación correspondiente

print("\n A es igual que B: " +str(a==b))
print("\n A es diferente que B: " +str(a!=b))
print("\n A es mayor que B: " +str(a>b))
print("\n A es menor que B: " +str(a<b))
print("\n A es mayor o igual que B: " +str(a>=b))
print("\n A es menor o igual que B: " +str(a<=b))