import pygame
from random import randint
from collissions import *

def create_block(imagen:pygame.Surface = None,left=0,top=0,width=50,height=50,color=(255,255,255),borde=0,radio=0):
    if imagen:
        imagen = pygame.transform.scale(imagen, (width,height))
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"borde":borde,"radio":radio, "img":imagen}

def create_player(settings,imagen:pygame.Surface = None):
    return create_block(imagen,settings["WIDTH"]//2-settings["PLAYER_WIDTH"],settings["HEIGHT"]//2-settings["PLAYER_HEIGHT"],settings["PLAYER_WIDTH"],settings["PLAYER_HEIGHT"],settings["WHITE"],radio=settings["PLAYER_HEIGHT"]//2)

def create_zombie(settings,imagen:pygame.Surface = None):
    random_position = generate_random_position(settings)
    return create_block(imagen,random_position[0],random_position[1],settings["ZOMBIE_WIDTH"],settings["ZOMBIE_HEIGHT"],settings["YELLOW"],radio=settings["ZOMBIE_HEIGHT"]//2)

def create_bullet(settings,origen:tuple[int,int], target:tuple[int,int],imagen:pygame.Surface = None):
    bullet = create_block(imagen,origen[0]-settings["BULLET_WIDTH"]//2,origen[1]-settings["BULLET_HEIGHT"]//2, settings["BULLET_WIDTH"], settings["BULLET_HEIGHT"],settings["RED"],radio=settings["BULLET_HEIGHT"]//2)
    direccion = mov_direccion(origen,target,settings["BULLET_SPEED"])
    bullet["direc"] = direccion  
    return bullet

def load_zombie_list(settings,lista:list,cantidad:int, imagen:pygame.Surface = None):
    for _ in range(cantidad):
        lista.append(create_zombie(settings,imagen))

def show_text(superficie:pygame.Surface, coordenada:tuple[int,int], texto:str, fuente:pygame.font, color:tuple[int,int,int], background_color:tuple[int,int,int] = None):
    sup_texto = fuente.render(texto,True,color,background_color)
    rect_texto = sup_texto.get_rect()
    rect_texto.center = coordenada
    superficie.blit(sup_texto,rect_texto)
    pygame.display.flip()

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
