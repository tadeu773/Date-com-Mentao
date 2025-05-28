import pygame
import random
from os import path

from config import *

# --- Caminhos absolutos relativos a este script ---
SCRIPT_DIR  = path.dirname(path.abspath(__file__))
MUSIC_FILE  = path.join(SCRIPT_DIR, "Musicas", "penelope.mp3")
FUNDOS_DIR  = path.join(SCRIPT_DIR, "Fundos")

# --- Inicializa áudio ---
pygame.mixer.init()
if not path.exists(MUSIC_FILE):
    raise FileNotFoundError(f"Não encontrei a música em: {MUSIC_FILE}")
pygame.mixer.music.load(MUSIC_FILE)
pygame.mixer.music.play(-1)

def init_screen(screen):
    global progresso_jogador
    progresso_jogador = {
        "piscina": False,
        "madero": False,
        "jk": False,
        "piscina completa": False,
        "jk completo": False,
        "madero completo": False,
        "insperina desbloqueada": False
        }
    
    clock = pygame.time.Clock()

    # Carrega e ajusta o fundo de tela inicial
    background_path = path.join(FUNDOS_DIR, "inicio.png")
    background = pygame.image.load(background_path).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # Carrega o título como imagem
    titulo_path = path.join(FUNDOS_DIR, "titulo.png")
    titulo = pygame.image.load(titulo_path).convert_alpha()
    titulo_rect = titulo.get_rect(center=(500, 450))  # Pode ajustar a altura
    titulo = pygame.transform.scale(titulo, (250, 250))  # ajuste os valores conforme necessário

    # Botão "JOGAR"
    font = pygame.font.Font(None, 60)
    button_width   = 200
    button_height  = 80
    button_x       = 550
    button_y       =  150
    button_rect    = pygame.Rect(button_x, button_y, button_width, button_height)
    text_jogar     = font.render("JOGAR", True, WHITE)
    text_jogar_rect= text_jogar.get_rect(center=button_rect.center)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if button_rect.collidepoint(event.pos):
                    state = MAPA
                    running = False

        # Desenha tudo
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        screen.blit(titulo, titulo_rect)
        pygame.draw.rect(screen, RED, button_rect, border_radius=12)
        screen.blit(text_jogar, text_jogar_rect)

        pygame.display.flip()

    return state
