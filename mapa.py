import pygame
import random
from os import path
from config import *
from classes import *

# --- Caminhos absolutos relativos a este script ---
SCRIPT_DIR    = path.dirname(path.abspath(__file__))
FUNDOS_DIR    = path.join(SCRIPT_DIR, "Fundos")
BOTOES_DIR    = path.join(SCRIPT_DIR, "Botoes")
BARRAS_DIR = path.join(SCRIPT_DIR, "Barra")

def tela_mapa(screen):
    WIDTH = 800 # Largura da tela
    HEIGHT = 600 # Altura da tela
    clock = pygame.time.Clock()

    # Verifica qual mapa carregar
    nome_arquivo_mapa = "mapa_insperina.png" if progresso_jogador.get("insperina desbloqueada") else "mapa.png"
    mapa_path = path.join(FUNDOS_DIR, nome_arquivo_mapa)
    mapa = pygame.image.load(mapa_path).convert()
    mapa = pygame.transform.scale(mapa, (WIDTH, HEIGHT))
    mapa_rect = mapa.get_rect()

    barra1 = pygame.image.load(path.join(BARRAS_DIR, "barra1.png")).convert_alpha()
    barra2 = pygame.image.load(path.join(BARRAS_DIR, "barra2.png")).convert_alpha()
    barra3 = pygame.image.load(path.join(BARRAS_DIR, "barra3.png")).convert_alpha()
    barra4 = pygame.image.load(path.join(BARRAS_DIR, "barra4.png")).convert_alpha()

    # Redimensiona para caber no canto
    barra1 = pygame.transform.scale(barra1, (150, 40))
    barra2 = pygame.transform.scale(barra2, (150, 40))
    barra3 = pygame.transform.scale(barra3, (150, 40))
    barra4 = pygame.transform.scale(barra4, (150, 40))

    # Botões de imagem
    insperimg = pygame.image.load(path.join(BOTOES_DIR, "insper.png")).convert_alpha()
    insperimg = pygame.transform.scale(insperimg, (200, 100))
    botao_insper = BotaoImagem(insperimg, 50, 350)

    jkimg = pygame.image.load(path.join(BOTOES_DIR, "JK.jpg")).convert_alpha()
    jkimg = pygame.transform.scale(jkimg, (200, 100))
    botao_jk = BotaoImagem(jkimg, 600, 350)

    maderoimg = pygame.image.load(path.join(BOTOES_DIR, "madero.jpg")).convert_alpha()
    maderoimg = pygame.transform.scale(maderoimg, (200, 100))
    botao_madero = BotaoImagem(maderoimg, 550, 150)

    botao_piscina_img = pygame.Surface((200, 200), pygame.SRCALPHA)
    botao_piscina_img.fill((0, 0, 0, 0))
    botao_piscina = BotaoImagem(botao_piscina_img, 120, 80)

    # Botão “insperina” transparente
    botao_insperina_img = pygame.Surface((130, 120), pygame.SRCALPHA)
    botao_insperina_img.fill((0, 0, 0, 0))
    botao_insperina = BotaoImagem(botao_insperina_img, 400, 120)  # ajuste x, y conforme sua imagem

    running = True
    state = MAPA

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
    
            if botao_insper.foi_clicado(event):
                state = INSPER
                running = False

            if botao_piscina.foi_clicado(event) and progresso_jogador["piscina"]:
                state = PRE_PSCI
                running = False

            if botao_madero.foi_clicado(event) and progresso_jogador["madero"]:
                state = PRE_MADERO
                running = False

            if botao_jk.foi_clicado(event) and progresso_jogador["jk"]:
                state = PRE_JK
                running = False

            if botao_insperina.foi_clicado(event) and progresso_jogador.get("insperina desbloqueada"):
                state = INSPERINA
                running = False

        botao_insper.desenhar(screen)
        botao_jk.desenhar(screen)
        botao_madero.desenhar(screen)
        botao_piscina.desenhar(screen)
        botao_insperina.desenhar(screen)

        screen.fill(BLACK)
        screen.blit(mapa, mapa_rect)

        # Escolhe a barra com base na progressão
        if progresso_jogador["madero completo"]:
            barra = barra4
        elif progresso_jogador["jk completo"]:
            barra = barra3
        elif progresso_jogador["piscina completa"]:
            barra = barra2
        else:
            barra = barra1

        # Desenha no canto superior esquerdo
        screen.blit(barra, (10, 10))

        pygame.display.flip()

    return state
