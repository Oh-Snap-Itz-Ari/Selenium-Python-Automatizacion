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

# 2. Se imprime una comparación con and (&&)

print("\n A es menor que B y a su vez menor que C: " +str(a<b and a<c))
print("\n A es igual que B y a su vez igual que C: " +str(a==b and a==c))

# 3. Se imprime una comparación con or (o)

print("\n A es menor que B o A es menor que C: " +str(a<b or a<c))
print("\n A es igual que B o A es igual que C: " +str(a==b or a==c))
