# 1. Se crea un for que imprima los valores desde el cero (0) hasta el 10
print("\nLos números impresos a través del ciclo condicional son: ")
for x in range(11):
    print(str(x))

# 2. Se crea un for que imprima los valores completos de una lista (Array)
colores = ["Amarillo", "Azul", "Rojo", "Verde", "Morado", "Naranja"]

# 2.1. Se almacena en valor_color los colores y luego los imprime a través del for
print("\nLos colores que se guardaron dentro del array son: ")
for valor_color in colores:
    print(valor_color)

# 3. En caso tal de que tengamos una lista podemos imprimir cada uno de sus carácteres:

nombre  = "Alex Melo"

print("\nEl nombre escrito a en la lista e impreso por carácteres seria: ")
for carac_nombre in nombre:
    print(carac_nombre)

# 4. Se puede imprimir los valores de una variable añadiendo ciertos condicionales

print("\nLos números impresos del 10 al 20 son: ")
for x in range(10,21):
    print(str(x))

print("\nLos números del 0 al 50 con saltos de 5 en 5 serian los siguientes:")
for x in range(0,55,5):
    print(str(x))

print("\nLos números del 0 al 50 con saltos de 5 en 5 serian los siguientes:")
for x in range(0,55,5):
    print(str(x))

print("\nEs posible detener un ciclo añadiendo un break, en este caso detenemos la ejecución cuando sea <=30:")
for x in range(0,55,5):
    if(x >= 35):
        break
    print(str(x))

# 5. Podemos añadir condicionales especiales para que no se impriman ciertos valores dentro del for

print("\nLos números pares entre 1 y 10 son: ")
for x in range(1,11):
    if(x == 1 or x == 3 or x == 5 or x == 7 or x == 9):
        continue
    print(x)