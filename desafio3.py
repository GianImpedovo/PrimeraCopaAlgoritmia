import random


CANTIDADFIGURITAS = 5

def aperturaFiguritas():
    print("Apertura de paquete:")
    vec = []
    for i in range(CANTIDADFIGURITAS):
        vec.append(random.randint(1, 860))
    print(vec)
    return vec

def figuritasAlbum(totalFiguritas):
    largo = len(totalFiguritas)
    totalPaquetes = 0
    while largo < 860:
        paquete = aperturaFiguritas()
        totalPaquetes += 1
        for i in range(len(paquete)):
            comprobacion = comprobarNumero(totalFiguritas, paquete[i])
            if comprobacion == True:
                totalFiguritas.append(paquete[i])
            
def comprobarNumero(vec, aux):
    comprobacion = True
    for i in range(len(vec)):
        if vec[i] == aux:
            comprobacion = False
    return comprobacion

# Programa principal

totalFiguritas = []


figuritasAlbum(totalFiguritas)