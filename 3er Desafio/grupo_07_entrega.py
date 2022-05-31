import random


CANTIDADFIGURITAS = 5
VALORPAQUETE = 65

def aperturaFiguritas():
    vec = []
    for i in range(CANTIDADFIGURITAS):
        vec.append(random.randint(1, 860))
    return vec
    
            
def comprobarNumero(vec, aux):
    comprobacion = True
    for i in range(len(vec)):
        if vec[i] == aux:
            comprobacion = False
    return comprobacion

# Programa principal

print("************************************")
print("*** LLENADO DE ALBUM DEL MUNDIAL ***")
print("************************************")
print()
print(" - Comienza la apertura de paquetes - ")
print()
totalAlbum = []
totalPaquetes = 0
precioTotal = 0
while len(totalAlbum) < 860:
    paquete = aperturaFiguritas()
    totalPaquetes += 1
    for i in range(len(paquete)):
        aux = paquete[i]
        comprobacion = comprobarNumero(totalAlbum, aux)
        if comprobacion:
            totalAlbum.append(aux)
carga = "---------------"
for i in range(len(carga)):
    lista = list(carga)
    lista[i] = "#"
    carga = "".join(lista)
    print("Cargando: [", carga,"]")

            
precioTotal = totalPaquetes * VALORPAQUETE
figuritasTotal = totalPaquetes * 5

print()
print(" > Total de paquetes abiertos:", totalPaquetes)
print()
print(" > Total gastado en paquetes: $", precioTotal)
print()
print(" > Total de figuritas que tengo:", figuritasTotal)
print()
print(" > La figurita más dificil de encontrar fue:", totalAlbum[859])
print()