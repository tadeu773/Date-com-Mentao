import pygame
import random
import time
import os
from config import *
from classes import *

# Tela principal do jogo
def tela_pipoca(screen):
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 26)

    fundo = carregar_imagem(os.path.join(IMAGENS_PIPOCA_DIR, "cinema.png"), (WIDTH, HEIGHT))

    todos_sprites = pygame.sprite.Group()
    blocos_menores = pygame.sprite.Group()

    jogador = BlocoMaior()
    todos_sprites.add(jogador)

    coletados = 0
    perdidos = 0
    tempo_total = 90
    tempo_inicio = time.time()

    running = True

    while running:
        tempo_restante = max(0, int(tempo_total - (time.time() - tempo_inicio)))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                state = QUIT
                running = False

        if random.random() < 0.02:
            bloco = BlocoMenor()
            todos_sprites.add(bloco)
            blocos_menores.add(bloco)

        for bloco in list(blocos_menores):
            bloco.update()
            if bloco.rect.top > HEIGHT:
                bloco.kill()
                perdidos += 1
            elif jogador.rect.colliderect(bloco.rect):
                bloco.kill()
                coletados += 1

        jogador.update()

        if coletados >= 15:
            state = MAPA
            running = False
        elif perdidos >= 10 or tempo_restante <= 0:
            state = GAMEOVER
            running = False

        screen.blit(fundo, (0, 0))
        todos_sprites.draw(screen)
        desenhar_texto(f'Coletados: {coletados}', fonte, PRETO, screen, 10, 10)
        desenhar_texto(f'Perdidos: {perdidos}', fonte, PRETO, screen, 10, 50)
        desenhar_texto(f'Tempo: {tempo_restante}s', fonte, PRETO, screen, 10, 90)
        pygame.display.flip()
        clock.tick(FPS)
    return state
