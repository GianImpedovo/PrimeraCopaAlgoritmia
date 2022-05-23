ARGENTINA = "Argentina"
MEXICO = "Mexico"
POLONIA = "Polonia"
ARABIA_SAUDITA = "Arabia Saudita"

# Funciones

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
    print( " Ingrese los jugadores o n para finalizar la carga ")
    nombreJugador = input(" Nombre jugador : ")

    while nombreJugador != "n":
        equipo[2].append(nombreJugador)
        nombreJugador = input(" Nombre jugador : ")

def cargamosDatosEquipo(equipo):
    nombre = input("Ingrese el nombre del pais : ")
    partido = int(input("Ingrese el partido que jugo ( 1 o 2 ) : "))
    
    equipo[0] = nombre
    equipo[1] = partido
    ingresarJugadores(equipo)

def computarPartido(equipo1, equipo2, equipo3, equipo4):
    
    cargamosDatosEquipo(equipo1)
    cargamosDatosEquipo(equipo2)
    cargamosDatosEquipo(equipo3)
    cargamosDatosEquipo(equipo4)
    
    determinamosPartidos(equipo1, equipo2, equipo3, equipo4)

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

def procesarFechas():
    equipo1 = ["", 0, []]
    equipo2 = ["", 0, []]
    equipo3 = ["", 0, []]
    equipo4 = ["", 0, []]

    for i in range(1):
        print(f"\n FECHA {i + 1} \n")
        computarPartido(equipo1, equipo2, equipo3, equipo4)
        computarGoleador(equipo1, equipo2, equipo3, equipo4)


# Programa Principal

listaPuntos = [ [ARGENTINA, 0] , [MEXICO, 0], [POLONIA, 0], [ARABIA_SAUDITA, 0]]
goleadores = []
procesarFechas()

print(goleadores)
print(listaPuntos)
