import pygame
import random
from os import path

from config import *
from classes import *
import narrativas
import moods

# --- Caminhos absolutos relativos a este script ---
SCRIPT_DIR     = path.dirname(path.abspath(__file__))
FUNDOS_DIR     = path.join(SCRIPT_DIR, "Fundos")
MOODS_DIR      = SCRIPT_DIR
NARRATIVAS_DIR = SCRIPT_DIR

def tela_insper(screen):
    clock = pygame.time.Clock()

    # Fundo da tela Insper
    background_path = path.join(FUNDOS_DIR, 'insper_inside.jpeg')
    background = pygame.image.load(background_path).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Moods (imagens de expressão do Mentão)
    imagens_mood = {
        "feliz":    carrega_imagem(path.join('feliz.png')),
        "surpreso": carrega_imagem(path.join('surpreso.png')),
        "briga":    carrega_imagem(path.join('briga.png')),
        "bravo":    carrega_imagem(path.join('bravo.png')),
        "bebendo":  carrega_imagem(path.join('bebendo.png'))
    }

    state = INSPER
    running = True

    def sair_para_mapa():
        nonlocal state, running
        state = MAPA
        running = False

    def gameover():
        nonlocal state, running
        state = GAMEOVER
        running = False

    # Inicializa a narrativa principal OU a narrativa da insperina
    if progresso_jogador.get("insperina desbloqueada") and not progresso_jogador.get("insperina finalizada"):
        narrativas.pre_insperina(sair_para_mapa)
    else:
        narrativas.iniciar_narrativa_insper(gameover, sair_para_mapa)

    botao_sair = BotaoSair(sair_para_mapa)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            for botao in narrativas.botoes_atuais:
                botao.checar_clique(event)

            botao_sair.checar_clique(event)

        personagem_img = imagens_mood[moods.mood_mentao]
        personagem_img = pygame.transform.scale(personagem_img, (300, 300))
        personagem_rect = personagem_img.get_rect(center=(WIDTH // 2, 150))

        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        screen.blit(personagem_img, personagem_rect)

        if narrativas.fala_mentao is not None:
            Mentao.exibir(screen, narrativas.fala_mentao)

        for botao in narrativas.botoes_atuais:
            botao.desenhar(screen)
        botao_sair.desenhar(screen)

        pygame.display.flip()

    return state