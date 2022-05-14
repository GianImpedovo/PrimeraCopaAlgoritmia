# FUNCIONES 

def mostrarDesconocidas(listaDesconocidas):
    print()
    print(" --- CANCIONES DESCONOCIDAS --- ")
    for nombre in listaDesconocidas:
        print(f" -> {nombre}")

def mostrarSiete(listaCanciones):
    print()
    print(" --- RANKING DE LAS 7 CANCIONES MAS ESCUCHADAS --- ")
    print()
    for i in range(2):
        nombre = listaCanciones[i][0]
        print(f" -> Ranking {i + 1} : {nombre}")

def sacarPromedioCanciones(listaCanciones, cantEncuestados):
    for cancion in listaCanciones:
        
        puntos = cancion[3]
        promedio = puntos / cantEncuestados
        cancion[3] = promedio

def cancionesDesconocidas(listaCanciones):
    noEscuchadas = list()
    for cancion in listaCanciones:

        puntos = cancion[3]
        nombreCancion = cancion[0]
        
        if puntos == 0:
            noEscuchadas.append(nombreCancion)
    
    return noEscuchadas

def verificacionPuntos():
    print()
    print(" En una escala del 1 al 10 ")
    puntos = int(input(" > Cuanto puntaje le das ? "))
    
    while puntos > 10 or puntos < 1 :
        print()
        print(" ERROR AL INGRESAR NUMERO, ingrese el puntaje nuevamente")
        print(" En una escala del 1 al 10 ")
        puntos = int(input(" > Cuanto puntaje le das ? "))
    
    return puntos

def realizarEncuesta(listaCanciones):
    print()
    print(" --- REALIZAMOS LA ENCUESTA --- ")
    print()
    for cancion in listaCanciones:
        
        print(" -> La cancion es : ", cancion[0])
        escucho = input(" Escuchaste esta cancion ? ( si = S / no = N ) ")
        
        if escucho == "S":
            puntos = verificacionPuntos()
            cancion[3] += puntos
        
        print()

def cargarCanciones():
    print()
    print(" --- INGRESAR LOS DATOS DE LAS CANCIONES --- ")
    print()
    listaCanciones = list()
    for i in range(4):
        print()
        nombre = input(" > Ingrese el nombre de la cancion : ")
        mundial = int(input(" > Ingrese el año del mundial : "))
        interprete = input(" > Ingrese el interprete de la cancion : ")
        puntos = 0
        
        cancion = [nombre, mundial, interprete, puntos]
        listaCanciones.append(cancion)

    return listaCanciones

# Programa Principal 
print()
print(" ### ENCUESTA RANKING DEL MUNDIAL ### ")
print()
listaCanciones = cargarCanciones() # Lista que contiene las canciones y los items pedidos : 
                                   # [ [nombreCancion, mundial, interprete, sumaPuntos] , [ cancion2 ]]

cantEncuestados = 0
print()
encuesta = input(" > Desea realizar encuesta : ( si = S / no = N ) ")

while encuesta != "N":
    realizarEncuesta(listaCanciones)
    cantEncuestados += 1
    print()
    encuesta = input(" > Desea realizar encuesta : ( si = S / no = N ) ")

# listaCanciones = [["asdf", 1, "asdf", 4],["asdf", 1, "asdf", 6],["asdf", 1, "asdf", 2],["asdf", 1, "asdf", 3]]

if cantEncuestados != 0:
    sacarPromedioCanciones(listaCanciones, cantEncuestados)
    listaDesconocidas = cancionesDesconocidas(listaCanciones)
    listaCanciones = sorted(listaCanciones, key= lambda x: x[3], reverse=True)
    mostrarSiete(listaCanciones)
    mostrarDesconocidas(listaDesconocidas)



