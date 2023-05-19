# 1. Creamos las variables de tipo int y str

a = 20
b = 10
nombre = "Alex Fabián"

# 2. Imprimimos las variables antes
print("\nLos tipos de las variables creadas son (antes): ")
print("a = "+str(type(a)) + "\n" + "b = "+str(type(b)) + "\n" + "Nombre = "+str(type(nombre)))

# 3. Hacemos el cambio a String a las variables a y b

print("\nSe hace el cambio a String y Float las variables a y b\n")

a = str(a)
b = str(b)
sumastrings = a+b

# 4. Imprimimos las variables después
print("Los tipos de las variables creadas son (después): ")
print("a = "+str(type(a)) + "\n" + "b = "+str(type(b)) + "\n" + "Nombre = "+str(type(nombre)))

# 5. Validamos que es posible hacer la suma de a y b en formato String sin necesidad de hacer la conversión

print("\nLa suma de a y b en formato String es: "+sumastrings + " lo que vendria siendo equivalente a una concatenación entre a (20) "
                                                                "y c (10)")