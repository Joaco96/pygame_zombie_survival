from random import randint
import pygame
import sys
from collissions import *
import math

def sorted_map(comparador, lista:list) -> list:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  copia_lista = lista.copy()
  sort(comparador, copia_lista)
  return copia_lista

def sort(comparador, lista:list) -> None:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  tam = len(lista)
  for i in range(tam - 1):
    for j in range(i + 1, tam):
      if (comparador(lista[i], lista[j])):
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux

def distancia_entre_puntos(pto_1:tuple[int,int],pto_2:tuple[int,int]) -> float:
    return ((pto_1[0] - pto_2[0])**2 + (pto_1[1] - pto_2[1])**2)**0.5 

def calcular_direccion(origen:tuple[int,int],target:tuple[int,int],speed:int = 1) -> tuple[int,int]:
    dist_x =  target[0] - origen[0]
    dist_y = target[1] - origen[1] 
    dist = distancia_entre_puntos(target, origen)
    dist_x = dist_x / dist * speed
    dist_y = dist_y / dist * speed
    return(dist_x,dist_y)

def calcular_direccion_angulo(angulo):
    radianes = math.radians(angulo)
    print(radianes)
    return (math.cos(radianes), math.sin(radianes))

def generate_random_position(settings) -> tuple[int,int]:
    # elijo un borde al azar
    edge = randint(0, 3)
    if edge == 0:  # Izquierda
        x = randint(-(settings["ALFA"]), 0)
        y = randint(0, settings["HEIGHT"])
    elif edge == 1:  # Derecha
        x = randint(settings["WIDTH"], settings["WIDTH"] + settings["ALFA"])
        y = randint(0, settings["HEIGHT"])
    elif edge == 2:  # Arriba
        x = randint(0, settings["WIDTH"])
        y = randint(-(settings["ALFA"]), 0)
    else:  # Abajo
        x = randint(0, settings["WIDTH"])
        y = randint(settings["HEIGHT"], settings["HEIGHT"] + settings["ALFA"])
    return (x, y)

def calcular_radio(rect) -> float:
    return rect.width // 2

def wait_user(tecla: int) -> None:
  flag_start = True
  while flag_start:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == tecla:
          flag_start = False

def terminar():
    pygame.quit()
    exit()
