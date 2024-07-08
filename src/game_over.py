import pygame
from main import *
from pygame.locals import *
import sys
from game import *

def game_over(SCREEN,FONT,score,settings):
    is_running = True
    clock = pygame.time.Clock()

    # bucle de pantalla
    while is_running:
        clock.tick(settings["FPS"])

        # analizar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                from main import main
                main()

        SCREEN.fill(settings["BLACK"])
        game_over_text = FONT.render('Game Over', True, (255, 0, 0))
        score_text = FONT.render(f'Score: {score}', True, settings["WHITE"])
        prompt_text = FONT.render('Press Enter', True, settings["WHITE"])

        SCREEN.blit(game_over_text, (SCREEN.get_width() // 2 - game_over_text.get_width() // 2, 200))
        SCREEN.blit(score_text, (SCREEN.get_width() // 2 - score_text.get_width() // 2, 300))
        SCREEN.blit(prompt_text, (SCREEN.get_width() // 2 - prompt_text.get_width() // 2, 400))
        # actualizar pantalla
        pygame.display.flip()
    