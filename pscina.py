import pygame
import random
import sys
from os import path
from config import *

# Caminhos
SCRIPT_DIR    = path.dirname(path.abspath(__file__))
NADADORES_DIR = path.join(SCRIPT_DIR, "Fotos Nadador")

def tela_pscina(screen):
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 32)
    VERDE = (0, 200, 0)
    fundo = pygame.image.load(path.join(SCRIPT_DIR, "Fundos", "piscina.jpg")).convert()
    fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))

    # Carrega sprites do jogador e bot
    sprites_jogador = [
        pygame.image.load(path.join(NADADORES_DIR, "nadador1.png")).convert_alpha(),
        pygame.image.load(path.join(NADADORES_DIR, "nadador2.png")).convert_alpha()
    ]
    sprites_bot = [
        pygame.image.load(path.join(NADADORES_DIR, "bot1.png")).convert_alpha(),
        pygame.image.load(path.join(NADADORES_DIR, "bot2.png")).convert_alpha()
    ]

    TAMANHO_NAD = (80, 40)
    for i in range(len(sprites_jogador)):
        sprites_jogador[i] = pygame.transform.scale(sprites_jogador[i], TAMANHO_NAD)
        sprites_bot[i] = pygame.transform.scale(sprites_bot[i], TAMANHO_NAD)

    jogador_x, bot_x = 50, 50
    y_jogador, y_bot = 200, 300
    distancia_vitoria = 700
    jogo_ativo = True
    vencedor = ""
    state = PSCINA

    sprite_index_jogador = 0
    sprite_index_bot = 0
    anim_timer_bot = 0
    ANIM_INTERVAL_BOT = 10

    # Contagem regressiva
    for contagem in range(3, 0, -1):
        screen.blit(fundo, (0, 0))
        texto_info = fonte.render("A competição irá começar em:", True, VERDE)
        texto_contagem = fonte.render(str(contagem), True, VERDE)
        texto_instrucao = fonte.render("Aperte a barra de espaço para nadar", True, VERDE)

        screen.blit(texto_info, (WIDTH // 2 - texto_info.get_width() // 2, HEIGHT // 2 - 90))
        screen.blit(texto_contagem, (WIDTH // 2 - texto_contagem.get_width() // 2, HEIGHT // 2 - 30))
        screen.blit(texto_instrucao, (WIDTH // 2 - texto_instrucao.get_width() // 2, HEIGHT // 2 + 30))
        pygame.display.flip()
        pygame.time.delay(1000)

    while True:
        clock.tick(FPS)
        screen.blit(fundo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return QUIT

            # Troca o sprite do jogador somente quando a tecla espaço é pressionada
            if jogo_ativo and evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                jogador_x += 21
                sprite_index_jogador = (sprite_index_jogador + 1) % len(sprites_jogador)

        # Atualiza o sprite do bot automaticamente
        if jogo_ativo:
            bot_x += random.randint(1, 3)
            anim_timer_bot += 1
            if anim_timer_bot >= ANIM_INTERVAL_BOT:
                sprite_index_bot = (sprite_index_bot + 1) % len(sprites_bot)
                anim_timer_bot = 0

            if jogador_x >= distancia_vitoria:
                vencedor = "Você venceu!"
                jogo_ativo = False
            elif bot_x >= distancia_vitoria:
                vencedor = "O Mentão venceu!"
                jogo_ativo = False

            if not jogo_ativo:
                texto = fonte.render(vencedor, True, VERDE)
                screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, 20))
                pygame.display.flip()
                pygame.time.delay(2000)
                return MAPA

        screen.blit(sprites_jogador[sprite_index_jogador], (jogador_x, y_jogador))
        screen.blit(sprites_bot[sprite_index_bot], (bot_x, y_bot))

        pygame.display.flip()