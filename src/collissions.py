import pygame
from utils import *

# colision de rectangulos
def detectar_colisiones(rect_1:pygame.Rect,rect_2:pygame.Rect) -> bool:
    """Detecta la colision de dos rectangulos.

    Args:
        rect_1 (pygame.Rect): Primer rectangulo para analizar.
        rect_2 (pygame.Rect): Segundo rectangulo para analizar.

    Returns:
        bool: Retorna si se tocan o no se tocan los dos rectangulos.
    """
    return (punto_en_rectangulo(rect_1.topright,rect_2) or punto_en_rectangulo(rect_1.topleft,rect_2) or punto_en_rectangulo(rect_1.bottomright,rect_2) or punto_en_rectangulo(rect_1.bottomleft,rect_2) or punto_en_rectangulo(rect_2.topright,rect_1) or punto_en_rectangulo(rect_2.topleft,rect_1) or punto_en_rectangulo(rect_2.bottomright,rect_1) or punto_en_rectangulo(rect_2.bottomleft,rect_1))

def punto_en_rectangulo(punto:tuple, rect:pygame.Rect) -> bool:
    """Detecta si un punto esta dentro de un rectangulo.

    Args:
        punto (tuple): Punto para analizar.
        rect (pygame.Rect): Rectangulo para analizar.

    Returns:
        bool: Retorna si el punto se encuentra dentro del rectangulo.
    """
    x,y = punto
    return x <= rect.right and x >= rect.left and y >= rect.top and y <= rect.bottom

# colision de circulos
def detectar_colisiones_circulos(rect_1:pygame.Rect,rect_2:pygame.Rect) -> bool:
    """Calcula los radios desde dos rectangulos y detecta la colision entre dos circulos.

    Args:
        rect_1 (pygame.Rect): Primer rectangulo para analizar su circulo interno.
        rect_2 (pygame.Rect): Segundo rectangulo para analizar su circulo interno.

    Returns:
        bool: Retorna si se tocan o no se tocan los dos circulos.
    """
    r1 = calcular_radio(rect_1)
    r2 = calcular_radio(rect_2)
    distancia = distancia_entre_puntos(rect_1.center,rect_2.center)
    return distancia <= r1 + r2

