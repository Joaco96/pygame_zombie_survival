from random import randint
import pygame
import sys
from collissions import *
import math

def sorted_map(comparador, lista:list) -> list:
  """Ordena una lista creando una nueva segun un comparador especificado.

  Args:
      comparador (_type_): Regla para comparar los elementos de la lista.
      lista (list): Lista a ordenar.

  Raises:
      TypeError: Error por falta de lista en el input.

  Returns:
      list: Devuelve una lista nueva ordenada segun el comparador.
  """
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  copia_lista = lista.copy()
  sort(comparador, copia_lista)
  return copia_lista

def sort(comparador, lista:list) -> None:
  """Ordena una lista modificando la misma.

  Args:
      comparador (_type_): Regla para comparar los elementos de la lista.
      lista (list): Lista a ordenar.

  Raises:
      TypeError: Error por falta de lista en el input.
  """
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
    """Calcula la distancia entre dos puntos.

    Args:
        pto_1 (tuple[int,int]): Tupla con dos coordenadas del primer punto.
        pto_2 (tuple[int,int]): Tupla con dos coordenadas del segundo punto.

    Returns:
        float: Devuelve la distancia entre estos dos puntos.
    """
    return ((pto_1[0] - pto_2[0])**2 + (pto_1[1] - pto_2[1])**2)**0.5 

def calcular_direccion(origen:tuple[int,int],target:tuple[int,int],speed:int = 1) -> tuple[int,int]:
    """Calculo la direccion entre dos puntos.

    Args:
        origen (tuple[int,int]): Punto origen para calcular la direccion.
        target (tuple[int,int]): Segundo punto para calcular la direccion.
        speed (int, optional): Acelerador en la direccion calculada. Defaults to 1.

    Returns:
        tuple[int,int]: Devuelve una tupla con la direccion resultante entre dos puntos.
    """
    dist_x =  target[0] - origen[0]
    dist_y = target[1] - origen[1] 
    dist = distancia_entre_puntos(target, origen)
    dist_x = dist_x / dist * speed
    dist_y = dist_y / dist * speed
    return(dist_x,dist_y)

def calcular_direccion_angulo(angulo:float) -> tuple[int,int]:
    """Calcula la direccion de un angulo determinado.

    Args:
        angulo (float): Angulo determinado para el calculo de la direccion.

    Returns:
        tuple[int,int]: Devuelve una tupla con la direccion en base al angulo determinado.
    """
    radianes = math.radians(angulo)
    return (math.cos(radianes), math.sin(radianes))

def generate_random_position(settings:dict) -> tuple[int,int]:
    """Determina una posicion random fuera de los limites de la pantalla

    Args:
        settings (dict): Diccionario con toda la informacion de configuracion del juego.

    Returns:
        tuple[int,int]: Retorna las coordenadas de la posicion random.
    """
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
    """Calcula el radio de una circunferencia.

    Args:
        rect (_type_): Rectangulo que contiene el circulo.

    Returns:
        float: Devuelve el radio de la circunferencia.
    """
    return rect.width // 2

def wait_user(tecla: int) -> None:
    """Paraliza el programa hasta que el usuario presione la tecla especificada.

    Args:
        tecla (int): Tecla especificada para desparalizar el programa.
    """
    flag_start = True
    pygame.mixer.music.pause()
    while flag_start:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == tecla:
            pygame.mixer.music.unpause()
            flag_start = False

def terminar():
    pygame.quit()
    exit()

def rotar_pos(bloque:dict,pos:tuple) -> pygame.Surface:
    """Calcula y rota una superficie de un elemento especificado en base a una posicion.

    Args:
        bloque (dict): Elemento origen para calcular la direccion de rotacion.
        pos (tuple): Posicion destino del calculo de la rotacion.

    Returns:
        pygame.Surface: Devuelve la superficie rotada en base al calculo realizado.
    """
    angulo = math.degrees(math.atan2(pos[1] - bloque["rect"][1], pos[0] - bloque["rect"][0]))
    imagen_rotada = pygame.transform.rotate(bloque["img"],-angulo)
    return imagen_rotada