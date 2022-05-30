ARGENTINA = "Argentina"
MEXICO = "Mexico"
POLONIA = "Polonia"
ARABIA_SAUDITA = "Arabia Saudita"

# Funciones
def validarNombre():
    nombre = input("\n > Ingrese el nombre del pais : ")
    while nombre != ARGENTINA and nombre != MEXICO and nombre != POLONIA and nombre != ARABIA_SAUDITA:
        print("\n INGRESO MAL EL NOMBRE DEL EQUIPO ")
        print(" ---> nombres validos : Argentina, Mexico, Polonia y Arabia Saudita.")
        nombre = input("\n > Ingrese el nombre del pais : ")

    return nombre

def validarPartido():
    partido = int(input("\n > Ingrese el partido que jugo ( 1 o 2 ) : "))
    while partido != 1 and partido != 2:
        print("\n INGRESO MAL EL PARTIDO - PARTIDOS VALIDOS : 1 o 2")
        partido = int(input("\n > Ingrese el partido que jugo ( 1 o 2 ) : "))
    
    return partido

def ordenarLista(listaPuntos):
    lista = []
    lista.append(listaPuntos[0])
    puntaje = listaPuntos[0][1]
    
    for i in range(1, len(listaPuntos)):

        if listaPuntos[i][1] == puntaje:
            lista.append(listaPuntos[i])
            
    return lista

def mostrarRanking(listaGanador, tipoDeLista):
    print()
    if tipoDeLista == 0: 
        print("\n RANKING GANADOR ")
        if len(listaGanador) > 1:
            print("\n EQUIPO CON MAYOR PUNTAJE : \n")
        else : 
            print("\n EL GANADOR DEL GRUPO ES : \n")
    elif tipoDeLista == 1:
        print("\n RANKING PEOR RENDIMIENTO ")

    else: 
        print("\n RANKING GOLEADORES ")
    
    for equipo in listaGanador:
        print(f" -> {equipo[0]} - {equipo[1]} ")
    print()

def ordenarListaGoleadores(goleadores):
    goleadores = sorted(goleadores, key= lambda x: x[1], reverse=True)
    listaGoleadores = ordenarLista(goleadores)
    tipoDeLista = 2
    mostrarRanking(listaGoleadores, tipoDeLista)

def ordenarListaPeor(listaPuntos):
    listaPuntos = sorted(listaPuntos, key= lambda x: x[1])
    listaPeores = ordenarLista(listaPuntos)
    tipoDeLista = 1
    mostrarRanking(listaPeores, tipoDeLista)

def ordenarListaGanador(listaPuntos):
    listaPuntos = sorted(listaPuntos, key= lambda x: x[1], reverse=True)
    listaGanador = ordenarLista(listaPuntos)
    tipoDeLista = 0
    mostrarRanking(listaGanador, tipoDeLista)

def sumarPuntos(ganadorPartido):

    if len(ganadorPartido) > 1 :

        for equipo in listaPuntos:
            
            for ganador in ganadorPartido:
            
                if equipo[0] == ganador:
                    equipo[1] += 1

    else:
        for equipo in listaPuntos:
            if equipo[0] == ganadorPartido[0]:
                equipo[1] += 3

def determinarGanador(partido):
    ganador = []
    golesEquipo1 = len(partido[0][2])
    golesEquipo2 = len(partido[1][2])
    
    if golesEquipo1 > golesEquipo2:
        ganador.append(partido[0][0])
    elif golesEquipo1 < golesEquipo2:
        ganador.append(partido[1][0])
    else:
        ganador.append(partido[0][0])
        ganador.append(partido[1][0])

    return ganador

def determinamosPartidos(equipo1, equipo2, equipo3, equipo4):

    partido1 = []
    partido2 = []

    if equipo1[1] == equipo2[1]:
        partido1 = [equipo1, equipo2]
        partido2 = [equipo3, equipo4]
        
    elif equipo1[1] == equipo3[1]:
        partido1 = [equipo1, equipo3]
        partido2 = [equipo2, equipo4]
        
    else:
        partido1 = [equipo1, equipo4]
        partido2 = [equipo2, equipo3]
        
    ganadorPartido1 = determinarGanador(partido1)
    ganadorPartido2 = determinarGanador(partido2)
    
    sumarPuntos(ganadorPartido1)
    sumarPuntos(ganadorPartido2)

def ingresarJugadores(equipo):
    print("\t --------------------------------------------")
    print("\n\t### CARGA DE JUGADORES QUE REALIZARON GOLES ###")
    print( "\n Ingrese los jugadores o 'n' para finalizar la carga ")
    nombreJugador = input("\n > Nombre jugador : ")

    while nombreJugador != "n":
        equipo[2].append(nombreJugador)
        nombreJugador = input("\n > Nombre jugador : ")

def cargaDatosEquipo(equipo):
    print("\n\t### CARGAR PAIS ### ")
    
    equipo[0] = validarNombre()
    equipo[1] = validarPartido()
    ingresarJugadores(equipo)

def obtenerPosJugador(jugador, goleadores):
    posicion = -1 
    for i in range(len(goleadores)):
        if jugador == goleadores[i][0]:
            posicion = i

    return posicion

def computarGoleador(equipo1, equipo2, equipo3, equipo4):
    
    equipos = [equipo1, equipo2, equipo3, equipo4]
    
    for equipo in equipos:
        listaJugadores = equipo[2]

        for jugador in listaJugadores:
            posicion = obtenerPosJugador(jugador, goleadores)

            if posicion != -1:
                goleadores[posicion][1] += 1

            else:
                goleadores.append([jugador, 1])
    
    return goleadores

def computarPartido(equipo1, equipo2, equipo3, equipo4):
    
    cargaDatosEquipo(equipo1)
    cargaDatosEquipo(equipo2)
    cargaDatosEquipo(equipo3)
    cargaDatosEquipo(equipo4)
    
    determinamosPartidos(equipo1, equipo2, equipo3, equipo4)

def procesarFechas():
    equipo1 = ["", 0, []]
    equipo2 = ["", 0, []]
    equipo3 = ["", 0, []]
    equipo4 = ["", 0, []]

    for i in range(3):
        print()
        print(f"\n ### FECHA {i + 1} ###\n")
        computarPartido(equipo1, equipo2, equipo3, equipo4)
        computarGoleador(equipo1, equipo2, equipo3, equipo4)

# Programa Principal
print("\n\t --- RESULTADOS DEL GRUPO C ---")
listaPuntos = [ [ARGENTINA, 0], [MEXICO, 0],  [POLONIA, 0],  [ARABIA_SAUDITA, 0]]
goleadores = []
procesarFechas()
ordenarListaGanador(listaPuntos)
ordenarListaPeor(listaPuntos)
ordenarListaGoleadores(goleadores)
