# 1. Se crea la lista "Lenguajes"

lenguajes = ["PHP", "JAVA", "PYTHON", "HTML", "CSS", "JAVASCRIPT"]

# 2. Se imprimen los lenguajes tal como se encuentra en la lista

print("\nLenguajes ingresados: \n" +str(lenguajes))

# 3. Se imprime el lenguaje #2, siendo en este caso PYTHON ya que se comienza a contar desde cero (0)

print("\nLenguaje #2: \n" +lenguajes[2])

# 4. Se añade un lenguaje más al final del listado y se imprime

lenguajes.append("DJANGO")
print("\nLenguajes ingresados (Se añade un lenguaje más al final del listado y se imprime): \n" +str(lenguajes))

# 5. Se cambia el lenguaje #3 por HTML5 y se imprime

lenguajes[3] = "HTML5"
print("\nLenguajes ingresados (Se cambia el lenguaje #3 por HTML5 y se imprime): \n" +str(lenguajes))

# 6. Se elimina el lenguaje DJANGO y se imprime

lenguajes.remove("DJANGO")
print("\nLenguajes ingresados (Se elimina el lenguaje DJANGO y se imprime): \n" +str(lenguajes))