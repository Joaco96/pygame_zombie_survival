import pygame
from utils import *

# colision de rectangulos
def detectar_colisiones(rect_1:pygame.Rect,rect_2:pygame.Rect) -> bool:
    return (punto_en_rectangulo(rect_1.topright,rect_2) or punto_en_rectangulo(rect_1.topleft,rect_2) or punto_en_rectangulo(rect_1.bottomright,rect_2) or punto_en_rectangulo(rect_1.bottomleft,rect_2) or punto_en_rectangulo(rect_2.topright,rect_1) or punto_en_rectangulo(rect_2.topleft,rect_1) or punto_en_rectangulo(rect_2.bottomright,rect_1) or punto_en_rectangulo(rect_2.bottomleft,rect_1))

def punto_en_rectangulo(punto:tuple, rect:pygame.Rect) -> bool:
    x,y = punto
    return x <= rect.right and x >= rect.left and y >= rect.top and y <= rect.bottom

# colision de circulos
def detectar_colisiones_circulos(rect_1:pygame.Rect,rect_2:pygame.Rect) -> bool:
    r1 = calcular_radio(rect_1)
    r2 = calcular_radio(rect_2)
    distancia = distancia_entre_puntos(rect_1.center,rect_2.center)
    return distancia <= r1 + r2

