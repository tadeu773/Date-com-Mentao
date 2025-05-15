import pygame
import random
from os import path
from config import *
from classes import *

def tela_mapa(tela):
    clock = pygame.time.Clock()

    mapa = pygame.image.load(path.join("Fundos", 'mapa.png')).convert()
    mapa = pygame.transform.scale(mapa, (WIDTH, HEIGHT))
    mapa_rect = mapa.get_rect()


    insperimg = pygame.image.load(path.join("Botoes", 'insper.png')).convert()
    insperimg = pygame.transform.scale(insperimg, (200, 100))
    botao_insper = BotaoImagem(insperimg, 50, 350)

    jkimg = pygame.image.load(path.join("Botoes", "JK.jpg")).convert()
    jkimg = pygame.transform.scale(jkimg, (200, 100))
    botao_jk = BotaoImagem(jkimg, 600, 350)

    maderoimg = pygame.image.load(path.join("Botoes", "madero.jpg")).convert()
    maderoimg = pygame.transform.scale(maderoimg, (200, 100))
    botao_madero = BotaoImagem(maderoimg, 550, 150)

    # Cria uma superfície transparente apenas para definir a área clicável
    botao_transparente_img = pygame.Surface((200, 200), pygame.SRCALPHA)
    botao_transparente_img.fill((0, 0, 0, 0))  # Totalmente transparente

# Defina a posição aproximada da piscina (ajuste os valores conforme necessário)
    botao_piscina = BotaoImagem(botao_transparente_img, 120, 80)



    running = True
    state = MAPA  # Define o estado atual

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
        
            if botao_insper.foi_clicado(event):
                state = INSPER
                running = False

            if botao_jk.foi_clicado(event):
                state = QUIT
                running = False

            if botao_madero.foi_clicado(event):
                state = QUIT
                running = False

            if botao_piscina.foi_clicado(event):
                state = PSCINA
                running = False

        tela.fill(BLACK)  # Limpa a tela
        tela.blit(mapa, mapa_rect)  # Desenha o mapa na tela

        botao_insper.desenhar(mapa)
        botao_jk.desenhar(mapa)
        botao_madero.desenhar(mapa)

        pygame.display.flip()

    return state
