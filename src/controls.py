import pygame
from main import *
from pygame.locals import *
import sys

def controls(SCREEN,FONT,settings):
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
        show_text(SCREEN,(settings["WIDTH"]//2,100),"Controls",FONT,settings["RED"])
        show_text(SCREEN,(settings["WIDTH"]//2,180),"[A] [W] [S] [D] -> Movimiento personaje",FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,230),"Click IZQ Mouse -> Disparo",FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,280),"[P] -> Pausa",FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,330),"[M] -> Mute",FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,500),"Press ENTER for Main Menu",FONT,settings["WHITE"])
        
        # actualizar pantalla
        pygame.display.flip()
    