import pygame
from main import *
from pygame.locals import *
import sys

def controls(SCREEN,TITLE_FONT,FONT,settings):
    is_running = True
    clock = pygame.time.Clock()
    imagen_fondo = pygame.transform.scale(pygame.image.load(settings["CONTROLS_IMAGE"]), settings["SIZE_SCREEN"])

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

        SCREEN.blit(imagen_fondo,settings["ORIGIN"])
        show_text(SCREEN,(settings["WIDTH"]//2,100),"Controls",TITLE_FONT,settings["RED"])
        show_text(SCREEN,(settings["WIDTH"]//2,220),"IAI IWI ISI IDI - Movimiento personaje",FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,270),"Click IZQ Mouse - Disparo",FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,320),"IPI - Pausa",FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,370),"IMI - Mute",FONT,settings["YELLOW"])
        show_text(SCREEN,(settings["WIDTH"]//2,500),"Press ENTER for Main Menu",FONT,settings["WHITE"])
        
        # actualizar pantalla
        pygame.display.flip()
    