import pygame
import random
import time
import os
from config import *
from classes import *

# Função para renderizar texto com contorno
def render_text_outline(surface, text, font, pos, fg, outline, width=2):
    base = font.render(text, True, fg)
    x, y = pos
    for dx in range(-width, width + 1):
        for dy in range(-width, width + 1):
            if dx or dy:
                surf = font.render(text, True, outline)
                surface.blit(surf, (x + dx, y + dy))
    surface.blit(base, (x, y))

# Tela principal do jogo
def tela_pipoca(screen):
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 26)
    fonte_grande = pygame.font.SysFont("arial", 80)

    fundo = carregar_imagem(os.path.join(IMAGENS_PIPOCA_DIR, "cinema.png"), (WIDTH, HEIGHT))

    todos_sprites = pygame.sprite.Group()
    blocos_menores = pygame.sprite.Group()

    jogador = BlocoMaior()
    todos_sprites.add(jogador)

    coletados = 0
    perdidos = 0
    tempo_total = 90
    tempo_inicio = time.time()

    # --- CONTAGEM REGRESSIVA + INSTRUÇÃO ---
    for count in ("3", "2", "1", "VAI!"):
        screen.blit(fundo, (0, 0))

        # Mensagem
        msg = "Use as setas para se movimentar! Não deixe as pipocas do Mentão cair!"
        render_text_outline(
            screen, msg, fonte,
            (WIDTH // 2 - fonte.size(msg)[0] // 2, HEIGHT // 2 - 100),
            BRANCO, PRETO, width=2
        )

        # Número/Texto central
        render_text_outline(
            screen, count, fonte_grande,
            (WIDTH // 2 - fonte_grande.size(count)[0] // 2, HEIGHT // 2),
            BRANCO, PRETO, width=3
        )

        pygame.display.flip()
        pygame.time.delay(800)

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
            state = PRE_JK
            progresso_jogador["jk completo"] = True
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
