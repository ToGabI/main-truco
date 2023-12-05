import random

#########################################################
######################CLASES#############################
#########################################################
class copas_1:
    nombre="1 de copa"
    palo="copas"
    valor=8
    valor_envido=1
class copas_2:
    nombre="2 de copas"
    palo="copas"
    valor=9
    valor_envido=2
class copas_3:
    nombre="3 de copas"
    palo="copas"
    valor=10
    valor_envido=3
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
class oro_1:
    nombre="1 de oro"
    palo="oro"
    valor=8
    valor_envido=1
class oro_2:
    nombre="2 de oro"
    palo="oro"
    valor=9
    valor_envido=2
class oro_3:
    nombre="3 de oro"
    palo="oro"
    valor=10
    valor_envido=3
class oro_4:
    nombre="4 de oro"
    palo="oro"
    valor=1
    valor_envido=4
class oro_5:
    nombre="5 de oro"
    palo="oro"
    valor=2
    valor_envido=5
class oro_6:
    nombre="6 de oro"
    palo="oro"
    valor=3
    valor_envido=6
class oro_7:
    nombre="7 de oro"
    palo="oro"
    valor=11
    valor_envido=7
class oro_10:
    nombre="10 de oro"
    palo="oro"
    valor=5
    valor_envido=0
class oro_11:
    nombre="11 de oro"
    palo="oro"
    valor=6
    valor_envido=0
class oro_12:
    nombre="12 de oro"
    palo="oro"
    valor=7
    valor_envido=0
class espada_1:
    nombre="1 de espada"
    palo="espada"
    valor=14
    valor_envido=1
class espada_2:
    nombre="2 de espada"
    palo="espada"
    valor=9
    valor_envido=2
class espada_3:
    nombre="3 de espada"
    palo="espada"
    valor=10
    valor_envido=3
class espada_4:
    nombre="4 de espada"
    palo="espada"
    valor=1
    valor_envido=4
class espada_5:
    nombre="5 de espada"
    palo="espada"
    valor=2
    valor_envido=5
class espada_6:
    nombre="6 de espada"
    palo="espada"
    valor=3
    valor_envido=6
class espada_7:
    nombre="7 de espada"
    palo="espada"
    valor=13
    valor_envido=7
class espada_10:
    nombre="10 de espada"
    palo="espada"
    valor=5
    valor_envido=0
class espada_11:
    nombre="11 de espada"
    palo="espada"
    valor=6
    valor_envido=0
class espada_12:
    nombre="12 de espada"
    palo="espada"
    valor=7
    valor_envido=0
class basto_1:
    nombre="1 de basto"
    palo="basto"
    valor=13
    valor_envido=1
class basto_2:
    nombre="2 de basto"
    palo="basto"
    valor=9
    valor_envido=2
class basto_3:
    nombre="3 de basto"
    palo="basto"
    valor=10
    valor_envido=3
class basto_4:
    nombre="4 de basto"
    palo="basto"
    valor=1
    valor_envido=4
class basto_5:
    nombre="5 de basto"
    palo="basto"
    valor=2
    valor_envido=5
class basto_6:
    nombre="6 de basto"
    palo="basto"
    valor=3
    valor_envido=6
class basto_7:
    nombre="7 de basto"
    palo="basto"
    valor=12
    valor_envido=7
class basto_10:
    nombre="10 de basto"
    palo="basto"
    valor=5
    valor_envido=0
class basto_11:
    nombre="11 de basto"
    palo="basto"
    valor=6
    valor_envido=0
class basto_12:
    nombre="12 de basto"
    palo="basto"
    valor=7
    valor_envido=0


#########################################################
#######################CARTAS############################
#########################################################

cartas=[copas_1,
        copas_2,
        copas_3,
        copas_4,
        copas_5,
        copas_6,
        copas_7,
        copas_10,
        copas_11,
        copas_12,
        oro_1,
        oro_2,
        oro_3,
        oro_4,
        oro_5,
        oro_6,
        oro_7,
        oro_10,
        oro_11,
        oro_12,
        espada_1,
        espada_2,
        espada_3,
        espada_4,
        espada_5,
        espada_6,
        espada_7,
        espada_10,
        espada_11,
        espada_12,
        basto_1,
        basto_2,
        basto_3,
        basto_4,
        basto_5,
        basto_6,
        basto_7,
        basto_10,
        basto_11,
        basto_12
        ]

#########################################################
#################FUNCION PARA REPARTIR###################
#########################################################
def repartir(cartas):
    jugador=[]
    bot=[]
    general=[]


    #Jugador
    for x in range(0,3):
        palabra_random=(random.choice(cartas)) #Pickea una palabra random de cartas
        for e in range(0,len(jugador)): #Ciclo que servira para recorrer cada elemento del array cartas
            while jugador.__contains__(palabra_random) == True: #Si el array contiene la palabra pickeada, genera otra
                palabra_random=(random.choice(cartas))
        jugador.append(palabra_random)


    #Maquina
    for x in range(0,3):
        palabra_random=(random.choice(cartas)) #Pickea una palabra random de cartas
        for e in range(0,len(bot)): #Ciclo que servira para recorrer cada elemento del array cartas
            while bot.__contains__(palabra_random) == True or jugador.__contains__(palabra_random) == True: #Si el array contiene la palabra pickeada o si el jugador la tiene, genera otra
                palabra_random=(random.choice(cartas))
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
    aux=True

    while aux:
        if par_manoJugador.__contains__(var_cartaElegida):
            par_manoJugador.remove(var_cartaElegida)
            aux=False
    return var_cartaElegida    #Se da como retorno la carta usada pero de todas formas el vector de la mano es modificado.
#########################################################
##############FUNCION PARA ELEGIR CARTA BOT##############
#########################################################

def elegir_cartaBot(par_manoBot):
    carta_bot=random.choice(par_manoBot)
    aux=True
    while aux:
        if par_manoBot.__contains__(carta_bot):
            par_manoBot.remove(carta_bot)
            aux=False
    return carta_bot
   

#########################################################
##############FUNCION OBTENER VALORES CARTAS#############
#########################################################
def valores_de_mano(par_manoJugador):
    vec_valores=[]
    for x in range(len(par_manoJugador)):
        e=0
        aux=1
        while e<len(cartas) and aux!=0: #Lo que hace este while es hacer un barrido sobre la lista "cartas" y verificar que las cartas de la mano del jugador no se hayan usado, si se usaron, a vec_valores le agrega un -1, y si no se usaron, devuelve el valor de la carta usando cartas[posicion].valor
            if par_manoJugador[x] != cartas[e].nombre:
                aux=1
            else:
                posicion=e
                aux=0
            e=e+1
        if aux == 1:
            vec_valores.append(-1)
        else:
            vec_valores.append(cartas[posicion].valor)
    return vec_valores


def valor_carta(par_manoJugador):
    
    return
#########################################################
####################FUNCION ENVIDO#######################
#########################################################

#########################################################
####################FUNCION COMPARAR#####################
#########################################################

#########################################################
####################FUNCION MOSTRAR######################
#########################################################
def cartas_mostrar(par_manoJugador):
    vaux=[]
    for x in range(len(par_manoJugador)):
        vaux.append(par_manoJugador[x].nombre)
    return vaux