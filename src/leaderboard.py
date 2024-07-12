import pygame
from main import *
from pygame.locals import *
from creation import *
import sys
from read_json import *

def leaderboard(SCREEN,TITLE_FONT,FONT,settings,current_score=None):
    is_running = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)

    #cargo imagenes
    imagen_fondo = pygame.transform.scale(pygame.image.load(settings["LEADERBOARD_IMAGE"]), settings["SIZE_SCREEN"])
    
    # importo puntajes desde json
    try:
        json = importar_json('src/leaderboard.json')
    except FileNotFoundError:
        print("Archivo de scores no encontrado")
        terminar()

    if len(json["scores"]) > 1:
        scores = sorted_map(lambda a,b: a[1] < b[1],json["scores"])
    else: scores = json["scores"]
    
    # bucle de pantalla
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
        if current_score != None:
            show_text(SCREEN,(settings["WIDTH"]//2,100),f"Recent score {current_score[0]} - {current_score[1]}",FONT,settings["YELLOW"])

        # mostrar leaderboard
        altura = 240
        for i in range(5):
            try:
                show_text(SCREEN,(settings["WIDTH"]//2,altura) ,f'{scores[i][0]}     -     {scores[i][1]}', FONT, settings["GREEN"])
            except IndexError:
                show_text(SCREEN,(settings["WIDTH"]//2,altura) ,f'***    -     0', FONT, settings["GREEN"])      
            altura += 40

        show_text(SCREEN,(settings["WIDTH"]//2,180),f"Leaderboard",TITLE_FONT,settings["RED"])       
        show_text(SCREEN,(settings["WIDTH"]//2,500),f"Press ENTER",FONT,settings["WHITE"])    

        # actualizar pantalla
        pygame.display.flip()