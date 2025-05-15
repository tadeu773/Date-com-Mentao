import pygame
import random
import sys
from config import *
from os import path

def tela_pscina(screen):
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 32)

    # Cores
    AZUL = (0, 150, 255)
    BRANCO = (255, 255, 255)

    # Carrega as imagens e redimensiona
    jogador_img = pygame.image.load(path.join("Fotos Nadador", "nadador_jogador.png")).convert_alpha()
    bot_img = pygame.image.load(path.join("Fotos Nadador", "nadador_bot.png")).convert_alpha()

    TAMANHO_NADADOR = (80, 40)
    jogador_img = pygame.transform.scale(jogador_img, TAMANHO_NADADOR)
    bot_img = pygame.transform.scale(bot_img, TAMANHO_NADADOR)

    # Posições iniciais
    jogador_x = 50
    bot_x = 50
    y_jogador = 150
    y_bot = 250

    distancia_vitoria = 700
    jogo_ativo = True
    vencedor = ""

    running = True
    while running:
        screen.fill(AZUL)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return QUIT

        if jogo_ativo:
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_SPACE]:
                jogador_x += 5

            bot_x += random.randint(1, 3)

            if jogador_x >= distancia_vitoria:
                vencedor = "Você venceu! 🏆"
                jogo_ativo = False
            elif bot_x >= distancia_vitoria:
                vencedor = "O bot venceu! 🤖"
                jogo_ativo = False

        # Desenha os nadadores com imagens
        screen.blit(jogador_img, (jogador_x, y_jogador))
        screen.blit(bot_img, (bot_x, y_bot))

        # Exibe o resultado
        if not jogo_ativo:
            texto = fonte.render(vencedor, True, BRANCO)
            screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, 20))
            pygame.display.flip()
            pygame.time.delay(2000)
            return MAPA

        pygame.display.flip()
        clock.tick(60)
