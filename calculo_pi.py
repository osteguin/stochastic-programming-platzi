import random
import math
from estadistica import desviacion_estandar, media

def aventar_agujas(numero_de_agujas):
    dentro_del_circulo = 0
    
    
    for _ in range(numero_de_agujas):
        # Coordenada aleatoria de un plano de [-1, 1]
        x = random.random() * random.choice([-1 , 1])
        y = random.random() * random.choice([-1 , 1])
        
        # Teorema de Pitágoras
        
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)
        
        if distancia_desde_el_centro <= 1:
            dentro_del_circulo += 1
            
    return (4 * dentro_del_circulo) / numero_de_agujas

def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []
    
    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)
        
    sigma_estimados= desviacion_estandar(estimados)
    media_estimados = media(estimados)
    
    print(f'Est = {round(media_estimados, 5)} | Sigma={round(sigma_estimados, 5)} | Agujas = {numero_de_agujas}')
    
    return (media_estimados, sigma_estimados)

def estimar_pi(precision, numero_de_intentos):
    numero_de_agujas = 1000
    sigma = precision
    
    while sigma >= precision / 1.96:
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos)
        numero_de_agujas *= 2
        
    return media

if __name__ == '__main__':
    
    estimar_pi(0.01, 1000)