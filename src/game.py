import pygame
from main import *
from creation import *
from collissions import *
from pygame.locals import *
from game_over import *

def game(SCREEN,FONT,settings):
    is_running = True
    clock = pygame.time.Clock()
    player = create_player(settings)
    zombie_list = []
    bullet_list = []
    score = 0
    ronda = 1
    vidas = 5
    load_zombie_list(settings,zombie_list,settings["CANT_ZOMBIES"])
    score_text = FONT.render(f"Score: {score}",True,settings["WHITE"],None)
    ronda_text = FONT.render(f"Ronda: {ronda}",True,settings["WHITE"],None)
    vidas_text = FONT.render(f"Vidas: {vidas}",True,settings["WHITE"],None)
    # configuro direcciones
    move_left = False
    move_right = False
    move_up = False
    move_down = False

    # bucle de juego
    while is_running:
        clock.tick(settings["FPS"])

        # analizar eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                is_running = False
                terminar()
            # eventos de presionado de teclas
            if event.type == KEYDOWN:
                if event.key == K_s:
                    move_down = True
                    move_up = False
                if event.key == K_w:
                    move_up = True
                    move_down = False
                if event.key == K_a:
                    move_left = True
                    move_right = False
                if event.key == K_d:
                    move_right = True
                    move_left = False
                if event.key == K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    playing_music = not playing_music
                
            if event.type == KEYUP:
                if event.key == K_s:
                    move_down = False
                if event.key == K_w:
                    move_up = False
                if event.key == K_a:
                    move_left = False
                if event.key == K_d:
                    move_right = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_bullet = create_bullet(settings,player["rect"].center,event.pos)
                    bullet_list.append(new_bullet)

        # actualizar movimiento
        if move_left and player["rect"].left > 0:
            player["rect"].x -= settings["PLAYER_SPEED"]
            if player["rect"].left < 0:
                player["rect"].left = 0
        if move_right and player["rect"].right < settings["WIDTH"]:
            player["rect"].x += settings["PLAYER_SPEED"]
            if player["rect"].right > settings["WIDTH"]:
                player["rect"].right = settings["WIDTH"]
        if move_up and player["rect"].top > 0:
            player["rect"].y -= settings["PLAYER_SPEED"]
            if player["rect"].top < 0:
                player["rect"].top = 0
        if move_down and player["rect"].bottom < settings["HEIGHT"]:
            player["rect"].y += settings["PLAYER_SPEED"]
            if player["rect"].bottom > settings["HEIGHT"]:
                player["rect"].bottom = settings["HEIGHT"]

        # recorro una copia de la lista zombies
        for zombie in zombie_list[:]:
            direccion = mov_direccion(zombie["rect"].center,player["rect"].center,settings["ZOMBIE_SPEED"])
            zombie["rect"].move_ip(direccion[0], direccion[1])
            # analizo colisiones
            if detectar_colisiones_circulos(zombie["rect"], player["rect"]):
                zombie_list.remove(zombie)
                vidas -= 1
                vidas_text = FONT.render(f"Vidas: {vidas}",True,settings["WHITE"],None)
                if len(zombie_list) == 0:
                        ronda += 1
                        load_zombie_list(settings,zombie_list, settings["CANT_ZOMBIES"] + ronda)
                        ronda_text = FONT.render(f"Ronda: {ronda}",True,settings["WHITE"],None)
            if vidas == 0:
                game_over(SCREEN,FONT,score,settings)
        for bullet in bullet_list[:]:
            bullet["rect"].move_ip(bullet["direc"][0],bullet["direc"][1])
            for zombie in zombie_list[:]:
                if detectar_colisiones_circulos(zombie["rect"], bullet["rect"]):
                    zombie_list.remove(zombie)
                    score += 1
                    score_text = FONT.render(f"Score: {score}",True,settings["WHITE"],None)
                    if len(zombie_list) == 0:
                        ronda += 1
                        load_zombie_list(settings,zombie_list, settings["CANT_ZOMBIES"] + ronda)
                        ronda_text = FONT.render(f"Ronda: {ronda}",True,settings["WHITE"],None)
        # dibujar pantalla
        SCREEN.fill(settings["BLACK"])
        # SCREEN.blit(imagen_fondo,ORIGIN)

        # los rectangulos se dibujan, las superficies se blitean
        # SCREEN.blit(block["img"], block["rect"])
        pygame.draw.rect(SCREEN, player["color"], player["rect"], player["borde"],player["radio"])
        
        for zombie in zombie_list:
            if zombie["img"]:
                SCREEN.blit(zombie["img"], zombie["rect"])
            else:
                pygame.draw.rect(SCREEN, zombie["color"], zombie["rect"], border_radius=zombie["radio"])
        for bullet in bullet_list:
            if bullet["img"]:
                SCREEN.blit(bullet["img"], bullet["rect"])
            else:
                pygame.draw.rect(SCREEN, bullet["color"], bullet["rect"], border_radius=bullet["radio"])

        SCREEN.blit(score_text,((settings["WIDTH"]//2-score_text.get_width()//2),20))
        SCREEN.blit(ronda_text,((ronda_text.get_width()//2),20))
        SCREEN.blit(vidas_text,((settings["WIDTH"]-vidas_text.get_width()),20))

        # actualizar pantalla
        pygame.display.flip()
