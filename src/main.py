import pygame
from creation import *
from collissions import *
from pygame.locals import *
from leaderboard import *
from read_json import *
import sys
from game import *

# inicializo modulos de pygame
pygame.init()

# Imagenes -> archivos .bmp no tienen compresion
# cargo imagenes
# imagen_player = pygame.image.load("path del archivo") por ejemplo -> ("./src./assets/player.jpg")
# imagen_fondo = pygame.transform.scale(pygame.image.load("path del archivo"), SIZE_SCREEN)
# 

# Audio -> Sonido(guardo en variables para usar) o Musica(uno solo en pygame)
# cargo sonidos
# collision_sound = pygame.mixer.Sound("path donde esta el archivo") por ejemplo -> ("./src./assets/coin.mp3")
# collision_sound.play() para que suene

# importo configuracion desde json
try:
    json = importar_json('src/settings.json')
except FileNotFoundError:
    print("Archivo de configuracion no encontrado")
    terminar()
settings = json["settings"]

# configurar pantalla
SCREEN = pygame.display.set_mode(settings["SIZE_SCREEN"])
pygame.display.set_caption("Zombie Survival")

# fuentea
FONT = pygame.font.SysFont(None,48)    

SCREEN.fill(settings["BLACK"])
show_text(SCREEN,settings["CENTER_SCREEN"],"ZOMBIE SURVIVAL",FONT, settings["RED"])
show_text(SCREEN,(settings["WIDTH"] //2, settings["HEIGHT"] -50), "Presione SPACE para comenzar",FONT,settings["BLUE"])
pygame.display.flip()

def main():
    # importo puntajes desde json
    try:
        json = importar_json('src/leaderboard.json')
    except FileNotFoundError:
        print("Archivo de scores no encontrado")
        terminar()
    scores = json["scores"]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                from game import game
                game(SCREEN,FONT,settings,scores)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                from controls import controls
                controls(SCREEN,FONT,settings)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                from leaderboard import leaderboard
                leaderboard(SCREEN,FONT,settings,scores)

        SCREEN.fill(settings["BLUE"])

        show_text(SCREEN,(settings["WIDTH"]//2,115),"ZOMBIE SURVIVAL",FONT,settings["BLACK"])
        show_text(SCREEN,(settings["WIDTH"]//2,275),"P - Play",FONT,settings["BLACK"])
        show_text(SCREEN,(settings["WIDTH"]//2,350),"C - Controls",FONT,settings["BLACK"])
        show_text(SCREEN,(settings["WIDTH"]//2,425),"L - Leaderboard",FONT,settings["BLACK"])
        pygame.display.flip()

if __name__ == '__main__':
    main()


