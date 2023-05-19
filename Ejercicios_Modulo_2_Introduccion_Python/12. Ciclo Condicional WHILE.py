# 1. Se crean las variables de inicio y fin, las cuales van a ser de utilidad dentro del While
inicio = 0
fin = 10

inicio2 = 0
fin2 = 10

# 2. Se crea un While que permita imprimir los valores del 1 al 10
print("\nLos valores del 1 al 10 impresos a través de un While son los siguientes: ")
while (inicio < fin):
    inicio = inicio + 1
    print(str(inicio))

# 3. Se crea un While que permita imprimir los valores del 0 al 10 omitiendo el 5
print("\nLos valores del 1 al 10 impresos a través de un While y omitiendo el 5 son los siguientes: ")
while (inicio2 < fin2):
    inicio2 = inicio2 + 1
    if (inicio2 == 5):
        continue
    print(str(inicio2))