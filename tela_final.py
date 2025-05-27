import pygame
import random
from os import path

from config import *

# --- Caminhos absolutos relativos a este script ---
SCRIPT_DIR  = path.dirname(path.abspath(__file__))
FUNDOS_DIR  = path.join(SCRIPT_DIR, "Fundos")


def tela_final(screen):
    clock = pygame.time.Clock()

    # Carrega imagem final do jogo
    background_path = path.join(FUNDOS_DIR, "fim_feliz.jpg")
    background = pygame.image.load(background_path).convert()
    WIDTH, HEIGHT = background.get_size()
    background_rect = background.get_rect()

    # Define fonte
    font_titulo = pygame.font.Font(None, 80)
    font_texto  = pygame.font.Font(None, 50)

    # Textos
    texto_titulo = font_titulo.render("Fim de Jogo", True, WHITE)
    texto_titulo_rect = texto_titulo.get_rect(center=(WIDTH // 2, 40))

    texto_conquista = font_texto.render("Você conquistou o Mentão!", True, WHITE)
    texto_conquista_rect = texto_conquista.get_rect(center=(WIDTH // 2, 100))

    # Botão "Voltar para o mapa"
    button_width   = 300
    button_height  = 70
    button_x       = (WIDTH - button_width) // 2
    button_y       = HEIGHT - button_height - 40
    button_rect    = pygame.Rect(button_x, button_y, button_width, button_height)
    texto_botao    = font_texto.render("Voltar para o mapa", True, WHITE)
    texto_botao_rect = texto_botao.get_rect(center=button_rect.center)

    running = True
    state = TELA_FINAL
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
        screen.blit(texto_titulo, texto_titulo_rect)
        screen.blit(texto_conquista, texto_conquista_rect)

        # 🔴 Desenha o botão com contorno branco para dar destaque
        pygame.draw.rect(screen, RED, button_rect, border_radius=12)
        pygame.draw.rect(screen, WHITE, button_rect, 3, border_radius=12)  # contorno branco
        screen.blit(texto_botao, texto_botao_rect)

        pygame.display.flip()

    return state
