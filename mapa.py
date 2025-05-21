import pygame
import random
from os import path
from config import *
from classes import *

# --- Caminhos absolutos relativos a este script ---
SCRIPT_DIR    = path.dirname(path.abspath(__file__))
FUNDOS_DIR    = path.join(SCRIPT_DIR, "Fundos")
BOTOES_DIR    = path.join(SCRIPT_DIR, "Botoes")

def tela_mapa(screen):
    clock = pygame.time.Clock()

    # Carrega e ajusta o mapa de fundo
    mapa_path = path.join(FUNDOS_DIR, "mapa.png")
    mapa = pygame.image.load(mapa_path).convert()
    mapa = pygame.transform.scale(mapa, (WIDTH, HEIGHT))
    mapa_rect = mapa.get_rect()

    # Botões de imagem
    # Insper
    insper_path = path.join(BOTOES_DIR, "insper.png")
    insperimg = pygame.image.load(insper_path).convert_alpha()
    insperimg = pygame.transform.scale(insperimg, (200, 100))
    botao_insper = BotaoImagem(insperimg, 50, 350)

    # JK
    jk_path = path.join(BOTOES_DIR, "JK.jpg")
    jkimg = pygame.image.load(jk_path).convert_alpha()
    jkimg = pygame.transform.scale(jkimg, (200, 100))
    botao_jk = BotaoImagem(jkimg, 600, 350)

    # Madero
    madero_path = path.join(BOTOES_DIR, "madero.jpg")
    maderoimg = pygame.image.load(madero_path).convert_alpha()
    maderoimg = pygame.transform.scale(maderoimg, (200, 100))
    botao_madero = BotaoImagem(maderoimg, 550, 150)

    # Botão “piscina” transparente
    botao_piscina_img = pygame.Surface((200, 200), pygame.SRCALPHA)
    botao_piscina_img.fill((0, 0, 0, 0))
    # Ajuste x,y conforme sua arte do mapa
    botao_piscina = BotaoImagem(botao_piscina_img, 120, 80)

    running = True
    state = MAPA

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            # Cliques nos botões
            if botao_insper.foi_clicado(event):
                state = INSPER
                running = False

            if botao_piscina.foi_clicado(event) and progresso_jogador["piscina"]:
                state = PRE_PSCI
                running = False

            if botao_madero.foi_clicado(event) and progresso_jogador["madero"]:
                state = QUIT
                running = False

            if botao_jk.foi_clicado(event):
                state = JK
                running = False

        # Desenha tudo
        screen.fill(BLACK)

        botao_insper.desenhar(screen)
        botao_jk.desenhar(screen)
        botao_madero.desenhar(screen)
        botao_piscina.desenhar(screen)
        screen.blit(mapa, mapa_rect)

        pygame.display.flip()

    return state

