import random
import libreria

def function(pa):
    jugador=[]
    bot=[]
    general=[]


    #Jugador
    for x in range(0,3):
        palabra_random=random.choice(cartas) #Pickea una palabra random de cartas
        for e in range(0,len(jugador)): #Ciclo que servira para recorrer cada elemento del array cartas
            while jugador.__contains__(palabra_random) == True: #Si el array contiene la palabra pickeada, genera otra
                palabra_random=random.choice(cartas)
        jugador.append(palabra_random)


    #Maquina
    for x in range(0,3):
        palabra_random=random.choice(cartas) #Pickea una palabra random de cartas
        for e in range(0,len(bot)): #Ciclo que servira para recorrer cada elemento del array cartas
            while bot.__contains__(palabra_random) == True or jugador.__contains__(palabra_random) == True: #Si el array contiene la palabra pickeada o si el jugador la tiene, genera otra
                palabra_random=random.choice(cartas)
        bot.append(palabra_random)    
    
    general.append(bot)
    general.append(jugador)
    return general



#Programa

cartas=[
    '4 de copas','4 de espada','4 de basto','4 de oro',
    '5 de copas','5 de espada','5 de basto','5 de oro',
    '6 de copas','6 de espada','6 de basto','6 de oro',
    '7 de copas','7 de basto',
    '10 de copas','10 de espada','10 de basto','10 de oro',
    '11 de copas','11 de espada','11 de basto','11 de oro',
    '12 de copas','12 de espada','12 de basto','12 de oro'
    ,'1 de copa','1 de oro',
    '2 de copa','2 de espada','2 de basto','2 de oro',
    '3 de copa','3 de espada','3 de basto','3 de oro',
    '7 de oro','7 de espada',
    '1 de basto',
    '1 de espada']
#Valores de cada carta (Vector ordenado en base al anterior)
valores_cartas=[
    1,1,1,1,
    2,2,2,2,
    3,3,3,3,
    4,4,
    5,5,5,5,
    6,6,6,6,
    7,7,7,7,
    8,8,
    9,9,9,9,
    10,10,10,10,
    11,12,
    13,
    14
]


print(function(cartas))
######TEMPORAL########
#Imprimir cada carta con su respectivo valor#
for i in range (0,40):
    print(cartas[i],":",valores_cartas[i])
########EJEMPLO PARA USAR FUNCIONES##########
#libreria.prueba()