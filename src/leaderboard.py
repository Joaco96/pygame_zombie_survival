import pygame
from main import *
from pygame.locals import *
from creation import *
import sys

def leaderboard(SCREEN,FONT,settings,scores,current_score=None):
    is_running = True
    clock = pygame.time.Clock()

    # bucle de juego
    while is_running:
        clock.tick(settings["FPS"])
        # analizar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                from main import main
                main()

        SCREEN.fill(settings["BLACK"])
        
        # armar leaderboard
        altura = 240
        for i in range(5):
            try:
                show_text(SCREEN,(settings["WIDTH"]//2,altura) ,f'{scores[i][0]}     -     {scores[i][1]}', FONT, settings["GREEN"])
            except IndexError:
                show_text(SCREEN,(settings["WIDTH"]//2,altura) ,f'***    -     0', FONT, settings["GREEN"])
      
            altura += 40
        if current_score:
            show_text(SCREEN,(settings["WIDTH"]//2,100),f"Recent score: {current_score[0]} - {current_score[1]}",FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,200),f"Leaderboard",FONT,settings["RED"])       
        show_text(SCREEN,(settings["WIDTH"]//2,500),f"Press ENTER",FONT,settings["WHITE"])    

        # actualizar pantalla
        pygame.display.flip()