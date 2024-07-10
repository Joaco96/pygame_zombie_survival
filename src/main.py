import pygame
from creation import *
from collissions import *
from pygame.locals import *
from leaderboard import *
from read_json import *
from game import *

# inicializo modulos de pygame
pygame.init()

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

# fuente
TITLE_FONT = pygame.font.Font(settings["TITLE_FONT"],48)   
FONT = pygame.font.Font(settings["FONT"],48)   

# icono
icono = pygame.image.load(settings["ICON_IMAGE"])
pygame.display.set_icon(icono)

def main():
    imagen_fondo = pygame.transform.scale(pygame.image.load(settings["MENU_IMAGE"]), settings["SIZE_SCREEN"])

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
                game(SCREEN,TITLE_FONT,FONT,settings,scores)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                from controls import controls
                controls(SCREEN,TITLE_FONT,FONT,settings)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                from leaderboard import leaderboard
                leaderboard(SCREEN,TITLE_FONT,FONT,settings)

        SCREEN.blit(imagen_fondo,settings["ORIGIN"])
        show_text(SCREEN,(settings["WIDTH"]//2,115),"ZOMBIE SURVIVAL",TITLE_FONT,settings["RED"])
        show_text(SCREEN,(settings["WIDTH"]//2,275),"P    Play",FONT,settings["WHITE"])
        show_text(SCREEN,(settings["WIDTH"]//2,350),"C    Controls",FONT,settings["WHITE"])
        show_text(SCREEN,(settings["WIDTH"]//2,425),"L    Leaderboard",FONT,settings["WHITE"])
        pygame.display.flip()

if __name__ == '__main__':
    main()


