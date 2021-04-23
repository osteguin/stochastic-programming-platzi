import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol'] #Con mayúsculas significa que es una constante
VALORES = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
            
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    
    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()
    
    manos = []
    
    for __ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
            
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 3:
                pares += 1
                break
        
        
    probabilidad_par = pares/intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} es {probabilidad_par}')

if __name__ ==  '__main__':
    tamano_de_mano = int(input('De cuantas barajas será la mano: '))
    intentos = int(input('Cuantos intentos de la simulacion: '))
    main(tamano_de_mano, intentos)
    
    #print(mano)
    #print(barajas)