
#introducion
    #importamos  los modulos random y el del tiempo
        #memnsaje de inicio del juego.
        #introducir el nombre del jugador
        #imprimir el nombre del jugador
        #usar la biblioteca para que dejar unos segundos de sleep antes comenzar el juego
        #avisar del comienzo del juego, sleep otros segundos

import random
import time



print("Bienvenido al juego de las adivinanzas")

name = input('Introduce tu nombre :')
print ("Hola " + name + ' \nSuerte para ti')

time.sleep(3)

print("El juego comenzara en poco!")
time.sleep(3)

#programar 
    #el juego 
        #definimos las funciones y variables inportantes
            #definimos la funcion principal
            #las variables globales que vamos a utilizar durante la funcion
            #contar, mostrar, palabras, listo,tamano, jugar
            #definimos la variable de las palabras del juego en una lista
            #empezamos a utilizar las variables globales 
            #palabra que elija cualquier palabra de la lista de palabras del juego
            #contar que empiece a contar desde cero
            #tamano que cuente la cantidad de letras
            #mostrar que muestre la cantidad de letras multiplicado por la cantidad espacios
            #palabras adivinadas que esten en una lista vacia
            #jugar que este vacio tambien





def Principal():
    global contar 
    global mostrar
    global palabras
    global palabras_adivinadas
    global tamano
    global jugar

    palabras_juego = ["casa", "avion", ]

    palabras = random.choice(palabras_juego)
    contar = 0
    tamano = len(palabras)
    mostrar ="_" * tamano
    palabras_adivinadas = []
    jugar = ""




    #blucle que se ejecutara
        #el bucle sera ejecutado siempre para repetir el codigo del juego
            #creamos la funcions principal del bucle
            #creamos las variable globale : juego
            #el input encaso de que quiereas jugar mas

            #el bucle de la partida

                #condicion de si jugar partida es igual a SI que hacer: ejecutar funcion principal 
                #condicion de si jugar partida es igual a NO que hacer: ejecutar funcion imprimir fin y salir 

def bucle_jugar():
    global juego
    jugar_partida = input("Quieres juagar otra vez ? , Pulsa \ny=Si, \ny=No")

    while jugar_partida not in ["y","n", "Y","N"]:
        jugar_partida = input("Quieres juagar otra vez ? , Pulsa \ny=Si, \ny=No")
    
    if jugar_partida == "y":
        Principal()
    elif jugar_partida == "n":
        print("fin del juego")
        exit()

#condiciones que se iniciaran al comenzar el juego:
    #definimos la funcion del juego
        #traer alguns de las variables globales de la  funcion principal.
        #contar, mostrar, palabras, palabras_adivinadaas jugar
        #poner un limite de intentos
        #crear la variable  para que se introduzca la palabra que se va a adivinar y se mostrara

        #usar strip() para eliminar cualquier espacio en blanco en  la palabra de la  variable que se va adivinar

        #creammos el bucle  que controla  la cantidad de de espacios en blanco y 
            # if len(adivinar.strip()) ==0 or len(adivinar.strip()) >=2 or adivinar <= "9":
                #sin olvidad de llamar a la funcion del juego
            
            




def adivinazas ():
    global contar 
    global mostrar
    global palabras
    global palabras_adivinadas
    global jugar

    limite = 5
    adivinar = input("Estos son espacios de las palabras : " + mostrar + " Introduce la palabra : \n ")
    adivinar = adivinar.strip()

    if len(adivinar.strip()) == 0 or len(adivinar.strip()) >=2 or adivinar <= "9":
        print("nombre, numero  o metodo de entrada invalido , \nIntentalo de nuevo")
        adivinazas()

#la base del juego
    #adivinar la palabras

        #hacer la extensiond||agregar elementos de una lista en otra)||  de adivinar el las palabras
        #crear el bucle del inicio para encontrar palabras en la funcion
        #hacer que las palabras cogan palabrasy espacios dela funcion de adivinar
        #mostrar

        #entonces si adivinar esta  en palabras ya adivinadas decir al programa que intente otra palabra

        #en caso que este todo bien pues dale las congratulaciones.

        #entonces contar tiene que ser diferente de limite


    elif adivinar in palabras:
        palabras_adivinadas.extend([adivinar])
        inicio = palabras.find(adivinar)
        palabras =palabras[:inicio] + "_" + palabras[inicio + 1:]
        mostrar = mostrar[:inicio] + adivinar + mostrar[inicio + 1:]
        print(mostrar + "\n")

    elif adivinar in palabras_adivinadas:
        print("intenta otra palabtra. \n")



    else:
        contar += 1
        if contar == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limite - contar) + " guesses remaining\n")
        elif contar == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limite - contar) + " guesses remaining\n")
        elif contar == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limite - contar) + " guesses remaining\n")
        elif contar == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limite - contar) + " last guess remaining\n")
        elif contar == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",palabras_adivinadas,palabras)
            bucle_jugar()




    if palabras == "_" * tamano:
       print("lo has conseguido!, \n Enhorabuena")

       bucle_jugar()
    elif contar != limite:
        adivinazas()

Principal()

adivinazas()

    





