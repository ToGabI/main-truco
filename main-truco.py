import random
import time
import libreria
from libreria import cartas

#Programa



####PRUEBA REPARTIR####
aux_cartasJugador,aux_cartasBot=libreria.repartir(cartas) #SE USA libreria.*nombre_funcion* para invocar la funcion deseada
cartasJugador=libreria.cartas_mostrar(aux_cartasJugador)
cartasBot=libreria.cartas_mostrar(aux_cartasBot)

print(f'valores de la maquina: {cartasBot}')
time.sleep(1)
#################TESTEO DE FUNCION "ELEGIR_CARTA"###############
#USO: variable_carta_elegida=libreria.elegir_carta(vec_cartasJugador/Bot)

###TESTEO PARA VER SI FUNCIONA LO DE VALORES#####
print(f'Su mano es: {cartasJugador}')
ganador=0
while ganador!=1:
    Jugador=libreria.elegir_carta(cartasJugador)
    valor_Jugador=libreria.valor_carta_jugador(Jugador)
    print(f'La carta que elegiste es: {Jugador}, y su valor es {valor_Jugador}')
    print(f'Tu mano es: {cartasJugador}')

    
    Bot=libreria.elegir_cartaBot(cartasBot)
    valor_Bot=libreria.valor_carta_bot(Bot)
    print(f'La carta elegida por la máquina es: {Bot}, y su valor es {valor_Bot}')

    time.sleep(0.5)
    while valor_Jugador == valor_Bot:
        print('Parda la mejor')
        Jugador=libreria.elegir_carta(cartasJugador)
        valor_Jugador=libreria.valor_carta_jugador(Jugador)
        print(f'La carta que elegiste es: {Jugador}, y su valor es {valor_Jugador}')
        print(f'Tu mano es: {cartasJugador}')

        valor_Bot=libreria.valor_carta_bot(Bot)
        Bot=libreria.elegir_cartaBot(cartasBot)
        print(f'La carta elegida por la máquina es: {Bot}, y su valor es {valor_Bot}')

        if valor_Jugador > valor_Bot:
            print('Ganaste la partida')
            ganador=1
        elif valor_Jugador < valor_Bot:
            print('Perdiste la partida')
            ganador=1


    while valor_Jugador > valor_Bot:
        print('Ganaste la mano')
        Jugador=libreria.elegir_carta(cartasJugador)
        valor_Jugador=libreria.valor_carta_jugador(Jugador)
        print(f'La carta que elegiste es: {Jugador}, y su valor es {valor_Jugador}')
        print(f'Tu mano es: {cartasJugador}')

        valor_Bot=libreria.valor_carta_bot(Bot)
        Bot=libreria.elegir_cartaBot(cartasBot)
        print(f'La carta elegida por la máquina es: {Bot}, y su valor es {valor_Bot}')
    while valor_Jugador < valor_Bot:
        print('Perdiste la mano')
        valor_Bot=libreria.valor_carta_bot(Bot)
        Bot=libreria.elegir_cartaBot(cartasBot)
        print(f'La carta elegida por la máquina es: {Bot}, y su valor es {valor_Bot}')

        Jugador=libreria.elegir_carta(cartasJugador)
        valor_Jugador=libreria.valor_carta_jugador(Jugador)
        print(f'La carta que elegiste es: {Jugador}, y su valor es {valor_Jugador}')
        print(f'Tu mano es: {cartasJugador}')

    
