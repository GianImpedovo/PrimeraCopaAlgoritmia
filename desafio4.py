# Desafio 4

import random


POSICIONES = 6


# Armar posiciones random 
def armarCamino():
    camino = []
    for i in range(POSICIONES):
        camino.append(random.randint(0,1))
    return camino


def armarPersonaje():
    nombre = input("Ingrese el nombre del jugador: ")
    numero = int(input("Ingrese el número del jugador: "))
    print()
    print(" - El jugador que elegiste es:", nombre, "y tiene la camiseta:", numero)
    return nombre, numero
    
def juego(camino, personaje, frases):
    largo = len(camino)
    i = 0
    perdio = False
    
    while i < largo and perdio == False:
        fraseRandom = random.randint(0,5)
        print(" -- ", personaje[0], frases[fraseRandom], " -- ")
        decision = int(input("Seleccione 0 para la izquierda y 1 para la derecha: "))
        while decision != 0 and decision != 1:
            print ("Ingrese una opción válida")
            decision = int(input("Seleccione 0 para la izquierda y 1 para la derecha: "))
        print()

        if decision == camino[i] and perdio == False:
            print(personaje[0], "pasa al jugador brasileño.")
            print()
        else:
            print(personaje[0], "pierde la pelota con el brasileño y la Argentina se despide de ganar el mundial")
            print()
            perdio = True
        i += 1
    return perdio


# Programa principal

print("*********************************************")
print("*** ¡Bienvenido al juego de las gambetas! ***")
print("*********************************************")
print()
print()

camino = armarCamino()

print(" => ¡Armemos tu jugador! <= ")
print()
personaje = armarPersonaje()


print()
print()
print(" => ¡Arranca el juego! <= ")
print()
print ('" - Aquí Mariano Closs para ustedes relatándoles la final de la copa del mundo, BRASIL VS ARGENTINA. Nos encontramos en el minuto 90 del partido y', personaje [0], 'recibe la pelota y está decidido a encarar al RIVAL para definir el partido. - "')
print()

print(camino)

frases = ['se enfrenta a marquinhos que quiere frenar el ataque del argentino. A donde ira?', 'avanza con la pelota y se cruza con Romaldinho que quiere dejar a la Argentina sin posibilidades de ataque', 'sigue avanzado y se cruza con su compañero de club Fernandinho, el cual no esta dispuesto a dejar que el ataque de argentina avance', 'va con la pelota pegada al pie y decide encarar al proximo brasileño de turno', 'encara y se enfrenta cara a cara con Adriano para poder acercarse al arco de los de amarillo', 'se encuentra con Rafinha que hara lo necesario para evitar que continue el ataque']
resultado = juego(camino, personaje, frases)

if resultado == False:
    print(" => ", personaje[0], "PASA AL ULTIMO DEFENSOR BRASILEÑO Y SE PONE DE FRENTE AL ARCO, SE PREPARA PARA DISPARAR Y GOOOOOOOOOOOOOOL! ARGENTINO ARGENTINO GOL DE", personaje[0], "PARA DARLE LA VICTORIA Y GANAR EL MUNDIAL <= ")
    print()
else:
    print(" => SE TERMINA EL PARTIDO Y ARGENTINA NO PUEDE CONSEGUIR LA VICTORIA ANTE BRASIL <=")
    print()
    
reinicio = int(input("¿Deseas volver a jugar? 0 para si - 1 para no: "))
while reinicio != 0 and reinicio != 1:
        print ("Ingrese una opción válida")
        reinicio = int(input("¿Deseas volver a jugar? 0 para si - 1 para no: "))
        
while (reinicio == 0):
    resultado = juego(camino, personaje, frases)
    if resultado == False:
        print(" => ", personaje[0], "PASA AL ULTIMO DEFENSOR BRASILEÑO Y SE PONE DE FRENTE AL ARCO, SE PREPARA PARA DISPARAR Y GOOOOOOOOOOOOOOL! ARGENTINO ARGENTINO GOL DE", personaje[0], "PARA DARLE LA VICTORIA Y GANAR EL MUNDIAL <= ")
        print()
    else:
        print(" => SE TERMINA EL PARTIDO Y ARGENTINA NO PUEDE CONSEGUIR LA VICTORIA ANTE BRASIL <=")
        print()
    camino = armarCamino()
    if resultado == False:
        personaje = armarPersonaje()
    
    print()
    reinicio = int(input("¿Deseas volver a jugar? 0 para si - 1 para no: "))
    print()
    while reinicio != 0 and reinicio != 1:
        print ("Ingrese una opción válida")
        print()
        reinicio = int(input("¿Deseas volver a jugar? 0 para si - 1 para no: "))
        print()

print(" ************************** ")
print(" *** Gracias por jugar *** ")
print(" ************************** ")
    
    