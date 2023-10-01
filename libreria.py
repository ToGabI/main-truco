

import random
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
###################################################################################
#########################################################
##################FUNCION PARA COMPARAR##################
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
        if i==3:   #Cuando i=3 significa que la proxima vez va a romper el ciclo, es decir que si la carta elegida aún no coincide con alguna de la manose le comunica al jugador que la carta que eligió no forma parte de su mano/no fue bien escrita
            var_cartaElegida=""  #Al haber un problema por lo dicho en la linea anterior, la carta elegida se asigna como VACIA
            print("La carta elegida no es parte de su mano. Verifique que escribio bien su carta.")
    if var_cartaElegida!="":   #Si la variable de la carta elegida queda VACIA, no se entra en este IF, pero si se pudo asignar un valor, significa que todo salio bien, por lo que se verifica que carta del vector fue seleccionada y se reemplaza por "CARTA USADA"
        for x in range (0,3):
            if par_manoJugador[x]==var_cartaElegida:
                par_manoJugador[x]="*Carta Usada*"
    return var_cartaElegida    #Se da como retorno la carta usada pero de todas formas el vector de la mano es modificado.