import pygame
from main import *
from creation import *
from collissions import *
from pygame.locals import *
from game_over import *

def game(SCREEN,TITLE_FONT,FONT,settings,scores):
    # cargo imagenes
    imagen_player = pygame.transform.scale(pygame.image.load(settings["PLAYER_IMAGE"]),(settings["PLAYER_WIDTH"],settings["PLAYER_HEIGHT"]))
    imagen_zombie = pygame.transform.scale(pygame.image.load(settings["ZOMBIE_IMAGE"]),(settings["ZOMBIE_WIDTH"],settings["ZOMBIE_HEIGHT"]))
    imagen_bullet = pygame.transform.scale(pygame.image.load(settings["BULLET_IMAGE"]),(settings["BULLET_WIDTH"],settings["BULLET_HEIGHT"]))
    imagen_vault = pygame.transform.scale(pygame.image.load(settings["VAULT_IMAGE"]),(settings["VAULT_WIDTH"],settings["VAULT_HEIGHT"]))
    imagen_fondo = pygame.transform.scale(pygame.image.load(settings["BACKGROUND_IMAGE"]), settings["SIZE_SCREEN"])

    #cargo sonidos
    gun_sound = pygame.mixer.Sound(settings["GUN_SOUND"])
    impact_player_sound = pygame.mixer.Sound(settings["IMPACT_PLAYER_SOUND"])
    impact_zombie_sound = pygame.mixer.Sound(settings["IMPACT_ZOMBIE_SOUND"])
    vault_sound = pygame.mixer.Sound(settings["VAULT_SOUND"])

    is_running = True
    clock = pygame.time.Clock()
    NEWROUNDEVENT = USEREVENT + 1
    NEWVAULTEVENT = USEREVENT + 2
    pygame.time.set_timer(NEWVAULTEVENT, settings["VAULT_TIME"])
    ENDVAULTEVENT = USEREVENT + 3
    player = create_player(settings,imagen_player)
    zombie_list = []
    vault_list = []
    bullet_list = []
    score = 0
    ronda = 1
    vidas = settings["LIFES"]
    load_zombie_list(settings,zombie_list,settings["CANT_ZOMBIES"],imagen_zombie)

    # configuro direcciones
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    vault_bullet = False

    # cargo musica
    pygame.mixer.music.load(settings["SUSPENSE_MUSIC"])
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)
    playing_music = True

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

                if event.key == pygame.K_p:
                    show_text(SCREEN,settings["CENTER_SCREEN"],f"PAUSA",FONT,settings["RED"])
                    pygame.display.flip()
                    wait_user(pygame.K_p)
                
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
                    if vault_bullet:
                        gun_sound.play()
                        new_vault_bullets = create_vault_bullet(settings,player["rect"].center,event.pos,imagen_bullet)
                        bullet_list.append(new_vault_bullets[0])
                        bullet_list.append(new_vault_bullets[1])
                        bullet_list.append(new_vault_bullets[2])
                    else:
                        gun_sound.play()
                        new_bullet = create_bullet(settings,player["rect"].center,event.pos,imagen_bullet)
                        bullet_list.append(new_bullet)

            if event.type == NEWROUNDEVENT:
                load_zombie_list(settings,zombie_list, settings["CANT_ZOMBIES"] + ronda,imagen_zombie)

            if event.type == NEWVAULTEVENT:
                new_vault = create_vault(settings,imagen_vault)
                vault_list.append(new_vault)

            if event.type == ENDVAULTEVENT:
                vault_bullet = False

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

        # recorro una copia de la lista de zombies
        for zombie in zombie_list[:]:
            direccion = calcular_direccion(zombie["rect"].center,player["rect"].center,settings["ZOMBIE_SPEED"])
            zombie["rect"].move_ip(direccion[0], direccion[1])
            # analizo colisiones
            if detectar_colisiones_circulos(zombie["rect"], player["rect"]):
                impact_player_sound.play()
                zombie_list.remove(zombie)
                vidas -= 1
                vidas_text = FONT.render(f"Vidas: {vidas}",True,settings["WHITE"],None)
                if len(zombie_list) == 0:
                        ronda += 1
                        pygame.time.set_timer(NEWROUNDEVENT, settings["ROUND_START_TIME"], 1)
            if vidas == 0:
                pygame.mixer.music.fadeout(2000)
                game_over(SCREEN,TITLE_FONT,FONT,scores,settings,score)
        
        # recorro una copia de la lista de balas
        for bullet in bullet_list[:]:
            bullet["rect"].move_ip(bullet["direc"][0],bullet["direc"][1])
            if bullet["rect"].right > settings["WIDTH"] or bullet["rect"].left < 0 or bullet["rect"].bottom > settings["HEIGHT"] or bullet["rect"].top < 0:
                bullet_list.remove(bullet)
            for zombie in zombie_list[:]:
                if detectar_colisiones_circulos(zombie["rect"], bullet["rect"]):
                    impact_zombie_sound.play()
                    zombie_list.remove(zombie)
                    score += 1
                    if len(zombie_list) == 0:
                        ronda += 1
                        pygame.time.set_timer(NEWROUNDEVENT, settings["ROUND_START_TIME"],1)

        # recorro una copia de la lista de vaults
        for vault in vault_list[:]:
            if detectar_colisiones_circulos(vault["rect"], player["rect"]):
                vault_sound.play()
                vault_bullet = True
                pygame.time.set_timer(ENDVAULTEVENT, settings["VAULT_DURATION"],1)
                vault_list.remove(vault)                                   
        
        mouse_pos = pygame.mouse.get_pos()
        imagen_player_rotada = rotar_pos(player,mouse_pos)

        for zombie in zombie_list:
            zombie["imagen_rotada"] = rotar_pos(zombie,player["rect"].center)

        # dibujar pantalla
        SCREEN.blit(imagen_fondo,settings["ORIGIN"])
        SCREEN.blit(imagen_player_rotada, imagen_player_rotada.get_rect(center=player["rect"].center))   
        for zombie in zombie_list:
            if zombie["img"]:
                SCREEN.blit(zombie["imagen_rotada"],zombie["imagen_rotada"].get_rect(center=zombie["rect"].center))
            else:
                pygame.draw.rect(SCREEN, zombie["color"], zombie["rect"], border_radius=zombie["radio"])
        for bullet in bullet_list:
            if bullet["img"]:
                SCREEN.blit(bullet["img"], bullet["rect"])
            else:
                pygame.draw.rect(SCREEN, bullet["color"], bullet["rect"], border_radius=bullet["radio"])

        for vault in vault_list:
            if vault["img"]:
                SCREEN.blit(vault["img"], vault["rect"])
            else:
                pygame.draw.rect(SCREEN, vault["color"], vault["rect"], border_radius=vault["radio"])

        show_text(SCREEN,(90,30),f"Round {ronda}",FONT,settings["WHITE"])
        show_text(SCREEN,(settings["WIDTH"]//2,30),f"Score {score}",FONT,settings["WHITE"])
        show_text(SCREEN,(settings["WIDTH"]-90,30),f"Lifes {vidas}",FONT,settings["WHITE"])

        # actualizar pantalla
        pygame.display.flip()

