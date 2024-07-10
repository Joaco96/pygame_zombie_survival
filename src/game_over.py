import pygame
from main import *
from pygame.locals import *
import sys
from game import *
from utils import *
from creation import *
from read_json import *

def game_over(SCREEN,TITLE_FONT,FONT,scores,settings,score):
    is_running = True
    clock = pygame.time.Clock()
    nombre = []
    imagen_fondo = pygame.transform.scale(pygame.image.load(settings["LEADERBOARD_IMAGE"]), settings["SIZE_SCREEN"])

    # bucle de pantalla
    while is_running:
        clock.tick(settings["FPS"])
        
        # analizar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if 122 >= event.key >= 97:
                    nombre.append(event.unicode)
                    show_text(SCREEN,(settings["WIDTH"]//2,150),event.unicode,FONT,settings["YELLOW"])
                    pygame.display.flip()
                if len(nombre) >= 3:
                    current_score = ("".join(nombre),score)
                    # actualizo puntajes
                    try:
                        actualizar_scores("src/leaderboard.json",current_score)
                    except FileNotFoundError:
                        print("Archivo de scores no encontrado")
                        terminar()
                    from leaderboard import leaderboard
                    leaderboard(SCREEN,TITLE_FONT,FONT,settings,current_score)

        # dibujar pantalla
        SCREEN.blit(imagen_fondo,settings["ORIGIN"])
        show_text(SCREEN,(settings["WIDTH"]//2,100),"Game Over",TITLE_FONT,settings["RED"])
        show_text(SCREEN,(settings["WIDTH"]//2,225),"Enter your name",FONT,settings["WHITE"])
        show_text(SCREEN,(settings["WIDTH"]//2,280),"".join(nombre),FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,345),f'Score {score}',FONT,settings["WHITE"])

        # actualizar pantalla
        pygame.display.flip()
    