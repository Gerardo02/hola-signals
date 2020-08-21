import math

print("Hola")

#convertidor a radianes

def convertidor(grados):
    radianes = (grados * math.pi)/180

    return radianes

print("El resultado en radianes es: " + str(convertidor(45)))
seno = math.sin(convertidor(60))
print("Y el seno es: " + str(seno))


#concatencion usando una funcion

def concatenar(str1, str2):
    return str1 + str2

print(concatenar("Hola me llamo ", "Gerardo"))

