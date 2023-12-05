import random
import time
import libreria
from libreria import cartas

#Programa



####PRUEBA REPARTIR####
vec_cartasJugador,vec_cartasBot=libreria.repartir(cartas) #SE USA libreria.*nombre_funcion* para invocar la funcion deseada
print(f'valores de la maquina: {vec_cartasBot}')
time.sleep(1)
#################TESTEO DE FUNCION "ELEGIR_CARTA"###############
#USO: variable_carta_elegida=libreria.elegir_carta(vec_cartasJugador/Bot)

###TESTEO PARA VER SI FUNCIONA LO DE VALORES#####

print(libreria.cartas_mostrar(vec_cartasJugador))
for x in range(0,3):
    print(libreria.elegir_carta(vec_cartasJugador))
    print(vec_cartasJugador)
    print(f"Carta elegida por la maquina: {libreria.elegir_cartaBot(vec_cartasBot)}")
