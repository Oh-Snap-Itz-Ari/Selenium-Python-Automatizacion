# 1. Se define la variable suma
def suma (*args):
    resultado = 0 # 2. Se pone como en cero la variable resultado para que ya se comience a sumar bien
    for n in args:
        resultado = resultado + n
    print("\nEl resultado de la suma entre las variables digitadas en la función es igual a: "+str(resultado))

suma(5)
suma(5,1)
suma(2,4,6)
suma(1,3,5,7)
