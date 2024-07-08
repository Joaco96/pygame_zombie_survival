import pygame

# colision de rectangulos
def detectar_colisiones2(rect_1:pygame.Rect,rect_2:pygame.Rect) -> bool:
    return (punto_en_rectangulo(rect_1.topright,rect_2) or punto_en_rectangulo(rect_1.topleft,rect_2) or punto_en_rectangulo(rect_1.bottomright,rect_2) or punto_en_rectangulo(rect_1.bottomleft,rect_2) or punto_en_rectangulo(rect_2.topright,rect_1) or punto_en_rectangulo(rect_2.topleft,rect_1) or punto_en_rectangulo(rect_2.bottomright,rect_1) or punto_en_rectangulo(rect_2.bottomleft,rect_1))

def punto_en_rectangulo(punto:tuple, rect:pygame.Rect) -> bool:
    x,y = punto
    return x <= rect.right and x >= rect.left and y >= rect.top and y <= rect.bottom

def distancia_entre_puntos(pto_1:tuple[int,int],pto_2:tuple[int,int]) -> float:
    return ((pto_1[0] - pto_2[0])**2 + (pto_1[1] - pto_2[1])**2)**0.5 

def calcular_radio(rect) -> float:
    return rect.width // 2

# colision de circulos
def detectar_colisiones_circulos(rect_1:pygame.Rect,rect_2:pygame.Rect) -> bool:
    r1 = calcular_radio(rect_1)
    r2 = calcular_radio(rect_2)
    distancia = distancia_entre_puntos(rect_1.center,rect_2.center)
    return distancia <= r1 + r2

def mov_direccion(origen:tuple[int,int],final:tuple[int,int],speed:int) -> tuple[int,int]:
    dist_x =  final[0] - origen[0]
    dist_y = final[1] - origen[1] 
    dist = distancia_entre_puntos(final, origen)
    dist_x = dist_x / dist * speed
    dist_y = dist_y / dist * speed
    return(dist_x,dist_y)