import random

#########################################################
#########################################################
#########################################################
class copas_4:
    nombre="4 de copas"
    palo="copas"
    valor=1
    valor_envido=4
class copas_5:
    nombre="5 de copas"
    palo="copas"
    valor=2
    valor_envido=5
class copas_6:
    nombre="6 de copas"
    palo="copas"
    valor=3
    valor_envido=6
class copas_7:
    nombre="7 de copas"
    palo="copas"
    valor=4
    valor_envido=7
class copas_10:
    nombre="10 de copas"
    palo="copas"
    valor=5
    valor_envido=0
class copas_11:
    nombre="11 de copas"
    palo="copas"
    valor=6
    valor_envido=0
class copas_12:
    nombre="12 de copas"
    palo="copas"
    valor=7
    valor_envido=0


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

#Palos


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
    14]

#########################################################
#################FUNCION PARA REPARTIR###################
#########################################################
def repartir(cartas):
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
#########################################################
################FUNCION PARA ELEGIR CARTA################
#########################################################
def elegir_carta(par_manoJugador):
    print("Su mano actual es: ", par_manoJugador)
    var_cartaElegida=str(input("Por favor, seleccione una carta de su mano:"))
    var_cartaElegida=var_cartaElegida.lower()    #Se pone todo en minusculas por si el jugador escribio la carta en mayusculas o "variado"
    i=0    #Declaro contador (Supongo que se podria hacer con FOR pero en este caso se me hizo mas facil con while)
    while i<3:
        if var_cartaElegida==par_manoJugador[i]:   #Verifico que la carta elegida forme parte de la mano del jugador
            if var_cartaElegida!="*Carta Usada*":  #Descarto el error de que el jugador escriba "CARTA USADA"
                print("La carta escogida es: ", var_cartaElegida)   #Le aviso al jugador que todo salio bien y pongo el contador en 4 para salir del ciclo
                i=4
        else:
            i=i+1
        if i==3:   #Cuando i=3 significa que la proxima vez va a romper el ciclo, es decir que si la carta elegida aún no coincide con alguna de la mano se le comunica al jugador que la carta que eligió no forma parte de su mano/no fue bien escrita
            var_cartaElegida=""  #Al haber un problema por lo dicho en la linea anterior, la carta elegida se asigna como VACIA
            print("La carta elegida no es parte de su mano. Verifique que escribio bien su carta.")
    if var_cartaElegida!="":   #Si la variable de la carta elegida queda VACIA, no se entra en este IF, pero si se pudo asignar un valor, significa que todo salio bien, por lo que se verifica que carta del vector fue seleccionada y se reemplaza por "CARTA USADA"
        for x in range (0,3):
            if par_manoJugador[x]==var_cartaElegida:
                par_manoJugador[x]="*Carta Usada*"
    return var_cartaElegida    #Se da como retorno la carta usada pero de todas formas el vector de la mano es modificado.
#########################################################
##############FUNCION PARA ELEGIR CARTA BOT##############
#########################################################





#########################################################
##############FUNCION OBTENER VALORES CARTAS#############
#########################################################

def valores_de_mano(par_manoJugador):
    vec_valores=[]
    for x in range(0,3):
        if par_manoJugador[x] not in cartas:#IMPORTANTE, esto verifica si la carta "Fue usada", de esa manera, cada vez que aparezca un "*Carta usada*" en la mano del jugador, lo reemplaza por un valor negativo
            vec_valores.append(-1)
        else:
            valores=cartas.index(par_manoJugador[x])#Esto lo que hace es guardar las posiciones de la manoJugador del array 'Cartas', para despues buscar sus respectivos valores en el array 'Valores_cartas'. El 'index' cumple la misma funcion que el 'find' solo que en arrays
            vec_valores.append(valores_cartas[valores]) #Esto compara las posiciones de manoJugador con las de 'Valores_cartas' y los va poniendo en el array
    return vec_valores

#########################################################
##############FUNCION OBTENER EL PALO####################
#########################################################

