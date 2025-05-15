import pygame
import random
import sys
from os import path

from config import *

# --- Caminhos relativos a este script ---
SCRIPT_DIR        = path.dirname(path.abspath(__file__))
NADADORES_DIR     = path.join(SCRIPT_DIR, "Fotos Nadador")

def tela_pscina(screen):
    clock    = pygame.time.Clock()
    fonte    = pygame.font.SysFont("arial", 32)
    AZUL     = (0, 150, 255)
    BRANCO   = (255, 255, 255)

    # Carrega as imagens e redimensiona
    jogador_img = pygame.image.load(path.join(NADADORES_DIR, "nadador_jogador.png")).convert_alpha()
    bot_img     = pygame.image.load(path.join(NADADORES_DIR, "nadador_bot.png")).convert_alpha()
    TAMANHO_NAD = (80, 40)
    jogador_img = pygame.transform.scale(jogador_img, TAMANHO_NAD)
    bot_img     = pygame.transform.scale(bot_img,     TAMANHO_NAD)

    # Posições iniciais
    jogador_x, bot_x = 50, 50
    y_jogador, y_bot = 150, 250

    distancia_vitoria = 700
    jogo_ativo        = True
    vencedor          = ""
    state             = PSCINA  # estado atual

    while True:
        clock.tick(FPS)
        screen.fill(AZUL)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                state = QUIT
                return state

            # Movimento do jogador: um passo por aperto de espaço
            if jogo_ativo and evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                jogador_x += 7   # jogador um pouco mais rápido

        # Movimento automático do bot
        if jogo_ativo:
            bot_x += random.randint(1, 3)

            # Verifica vitória
            if jogador_x >= distancia_vitoria:
                vencedor   = "Você venceu! 🏆"
                jogo_ativo = False
            elif bot_x >= distancia_vitoria:
                vencedor   = "O bot venceu! 🤖"
                jogo_ativo = False

            # Se alguém ganhou, aguarda, retorna ao mapa
            if not jogo_ativo:
                texto = fonte.render(vencedor, True, BRANCO)
                screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, 20))
                pygame.display.flip()
                pygame.time.delay(2000)
                return MAPA

        # Desenha nadadores com imagens
        screen.blit(jogador_img, (jogador_x, y_jogador))
        screen.blit(bot_img,     (bot_x,     y_bot))

        pygame.display.flip()
