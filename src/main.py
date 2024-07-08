import pygame
from creation import *
from collissions import *
from pygame.locals import *
from leaderboard import *
from read_json import *
import sys
from game import *
from controls import controls

# inicializo modulos de pygame
pygame.init()

def terminar():
    pygame.quit()
    exit()

NEWCOINEVENT = USEREVENT + 1

# Imagenes -> archivos .bmp no tienen compresion
# cargo imagenes
# imagen_player = pygame.image.load("path del archivo") por ejemplo -> ("./src./assets/player.jpg")
# imagen_fondo = pygame.transform.scale(pygame.image.load("path del archivo"), SIZE_SCREEN)
# 

# Audio -> Sonido(guardo en variables para usar) o Musica(uno solo en pygame)
# cargo sonidos
# collision_sound = pygame.mixer.Sound("path donde esta el archivo") por ejemplo -> ("./src./assets/coin.mp3")
# collision_sound.play() para que suene

# cargo musica
# pygame.mixer.music.load("path del archivo")
# pygame.mixer.music.set_volume(0 a 1)
# pygame.mixer.music.play()

# playing_music = True

# seteo intervalo
pygame.time.set_timer(NEWCOINEVENT, 5000)

# importo configuracion desde json
try:
    json = cargar_json('src/settings.json')
except FileNotFoundError:
    print("Archivo no encontrado")
    terminar()
settings = json["settings"]

# configurar pantalla
SCREEN = pygame.display.set_mode(settings["SIZE_SCREEN"])
pygame.display.set_caption("Zombie Survival")

# fuente
FONT = pygame.font.SysFont(None,48)    

SCREEN.fill(settings["BLACK"])
show_text(SCREEN,settings["CENTER_SCREEN"],"ZOMBIE SURVIVAL",FONT, settings["RED"])
show_text(SCREEN,(settings["WIDTH"] //2, settings["HEIGHT"] -50), "Presione SPACE para comenzar",FONT,settings["BLUE"])
pygame.display.flip()

def main():
    while True:
            SCREEN.fill(settings["BLUE"])

            title = FONT.render('ZOMBIE SURVIVAL', True, (0, 0, 0))
            play_button = FONT.render('Play', True, (0, 0, 0))
            config_button = FONT.render('Controls', True, (0, 0, 0))
            ranking_button = FONT.render('Leaderboard', True, (0, 0, 0))

            SCREEN.blit(title, (settings["WIDTH"] // 2 - title.get_width() // 2, 100))
            SCREEN.blit(play_button, (settings["WIDTH"] // 2 - play_button.get_width() // 2, 250))
            SCREEN.blit(config_button, (settings["WIDTH"] // 2 - config_button.get_width() // 2, 350))
            SCREEN.blit(ranking_button, (settings["WIDTH"] // 2 - ranking_button.get_width() // 2, 450))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminar()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 250 < event.pos[1] < 250 + play_button.get_height():
                        from game import game
                        game(SCREEN,FONT,settings)
                    elif 350 < event.pos[1] < 350 + config_button.get_height():
                        from controls import controls
                        controls(SCREEN,FONT,settings)
                    elif 450 < event.pos[1] < 450 + ranking_button.get_height():
                        from leaderboard import leaderboard
                        leaderboard(SCREEN,FONT,settings)

if __name__ == '__main__':
    main()


