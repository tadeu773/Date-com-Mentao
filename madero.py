import pygame
import random
import os
from config import *

# Dimensões da tela
largura = 800
altura = 600
bloco_largura = 70
bloco_altura = 70
velocidade_jogador = 6

# Cores
PRETO = (0, 0, 0)
VERMELHO = (200, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)

# Fonte
fonte = pygame.font.SysFont(None, 48)
fonte_pequena = pygame.font.SysFont(None, 32)

def render_text_outline(surface, text, font, pos, fg, outline, width=2):
    base = font.render(text, True, fg)
    x, y = pos
    for dx in range(-width, width+1):
        for dy in range(-width, width+1):
            if dx or dy:
                sombra = font.render(text, True, outline)
                surface.blit(sombra, (x + dx, y + dy))
    surface.blit(base, (x, y))

def jogo_madero(screen):
    clock = pygame.time.Clock()
    jogador_x = largura // 2 - bloco_largura // 2
    jogador_y = altura - bloco_altura
    blocos = []
    contador = 0
    tempo_total = 45000
    tempo_inicio = pygame.time.get_ticks()
    state = MADERO

    # Imagem da polícia
    CAMINHO_IMAGEM_POLICIA = os.path.join("Madero", "policia.png")
    img_policia = None
    if os.path.exists(CAMINHO_IMAGEM_POLICIA):
        img_policia = pygame.image.load(CAMINHO_IMAGEM_POLICIA).convert_alpha()
        img_policia = pygame.transform.scale(img_policia, (bloco_largura, bloco_altura))

    # Imagem do jogador
    CAMINHO_IMAGEM_MENTAO = os.path.join("Madero", "van_mentao.png")
    img_mentao = None
    if os.path.exists(CAMINHO_IMAGEM_MENTAO):
        img_mentao = pygame.image.load(CAMINHO_IMAGEM_MENTAO).convert_alpha()
        img_mentao = pygame.transform.scale(img_mentao, (bloco_largura, bloco_altura))

    # Fundo
    CAMINHO_IMAGEM_FUNDO = os.path.join("Fundos", "rua.jpg")
    img_fundo = None
    if os.path.exists(CAMINHO_IMAGEM_FUNDO):
        img_fundo = pygame.image.load(CAMINHO_IMAGEM_FUNDO).convert()
        img_fundo = pygame.transform.rotate(img_fundo, -90)
        img_fundo = pygame.transform.scale(img_fundo, (largura, altura))

    # CONTAGEM REGRESSIVA
    for cnt in ("3", "2", "1", "VAI!"):
        if img_fundo:
            screen.blit(img_fundo, (0, 0))
        else:
            screen.fill(PRETO)

        render_text_outline(screen, "Use as setas para se movimentar!", fonte_pequena,
                            (largura // 2 - 190, altura // 2 - 80), BRANCO, PRETO)
        render_text_outline(screen, "Desvie da polícia!", fonte_pequena,
                            (largura // 2 - 110, altura // 2 - 40), BRANCO, PRETO)
        render_text_outline(screen, cnt, fonte,
                            (largura // 2 - 20, altura // 2 + 30), BRANCO, PRETO)
        pygame.display.flip()
        pygame.time.delay(800)

    running = True

    while running:
        tempo_atual = pygame.time.get_ticks()
        tempo_passado = tempo_atual - tempo_inicio
        tempo_restante = max(0, (tempo_total - tempo_passado) // 1000)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                state = QUIT
                running = False

        # Movimento do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador_x > 0:
            jogador_x -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and jogador_x < largura - bloco_largura:
            jogador_x += velocidade_jogador
        jogador_x = max(0, min(jogador_x, largura - bloco_largura))

        # Velocidade dos blocos aumenta com o tempo
        segundos = tempo_passado // 5000
        velocidade_blocos = 4 + segundos
        tempo_para_criar = max(10, 30 - segundos)

        # Atualiza blocos
        for bloco in blocos:
            bloco['y'] += velocidade_blocos
        blocos = [b for b in blocos if b['y'] < altura]

        # Cria novos blocos
        contador += 1
        if contador >= tempo_para_criar:
            novo_x = random.randint(0, largura - bloco_largura)
            blocos.append({'x': novo_x, 'y': 0})
            contador = 0

        # Colisão
        jogador_rect = pygame.Rect(jogador_x, jogador_y, bloco_largura, bloco_altura)
        for bloco in blocos:
            bloco_rect = pygame.Rect(bloco['x'], bloco['y'], bloco_largura, bloco_altura)
            if jogador_rect.colliderect(bloco_rect):
                state = GAMEOVER
                running = False

        if tempo_passado >= tempo_total:
            state = MAPA
            progresso_jogador["madero completo"] = True
            running = False

        # Desenha fundo
        if img_fundo:
            screen.blit(img_fundo, (0, 0))
        else:
            screen.fill(PRETO)

        # Blocos da polícia
        for bloco in blocos:
            if img_policia:
                screen.blit(img_policia, (bloco['x'], bloco['y']))
            else:
                pygame.draw.rect(screen, VERMELHO, (bloco['x'], bloco['y'], bloco_largura, bloco_altura))

        # Jogador
        if img_mentao:
            screen.blit(img_mentao, (jogador_x, jogador_y))
        else:
            pygame.draw.rect(screen, VERDE, (jogador_x, jogador_y, bloco_largura, bloco_altura))

        # Tempo
        texto_tempo = fonte_pequena.render(f"Tempo: {tempo_restante}s", True, BRANCO)
        screen.blit(texto_tempo, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # MENSAGEM FINAL
    if state == MAPA:
        if img_fundo:
            screen.blit(img_fundo, (0, 0))
        else:
            screen.fill(PRETO)

        render_text_outline(screen, "Você conseguiu!", fonte,
                            (largura // 2 - 150, altura // 2 - 40), BRANCO, PRETO)
        render_text_outline(screen, "Novos diálogos no Insper desbloqueados!", fonte_pequena,
                            (largura // 2 - 200, altura // 2 + 20), BRANCO, PRETO)
        pygame.display.flip()
        pygame.time.delay(5000)

    return state
