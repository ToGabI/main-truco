import random
import time
import libreria
from libreria import cartas

#Programa



####REPARTIR JUGADOR####
aux_cartasJugador=libreria.repartir_jugador(cartas)
cartasJugador=libreria.cartas_mostrar(aux_cartasJugador)
####REPARTIR BOT####
aux_cartasBot=libreria.repartir_bot(cartas,aux_cartasJugador)
cartasBot=libreria.cartas_mostrar(aux_cartasBot)


print(f'valores de la maquina: {cartasBot}')
time.sleep(1)
#################TESTEO DE FUNCION "ELEGIR_CARTA"###############
#USO: variable_carta_elegida=libreria.elegir_carta(vec_cartasJugador/Bot)

###TESTEO PARA VER SI FUNCIONA LO DE VALORES#####
print(f'Su mano es: {cartasJugador}')
ganador=0
while ganador!=1:
    jugador=libreria.elegir_carta(cartasJugador)
    valor_jugador=libreria.valor_carta_jugador(jugador)

    bot=libreria.elegir_cartaBot(cartasBot)
    valor_bot=libreria.valor_carta_bot(bot)
    print(f'La carta elegida por la máquina es: {bot}')
    if valor_jugador > valor_bot:
        print('GANASTE LA MANO')
        jugador=libreria.elegir_carta(cartasJugador)
        valor_jugador=libreria.valor_carta_jugador(jugador)
        bot=libreria.elegir_cartaBot(cartasBot)
        valor_bot=libreria.valor_carta_bot(bot)
        print(f'La carta elegida por la máquina es: {bot}')
        if valor_jugador > valor_bot or valor_jugador == valor_bot:
            print('GANASTE LA PARTIDA')
            ganador=1
        else:
            print('PERDISTE LA MANO')
            bot=libreria.elegir_cartaBot(cartasBot)
            valor_bot=libreria.valor_carta_bot(bot)
            print(f'La carta elegida por la máquina es: {bot}')
            jugador=libreria.elegir_carta(cartasJugador)
            valor_jugador=libreria.valor_carta_jugador(jugador)
            if valor_jugador > valor_bot or valor_jugador == valor_bot:
                print('GANASTE LA PARTIDA')
                ganador=1
            else:
                print('PERDISTE LA PARTIDA')
                ganador=1
    elif valor_jugador == valor_bot:
        print('PARDA LA MEJOR')
        bot=libreria.elegir_cartaBot(cartasBot)
        valor_bot=libreria.valor_carta_bot(bot)
        print(f'La carta elegida por la máquina es: {bot}')
        jugador=libreria.elegir_carta(cartasJugador)
        valor_jugador=libreria.valor_carta_jugador(jugador)
        if valor_jugador > valor_bot:
            print('GANASTE LA PARTIDA')
            ganador=1
        elif valor_jugador < valor_bot:
            print('PERDISTE LA PARTIDA')
            ganador=1
        elif valor_bot == valor_jugador:
            print('PARDA LA MEJOR')
            if valor_jugador > valor_bot:
                print('GANASTE LA PARTIDA')
                ganador=1
            elif valor_jugador < valor_bot:
                print('PERDISTE LA PARTIDA')
                ganador=1
            elif valor_jugador == valor_bot:
                print('EMPATE')
                ganador=1
    elif valor_bot > valor_jugador:
        print('PERDISTE LA MANO')
        bot=libreria.elegir_cartaBot(cartasBot)
        valor_bot=libreria.valor_carta_bot(bot)
        print(f'La carta elegida por la máquina es: {bot}')
        jugador=libreria.elegir_carta(cartasJugador)
        valor_jugador=libreria.valor_carta_jugador(jugador)
        if valor_bot > valor_jugador or valor_bot == valor_jugador:
            print('PERDISTE LA PARTIDA')
            ganador=1
        else:
            print('GANAS TE LA MANO')
            jugador=libreria.elegir_carta(cartasJugador)
            valor_jugador=libreria.valor_carta_jugador(jugador)
            bot=libreria.elegir_cartaBot(cartasBot)
            valor_bot=libreria.valor_carta_bot(bot)
            print(f'La carta elegida por la máquina es: {bot}')
            if valor_bot > valor_jugador or valor_bot == valor_jugador:
                print('PERDISTE LA PARTIDA')
                ganador=1
            else:
                print('GANASTE LA PARTIDA')
                ganador=1
                