import pygame
from random import randint
from collissions import *
from utils import *
import math

def create_block(imagen:pygame.Surface = None,left=0,top=0,width=50,height=50,color=(255,255,255),borde=0,radio=0) -> dict:
    """Crea un rectangulo con toda la informacion necesaria para mostrarlo en pantalla.

    Args:
        imagen (pygame.Surface, optional): Imagen que se le asigna al rectangulo. Defaults to None.
        left (int, optional): Coordenada izquierda del rectangulo. Defaults to 0.
        top (int, optional): Coordenada superior del rectangulo. Defaults to 0.
        width (int, optional): Ancho del rectangulo. Defaults to 50.
        height (int, optional): Altura del rectangulo. Defaults to 50.
        color (tuple, optional): Color del rectangulo. Defaults to (255,255,255).
        borde (int, optional): Ancho de borde del rectangulo. Defaults to 0.
        radio (int, optional): Radio del borde del rectangulo. Defaults to 0.

    Returns:
        dict: Devuelve un diccionario con toda la informacion del rectangulo.
    """
    if imagen:
        imagen = pygame.transform.scale(imagen, (width,height))
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"borde":borde,"radio":radio, "img":imagen}

def create_player(settings:dict,imagen:pygame.Surface = None) -> dict:
    """Crea el judagor principal del juego.

    Args:
        settings (dict): Diccionario con toda la informacion de configuracion del juego.
        imagen (pygame.Surface, optional): Superficie de la imagen del jugador principal del juego. Defaults to None.

    Returns:
        dict: Devuelve un diccionario con todal la informacion del jugador principal del juego.
    """
    return create_block(imagen,settings["WIDTH"]//2-settings["PLAYER_WIDTH"],settings["HEIGHT"]//2-settings["PLAYER_HEIGHT"],settings["PLAYER_WIDTH"],settings["PLAYER_HEIGHT"],settings["WHITE"],radio=settings["PLAYER_HEIGHT"]//2)

def create_vault(settings:dict,imagen:pygame.Surface = None) -> dict:
    """Crea un baul para otorgarle al jugador un poder especial.

    Args:
        settings (dict): Diccionario con toda la informacion de configuracion del juego.
        imagen (pygame.Surface, optional): Superficie de la imagen del baul de poder especial. Defaults to None.

    Returns:
        dict: Devuelve un diccionario con toda la informacion del baul de poder especial.
    """
    return create_block(imagen,randint(0,settings["WIDTH"]-settings["VAULT_WIDTH"]),randint(0,settings["HEIGHT"]-settings["VAULT_HEIGHT"]),settings["VAULT_WIDTH"],settings["VAULT_HEIGHT"],settings["MAGENTA"],radio=settings["VAULT_HEIGHT"]//2)

def create_zombie(settings:dict,imagen:pygame.Surface = None) -> dict:
    """Crea un zombie en una posicion aleatorio de la pantalla.

    Args:
        settings (dict): Diccionario con toda la informacion de configuracion del juego.
        imagen (pygame.Surface, optional): Superficie de la imagen del zombie. Defaults to None.

    Returns:
        dict: Devuelve un diccionario con toda la informacion del zombie.
    """
    random_position = generate_random_position(settings)
    return create_block(imagen,random_position[0],random_position[1],settings["ZOMBIE_WIDTH"],settings["ZOMBIE_HEIGHT"],settings["YELLOW"],radio=settings["ZOMBIE_HEIGHT"]//2)

def create_bullet(settings:dict,origen:tuple[int,int], target:tuple[int,int],imagen:pygame.Surface = None,vault_bullet=False) -> dict:
    """Crea una bala individual o triple si esta en posesion del poder especial.

    Args:
        settings (dict): Diccionario con toda la informacion de configuracion del juego.
        origen (tuple[int,int]): Coordenada de origen de la bala.
        target (tuple[int,int]): Coordenada objetivo de la bala.
        imagen (pygame.Surface, optional): Superficie de la imagen de la bala. Defaults to None.
        vault_bullet (bool, optional): Determina si esta en posesion del poder especial. Defaults to False.

    Returns:
        dict: Devuelve un diccionario con toda la informacion de la bala.
    """
    bullet = create_block(imagen,origen[0]-settings["BULLET_WIDTH"]//2,origen[1]-settings["BULLET_HEIGHT"]//2, settings["BULLET_WIDTH"], settings["BULLET_HEIGHT"],settings["RED"],radio=settings["BULLET_HEIGHT"]//2)
    if vault_bullet:
        direccion = (target[0]*settings["BULLET_SPEED"],target[1]*settings["BULLET_SPEED"])  
    else:
        direccion = calcular_direccion(origen,target,settings["BULLET_SPEED"])
    bullet["direc"] = direccion  
    return bullet

def create_vault_bullet(settings:dict,origen:tuple[int,int], target:tuple[int,int],imagen:pygame.Surface = None) -> dict:
    """Crea una rafaga de balas estando en posesion del poder especial con una diferencia angular de 15 grados.

    Args:
        settings (dict): Diccionario con toda la informacion de configuracion del juego.
        origen (tuple[int,int]): Coordenada de origen de las balas.
        target (tuple[int,int]): Coordenada objetivo de la bala central.
        imagen (pygame.Surface, optional): Superficie de la imagen de la bala. Defaults to None.

    Returns:
        dict: Devuelve un diccionario con la informacion de las tres balas.
    """
    angulo = math.degrees(math.atan2(target[1] - origen[1], target[0] - origen[0]))
    dir_izq = calcular_direccion_angulo(angulo - 15)
    dir_der = calcular_direccion_angulo(angulo + 15)
    return (create_bullet(settings,origen,target,imagen),
    create_bullet(settings,origen,dir_izq,imagen,True),
    create_bullet(settings,origen,dir_der,imagen,True))

def load_zombie_list(settings:dict,lista:list,cantidad:int, imagen:pygame.Surface = None) -> None:
    """Carga la cantidad de zombies especificada en la lista destino.

    Args:
        settings (dict): Diccionario con toda la informacion de configuracion del juego.
        lista (list): Lista destino para cargar la cantidad de zombies.
        cantidad (int): Cantidad de zombies a cargar.
        imagen (pygame.Surface, optional): Superficie de la imagen del zombie. Defaults to None.
    """
    for _ in range(cantidad):
        lista.append(create_zombie(settings,imagen))

def show_text(superficie:pygame.Surface, coordenada:tuple[int,int], texto:str, fuente:pygame.font, color:tuple[int,int,int], background_color:tuple[int,int,int] = None) -> None:
    """Dibuja un boton en la superficie y coordenada especificada.

    Args:
        superficie (pygame.Surface): Superficie destino del texto.
        coordenada (tuple[int,int]): Cordenada destino del texto.
        texto (str): Texto a mostrar.
        fuente (pygame.font): Fuente del texto a mostrar.
        color (tuple[int,int,int]): Color del texto a mostrar.
        background_color (tuple[int,int,int], optional): Color de fondo del texto a mostrar. Defaults to None.
    """
    sup_texto = fuente.render(texto,True,color,background_color)
    rect_texto = sup_texto.get_rect()
    rect_texto.center = coordenada
    superficie.blit(sup_texto,rect_texto)

