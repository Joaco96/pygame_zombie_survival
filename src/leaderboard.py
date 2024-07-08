import pygame
from main import *
from pygame.locals import *
import sys

def leaderboard(SCREEN,FONT,settings):
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
        ranking_text = FONT.render('Leaderboard', True, (255, 0, 0))
        prompt_text = FONT.render('Press Enter', True, settings["WHITE"])

        SCREEN.blit(ranking_text, (SCREEN.get_width() // 2 - ranking_text.get_width() // 2, 200))        
        SCREEN.blit(prompt_text, (SCREEN.get_width() // 2 - prompt_text.get_width() // 2, 400))
        # actualizar pantalla
        pygame.display.flip()