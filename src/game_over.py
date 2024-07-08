import pygame
from main import *
from pygame.locals import *
import sys
from game import *
from utils import *
from creation import *
from read_json import *

def game_over(SCREEN,FONT,scores,settings,score):
    is_running = True
    clock = pygame.time.Clock()
    nombre = []

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
                    
                    # importo puntajes desde json
                    try:
                        json = importar_json('src/leaderboard.json')
                    except FileNotFoundError:
                        print("Archivo de scores no encontrado")
                        terminar()
                    new_scores = sorted_map(lambda a,b: a[1] < b[1],json["scores"])

                    from leaderboard import leaderboard
                    leaderboard(SCREEN,FONT,settings,new_scores,current_score)

        # dibujar pantalla
        SCREEN.fill(settings["BLACK"])
        show_text(SCREEN,(settings["WIDTH"]//2,100),"Game Over",FONT,settings["RED"])
        show_text(SCREEN,(settings["WIDTH"]//2,180),"Enter your name:",FONT,settings["WHITE"])
        show_text(SCREEN,(settings["WIDTH"]//2,225),"".join(nombre),FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,280),f'Score: {score}',FONT,settings["WHITE"])

        # actualizar pantalla
        pygame.display.flip()
    