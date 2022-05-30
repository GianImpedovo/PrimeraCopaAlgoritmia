# FUNCIONES 

# Función que imprime la lista de canciones desconocidas
def mostrarDesconocidas(listaDesconocidas):
    print()
    print(" --- CANCIONES DESCONOCIDAS --- ")
    for nombre in listaDesconocidas:
        print(f" -> {nombre}")

# Función que imprime el ranking de las siete canciones más escuchadas
def mostrarSiete(listaCanciones):
    print()
    print(" --- RANKING DE LAS 7 CANCIONES MAS ESCUCHADAS --- ")
    print()
    for i in range(7):
        nombre = listaCanciones[i][0]
        puntos = listaCanciones[i][3]
        print(f" -> Ranking {i + 1} : {nombre} -- Puntaje : {puntos}")

# Función que saca el promedio de puntos que tuvo cada canción
def sacarPromedioCanciones(listaCanciones, cantEncuestados):
    for cancion in listaCanciones:
        
        puntos = cancion[3]
        promedio = puntos / cantEncuestados
        cancion[3] = promedio

# Función que determina que canciones no fueron nunca escuchadas
def cancionesDesconocidas(listaCanciones):
    noEscuchadas = list()
    for cancion in listaCanciones:

        puntos = cancion[3]
        nombreCancion = cancion[0]
        
        if puntos == 0:
            noEscuchadas.append(nombreCancion)
    
    return noEscuchadas

# Función que verifica que el puntaje que se ingresa sea entre 1 y 10
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

# Función que realiza la encuesta
def realizarEncuesta(listaCanciones):
    print()
    print(" --- REALIZAMOS LA ENCUESTA --- ")
    print()
    for cancion in listaCanciones:
        
        print(" -> La cancion es : ", cancion[0])
        escucho = input(" Escuchaste esta cancion ? ( si = S / no = N ) ")
        
        # Solo si escuchó la canción puede votar su puntuación
        if escucho == "S":
            puntos = verificacionPuntos()
            cancion[3] += puntos
        
        print()

# Función en la que se ingresan los datos de las canciones
def cargarCanciones():
    print()
    print(" --- INGRESAR LOS DATOS DE LAS CANCIONES --- ")
    print()
    listaCanciones = [["El mundo unido por un balón", 1986, "Juan Carlos Abara"],["Un'estate italiana", 1990, "Gianna Nannini"],["Gloryland", 1994, "Daryl Hall"],["La copa de la vida", 1998, "Ricky Martin"],["Boom!", 2002, "Anastacia"],["The time of our lives", 2006, "Il Divo"],["Waka Waka", 2010, "Shakira"],["We are one", 2014, "Pitbull"], ["Live it up", 2018, "Nicky Jam"],["Hayya hayya", 2022, "Trinidad Cardona"]]
    listaCanciones = list()
    for i in range(10):
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

# Solo se va a ejecutar la función realizarEncuesta si se ingresó un si
while encuesta != "N":
    realizarEncuesta(listaCanciones)
    cantEncuestados += 1
    print()
    encuesta = input(" > Desea realizar encuesta : ( si = S / no = N ) ")


if cantEncuestados != 0:
    sacarPromedioCanciones(listaCanciones, cantEncuestados)
    listaDesconocidas = cancionesDesconocidas(listaCanciones)
    listaCanciones = sorted(listaCanciones, key= lambda x: x[3], reverse=True)
    mostrarSiete(listaCanciones)
    mostrarDesconocidas(listaDesconocidas)
else:
    print()
    print()
    print(" *** No se ha realizado ninguna encuesta *** ")



