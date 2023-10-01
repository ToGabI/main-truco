import random
from libreria import(cartas,valores_cartas) #importa las variables de libreria
import libreria


#Programa



#print(libreria.function(cartas))
######TEMPORAL########
#Imprimir cada carta con su respectivo valor#
for i in range (0,40):
    print(cartas[i],":",valores_cartas[i])
########EJEMPLO PARA USAR FUNCIONES##########
#libreria.prueba()

####PRUEBA REPARTIR
vec_cartasJugador,vec_cartasBot=libreria.repartir(cartas) #SE USA libreria.*nombre_funcion* para invocar la funcion deseada
#################TESTEO DE FUNCION "ELEGIR_CARTA"###############
#USO: variable_carta_elegida=libreria.elegir_carta(vec_cartasJugador/Bot)
print(vec_cartasJugador)
var_cartaElegida=libreria.elegir_carta(vec_cartasJugador)
while var_cartaElegida=="":  #SI LA FUNCION DETECTA QUE LA CARTA NO ESTA EN LA MANO O FUE MAL ESCRITA, LA VARIABLE QUEDA VACÍA PERO HAY QUE VOLVER A USAR LA FUNCION
    print("Su mano no há sido modificada:")
    var_cartaElegida=libreria.elegir_carta(vec_cartasJugador)
print(vec_cartasJugador)